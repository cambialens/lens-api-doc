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
data = '''{
  "query": {
      "terms":  {
          "lens_id": ["031-156-664-516-153"]
      }
  },
  "include": ["biblio", "doc_key"]
}'''
headers = {'Authorization': 'Bearer your_token', 'Content-Type': 'application/json'}

def scroll(scroll_id):
  if scroll_id is not None:
    global data
    data = '''{"scroll_id": "%s"}''' % scroll_id
  response = requests.post(url, data=data, headers=headers) 
  if response.status_code != requests.codes.ok:
    print response
  elif response.status_code == requests.codes.too_many_requests:
    time.sleep(8)
    scroll(scroll_id)
  else:
    json = response.json()
    scroll_id = json['scroll_id']
    print json['data'] #DO something with your data
    scroll(scroll_id)

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
