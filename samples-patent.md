---
layout: post-sidebar
title: Patent Code Samples
permalink: /samples-patent.html
show_sidebar: true
sidebar: toc
toc:  
  - title: Table of Contents
    subfolderitems:
      - page: R
        url: samples-patent.html#r
      - page: Python
        url: samples-patent.html#python
      - page: Java
        url: samples-patent.html#java
      - page: NodeJs
        url: samples-patent.html#nodejs
      - page: cURL
        url: samples-patent.html#curl    
---


### R
```r
require(httr)
getPatentData <- function(token, query){
	url <- 'https://api.lens.org/patent/search'
	headers <- c('Authorization' = token, 'Content-Type' = 'application/json')
	httr::POST(url = url, add_headers(.headers=headers), body = query)
}
token <- 'your-access-token'
request <- '{
                "query": {
                    "terms":  {
                        "lens_id": ["031-156-664-516-153"]
                    }
                },
                "include": ["biblio", "doc_key"]
}'
data <- getPatentData(token, request)
content(data, "text")
```

### Python
```python
import requests
url = 'https://api.lens.org/patent/search'
data = '''{
              "query": {
                  "terms":  {
                      "lens_id": ["031-156-664-516-153"]
                  }
              },
              "include": ["biblio", "doc_key"]
}'''
headers = {'Authorization': 'Bearer your-access-token', 'Content-Type': 'application/json'}
response = requests.post(url, data=data, headers=headers)
if response.status_code != requests.codes.ok:
  print(response.status_code)
else:
  print(response.text)
```

#### Cursor based pagination

```python
import requests
import time
url = 'https://api.lens.org/patent/search'

# include fields
include = '''["biblio", "doc_key"]'''
# request body with scroll time of 1 minute
request_body = '''{
  "query": {
      "terms":  {
          "lens_id": ["031-156-664-516-153"]
      }
  },
  "include": %s,
  "scroll": "1m"
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

### Java
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class JavaSample {

    public static void main(String[] args) {
        try {
            URL url = new URL("https://api.lens.org/patent/search");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setConnectTimeout(30000);
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setRequestProperty("Authorization", "Bearer your-access-token");

            String request = "{\"query\":{\"terms\":{\"lens_id\":[\"031-156-664-516-153\"]}},\"include\":[\"biblio\",\"doc_key\"]}";
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

var endPoint = 'https://api.lens.org/patent/search';
var token = 'your-access-token';
var query = {
  "query": {
      "terms":  {
          "lens_id": ["031-156-664-516-153"]
      }
  },
  "include": ["biblio", "doc_key"]
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
  https://api.lens.org/patent/search \
  -H 'Authorization: Bearer your-access-token' \
  -H 'Content-Type: application/json' \
  -d '{
        "query": {
            "terms":  {
                "lens_id": ["031-156-664-516-153"]
            }
    },
    "include": ["biblio", "doc_key"]
  }'
```
