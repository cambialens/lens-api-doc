---
layout: post-sidebar
title: Scholar Code Samples
permalink: /samples-scholar.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: R
        url: samples-scholar.html#r
      - page: Python
        url: samples-scholar.html#python
      - page: Java
        url: samples-scholar.html#java
      - page: NodeJs
        url: samples-scholar.html#nodejs
      - page: cURL
        url: samples-scholar.html#curl       
---

### R
```r
require(httr)
getScholarlyData <- function(token, query){
	url <- 'https://api.lens.org/scholarly/search'
	headers <- c('Authorization' = token, 'Content-Type' = 'application/json')
	httr::POST(url = url, add_headers(.headers=headers), body = query)
}
token <- 'your-access-token'
request <- '{
	"query": {
		"match_phrase": {
			"author.affiliation.name": "Harvard University"
		}
	},
	"size": 1,
	"sort": [{
		"year_published": "desc"
	}]
}'
data <- getScholarlyData(token, request)
content(data, "text")
```

#### R - Cursor Based Pagination
```r
Packages <- c("dplyr", "httr", "jsonlite")
lapply(Packages, library, character.only = TRUE)

token <- 'Your Access Token'

# this sets the maximum number of records returned per query
max_results <- 100 

getLensData<- function(token, query){
  url <- 'https://api.lens.org/scholarly/search'
  headers <- c('Authorization' = token, 'Content-Type' = 'application/json')
  httr::POST(url = url, add_headers(.headers=headers), body = query)
}

request <- paste0('{
	"query":  "malaria",
	"size": "',max_results,'",
	"scroll": "1m",
	"include": ["lens_id", "authors", "publication_type", "title"]
}')


data <- getLENSData(token, request)

record_json <- content(data, "text")

# convert json output from article search to list
record_list <- fromJSON(record_json) 

#convert it to a data frame
record_df <- data.frame(record_list) 
total<- record_list[["total"]]


# if a result contains more than the max number of records per request, use cursor based pagination
if(total > max_results) {
  
  #calculate the number of queries needed for those with more than the max number of results
  sets <- ceiling(record_list[["total"]] / max_results) 
  
  # extract the scroll id from the query to go back to the same search
  scroll_id <- record_list[["scroll_id"]] 
  
  # loop through the sets of results needed to bring back all records into a data frame
  for (i in 2:sets){ 
    #extract the latest scroll_id from the last query
    scroll_id <- record_list[["scroll_id"]] 
    
    # new query based on scroll_id and including 'include' for efficiency
    request <- paste0('{"scroll_id": "', 
                      scroll_id,
                      '", "include": ["lens_id", "authors", "publication_type", "title"]
                      }')
    
    # perform article search and extract text results
    data <- getLENSData(token, request)
    record_json <- httr::content(data, "text")
    
    # convert json output from article search to list
    record_list <- jsonlite::fromJSON(record_json) 
    new_df <- data.frame(record_list)
    
    # bind the latest search data frame to the previous data frame
    record_df <- dplyr::bind_rows(record_df,new_df) 
  } 
}
```
###### Credit: Neal Haddaway

### Python
```python
import requests
url = 'https://api.lens.org/scholarly/search'
data = '''{
     "query": {
           "match_phrase":{
                "author.affiliation.name": "Harvard University"
           }
     },
     "size": 1,
     "sort": [
           {
                "year_published": "desc"
           }
     ]
}'''
headers = {'Authorization': 'Bearer your-access-token', 'Content-Type': 'application/json'}
response = requests.post(url, data=data, headers=headers)
if response.status_code != requests.codes.ok:
  print(response.status_code)
else:
  print(response.text)
```

#### Python - Cursor Based Pagination

```python
import requests
import time
url = 'https://api.lens.org/scholarly/search'

# include fields
include = '''["patent_citations", "lens_id"]'''
# request body with scroll time of 1 minute
request_body = '''{
     "query": "Malaria",
     "size": 100,
     "scroll":"1m",
     "include": %s
}''' % include
headers = {'Authorization': 'Bearer YOUR-TOKEN', 'Content-Type': 'application/json'}

# Recursive function to scroll through paginated results
def scroll(scroll_id):
  # Change the request_body to prepare for next scroll api call
  # Make sure to append the include fields to make faster response
  if scroll_id is not None:
    global request_body
    request_body = '''{"scroll_id": "%s", "include": %s, "scroll": "1m"}''' % (scroll_id, include)

  # make api request
  response = requests.post(url, data=request_body, headers=headers) 

  # If rate-limited, wait for n seconds and proceed the same scroll id
  # Since scroll time is 1 minutes, it will give sufficient time to wait and proceed
  if response.status_code == requests.codes.too_many_requests:
    time.sleep(8)
    scroll(scroll_id)
  # If the response is not ok here, better to stop here and debug it
  elif response.status_code != requests.codes.ok:
    print(response.json())
  # If the response is ok, do something with the response, take the new scroll id and iterate
  else:
    json = response.json()
    if json.get('results') is not None and json['results'] > 0:
        scroll_id = json['scroll_id'] # Extract the new scroll id from response
        print(json['data']) #DO something with your data
        scroll(scroll_id)

# start recursive scrolling
scroll(scroll_id=None)
```

#### Python - Cursor Based Pagination - List of Identifiers
Use this script of you have a large list of Lens identifiers to send in the request. Sends 5,000 identifiers per request.

```python
import requests
import time
import itertools
import json

url = 'https://api.lens.org/scholarly/search'
headers = {'Authorization': 'Bearer YOUR-TOKEN', 'Content-Type': 'application/json'}

# Recursive function to scroll through paginated results
def scroll(scroll_id, request_body):
  # Change the request_body to prepare for next scroll api call
  # Make sure to append the include fields to make faster response
  if scroll_id is not None:
    request_body = '''{"scroll_id": "%s", "include": %s}''' % (scroll_id, include)

  # make api request
  response = requests.post(url, data=request_body, headers=headers) 

  # If rate-limited, wait for n seconds and proceed the same scroll id
  # Since scroll time is 1 minutes, it will give sufficient time to wait and proceed
  if response.status_code == requests.codes.too_many_requests:
    time.sleep(8)
    scroll(scroll_id, request_body)
  # If the response is not ok here, better to stop here and debug it
  elif response.status_code != requests.codes.ok:
    print(response.json())
  # If the response is ok, do something with the response, take the new scroll id and iterate
  else:
    json = response.json()
    scroll_id = json['scroll_id'] # Extract the new scroll id from response
    print(json['data']) #DO something with your data
    scroll(scroll_id, request_body)

include = '''["lens_id", "patent_citations"]'''
identifiers = [list of Lens identifiers which can be more than 10K]
# take 5000 at a time from the list and scroll for the 5000
for ids in itertools.batched(identifiers, 5000):
  request_body = '''{
    "query": {
        "terms":  {
          "lens_id":'''+(json.dumps(ids))+'''
      }
    },
    "include": %s
  }''' % include

  # start recursive scrolling
  scroll(scroll_id=None, request_body=request_body)
```

### Java
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class JavaSample {

    public static void main(String[] args) {
        try {
            URL url = new URL("https://api.lens.org/scholarly/search");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setConnectTimeout(30000);
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setRequestProperty("Authorization", "Bearer your-access-token");

            String request = "{\"query\":{\"match_phrase\":{\"author.affiliation.name\":\"Harvard University\"}},\"size\":10,\"sort\":[{\"year_published\":\"desc\"}]}";
            conn.getOutputStream().write(request.getBytes(StandardCharsets.UTF_8));

            if (conn.getResponseCode() != 200) {
                throw new RuntimeException(conn.getResponseCode());
            }

            BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
            String output;
            while ((output = br.readLine()) != null) {
                System.out.println(output);
            }
            conn.disconnect();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
### Java - Cursor Based Pagination - Aggregate by Journal

Use this script of you have a list of journals and want to aggregate output by journal to calculate the total scholarly citations per journal.

**Note**: If you have a large list of journals or result set, it would be better to use the [Aggregation API](https://docs.api.lens.org/aggregations.html) as this script is using recursion.  

```java
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Note: This example is using `jackson-databind` for working with json request/response.
 * To keep it simple, its using HttpURLConnection to send the http request.
 *
 */
public class ScholarlyScrollSample {

    private final static ObjectMapper objectMapper = new ObjectMapper();
    private static final String TOKEN = "YOUR_TOKEN";

    public static void main(String[] args) throws IOException {
        Map<String, CitationOutput> output = new HashMap<>();
        AtomicLong recordCounter = new AtomicLong();

        LensApiClient client = new LensApiClient(new URL("https://api.lens.org/scholarly/search")) {
            /**
             * Writing the response to Map in this example. Could be a database write if required.
             * If it's a heavy operation, a non-blocking implementation might be required.
             * @param response response from the api call
             */
            @Override
            public void consumeResponse(JsonNode response) {
                long numRecords = response.get("results").longValue();
                ArrayNode records = (ArrayNode) response.get("data");
                records.forEach(record -> {
                    String lensId = record.get("lens_id").asText();
                    String sourceTitle = record.path("source").path("title").asText();
                    int scholarlyCitationCounts = record.has("scholarly_citations_count") ? record.get("scholarly_citations_count").asInt() : 0;
                    CitationOutput existing = output.getOrDefault(sourceTitle, new CitationOutput());
                    output.put(sourceTitle, existing.merge(lensId, scholarlyCitationCounts));
                });
                recordCounter.addAndGet(numRecords);
            }
        };
        //Call the API and handle the response. Pass scrollTime e.g. "1m" since we want to scroll.
        client.scrollAndConsume(createRequest(), "1m");

        System.out.println("Completed processing " + recordCounter.get() + " records.");
        output.forEach((k, v) ->
                System.out.println(k + ": (citation count: " + v.getCitationCount() + ", records count: " + v.getRecordsCount() + ")")
        );
    }

    private static ObjectNode createRequest() throws JsonProcessingException {
        String request = "{" +
                "    \"include\": [" +
                "        \"lens_id\"," +
                "        \"scholarly_citations_count\"," +
                "        \"source.title\""+
                "    ]," +
                "    \"size\": 1000," +
                "    \"query\": {" +
                "        \"terms\": {" +
                "            \"source.title.exact\": [" +
                "                \"The Journal of Medical Sciences\"," +
                "                \"An International Journal of Otorhinolaryngology Clinics\"" +
                "            ]" +
                "        }" +
                "    }" +
                "}";
        return objectMapper.readValue(request, ObjectNode.class);
    }

    private abstract static class LensApiClient {
        private final URL url;

        private LensApiClient(URL url) {
            this.url = url;
        }

        /**
         * Perform http call and subsequent recursive calls for scrolling
         * @param request request body
         * @param scrollTime scroll context alive time e.g. 1m. Can be null if no scrolling is required
         * @throws IOException
         */
        public void scrollAndConsume(ObjectNode request, String scrollTime) throws IOException {
            if(scrollTime != null && !scrollTime.isBlank()) {
                request.put("scroll", scrollTime);
            }
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            try {
                conn.setConnectTimeout(30000);
                conn.setDoOutput(true);
                conn.setRequestMethod("POST");
                conn.setRequestProperty("Content-Type", "application/json");
                conn.setRequestProperty("Authorization", "Bearer " + TOKEN);
                conn.getOutputStream().write(objectMapper.writeValueAsBytes(request));

                //If rate-limited, wait until the next allowed call
                if (conn.getResponseCode() == 429) {
                    int sleepSeconds = Integer.parseInt(conn.getHeaderField("x-rate-limit-retry-after-seconds"));
                    System.out.println("Rate limited - sleeping for " + sleepSeconds + " seconds ...");
                    Thread.sleep(sleepSeconds * 1000L);
                    scrollAndConsume(request, scrollTime);
                } else if (conn.getResponseCode() == 200) {
                    JsonNode output = objectMapper.readTree(conn.getInputStream());
                    consumeResponse(output);
                    if (output.has("results") && output.get("results").intValue() > 0) {
                        if(output.has("scroll_id")) {
                            System.out.println("Fetched " + output.get("results") + " records. Scrolling next batch ...");
                            String scrollId = output.get("scroll_id").asText();
                            scrollAndConsume(createScrollRequest(request, scrollId), scrollTime);
                        }
                    }
                } else if(conn.getResponseCode() == 204) {
                    System.out.println("No more records found.");
                } else {
                    System.out.println("Failed with status: (" + conn.getResponseCode() + ")");
                }
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            } finally {
                conn.disconnect();
            }
        }

        /**
         * Implement this to handle the response.
         * Note: if the execution of implemented method is a heavy operation, the scroll context might get expired.
         * In such case, you should make the implementation non-blocking
         * @param response response from the api call
         */
        public abstract void consumeResponse(JsonNode response);

        /**
         * Create request for scroll based pagination
         * @param originalRequest previous request required to copy over pagination to next scroll request
         * @param scrollId scroll id from the response
         * @return scroll request
         */
        private ObjectNode createScrollRequest(ObjectNode originalRequest, String scrollId) {
            ObjectNode request = objectMapper.createObjectNode();
            JsonNode projection = originalRequest.get("include");
            request.set("include", projection);
            request.put("scroll_id", scrollId);
            return request;
        }
    }

    //Sample model schema to get citations count and records
    private static class CitationOutput {
        private Integer citationCount;
        private List<String> lensIds;

        public CitationOutput() {
            this.citationCount = 0;
            this.lensIds = new ArrayList<>();
        }

        public CitationOutput merge(String lensId, Integer citationCount) {
            this.citationCount += citationCount;
            this.lensIds.add(lensId);
            return this;
        }

        public Integer getCitationCount() {
            return citationCount;
        }

        public Integer getRecordsCount() {
            return lensIds.size();
        }
    }
}
```

### NodeJs
```javascript
var request = require('request');

var endPoint = 'https://api.lens.org/scholarly/search';
var token = 'your-access-token';
var query = {
     "query": {
           "match_phrase":{
                "author.affiliation.name": "Harvard University"
           }
     },
     "size": 10,
     "sort": [
           {
                "year_published": "desc"
           }
     ]
};

var options = {
     url: endPoint,
     body: query,
     json: true,
     headers: {
           "Authorization": "Bearer " + token
     }
}

request.post(options, function(err, res, data) {
     if (err) {
           console.log(err);
     }

     console.log(data);
});
```

### cURL
```bash
curl -X POST \
  https://api.lens.org/scholarly/search \
  -H 'Authorization: Bearer your-access-token' \
  -H 'Content-Type: application/json' \
  -d '{
	"query": {
		"bool": {
			"must": {
				"match_phrase": {
					"author.affiliation.name": "Harvard University"
				}
			},
			"filter": {
				"range": {
					"year_published": {
						"gte": "1999",
						"lte": "2000"
					}
				}
			}
		}
	},
	"size": 50
}'
```
