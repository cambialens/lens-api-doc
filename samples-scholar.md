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
    request_body = '''{"scroll_id": "%s", "include": %s}''' % (scroll_id, include)

  # make api request
  response = requests.post(url, data=request_body, headers=headers) 

  # If rate-limited, wait for n seconds and proceed the same scroll id
  # Since scroll time is 1 minutes, it will give sufficient time to wait and proceed
  if response.status_code == requests.codes.too_many_requests:
    time.sleep(8)
    scroll(scroll_id)
  # If the response is not ok here, better to stop here and debug it
  elif response.status_code != requests.codes.ok:
    print response.json()
  # If the response is ok, do something with the response, take the new scroll id and iterate
  else:
    json = response.json()
    scroll_id = json['scroll_id'] # Extract the new scroll id from response
    print json['data'] #DO something with your data
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
    print response.json()
  # If the response is ok, do something with the response, take the new scroll id and iterate
  else:
    json = response.json()
    scroll_id = json['scroll_id'] # Extract the new scroll id from response
    print json['data'] #DO something with your data
    scroll(scroll_id, request_body)

include = '''["lens_id", "patent_citations"]'''
identifiers = [list of Lens identifiers which can be more than 10K]
# take 5000 at a time from the list and scroll for the 5000
for ids in itertools.islice(identifiers, 5000):
  request_body = '''{
    "query": {
        "terms":  {
          "lens_id":'''+(json.dumps(ids))+'''
      }
    },
    "include": %s
  }''' % include

  # start recursive scrolling
  scroll(scroll_id=None, request_body)
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
