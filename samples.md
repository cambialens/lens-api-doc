---
layout: page
title: Code Samples
permalink: /samples.html
---

{:.table-contents}
- [R](#r)
- [Python](#python)
- [Java](#java)
- [NodeJs](#nodejs)
- [cURL](#curl)

## R
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

## Python
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

## Java
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

## NodeJs
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

## cURL
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
