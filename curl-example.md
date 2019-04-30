#### Find 20 records from offset 10 that match provided query
```
curl -X POST \
  http://localhost:8080/api/search \
  -H 'Authorization: Bearer ABCD' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "X-ray analysis of protein crystals",
    "size": 20,
    "from": 10
}'
```

#### Get title and patent citations for publication (doi)
```
curl -X POST \
  http://localhost:8080/api/search \
  -H 'Authorization: Bearer ABCD' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": {
    	"match":{
    		"external_ids.value": "10.1109/ee.1934.6540358"
    	}
    },
    "include":["title","patent_citations"]
}'
```

#### Get Scholarly metadata for a patent
```
curl -X POST \
  http://localhost:8080/api/search \
  -H 'Content-Type: application/json' \
  -d '{
	"query": {
		"match": {
			"patent_citations.lens_id": "115-570-536-815-377"
		}
	}
}'
```

#### Find recent 10 works from an institution sorted by published year

```
curl -X POST \
  http://localhost:8080/api/search \
  -H 'Content-Type: application/json' \
  -d '{
	"query": {
		"match_phrase": {
			"authors.affiliations.name": "Harvard University"
		}
	},
	"sort": [{
		"year_published": "desc"
	}],
	"size": 10
}'
```

#### Get 50 works from an institution published between two years
```
curl -X POST \
  http://localhost:8080/api/search \
  -H 'Authorization: Bearer ABCD' \
  -H 'Content-Type: application/json' \
  -d '{
	"query": {
		"bool": {
			"must": {
				"match_phrase": {
					"authors.affiliations.name": "Harvard University"
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

#### Get data having patent citations and affiliations
```
curl -X POST \
  http://localhost:8080/api/search \
  -H 'Content-Type: application/json' \
  -d '{
    "query": {
        "bool":{
            "must": [
                {"match": {"has_patent_citations": true}},
                {"match": {"has_affiliation": true}}
            ]
        }
    }
}'
```

#### Query by Author's Name
```
curl -X POST \
  http://localhost:8080/api/search \
  -H 'Authorization: Bearer ABCD' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": {
    	"match":{
    		"authors.first_name": "Sebastien"
    	}
    },
    "size": 10
}'
```
