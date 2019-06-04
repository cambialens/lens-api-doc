---
layout: page
title: Examples
permalink: /examples/
---
##### Find 20 records from offset 10 that match provided query
```json
{
    "query": "X-ray analysis of protein crystals",
    "size": 20,
    "from": 10
}
```

##### Get title and patent citations for publication (doi)
```json
{
    "query": {
    	"match":{
    		"external_ids.value": "10.1109/ee.1934.6540358"
    	}
    },
    "include":["title","patent_citations"]
}
```
##### Get Scholarly metadata for a patent
```json
{
	"query": {
		"match": {
			"patent_citations.lens_id": "115-570-536-815-377"
		}
	}
}
```

##### Find recent 10 works from an institution sorted by published year

```json
{
	"query": {
		"match_phrase": {
			"authors.affiliations.name": "Harvard University"
		}
	},
	"sort": [{
		"year_published": "desc"
	}],
	"size": 10
}
```

##### Get 100 works from an institution published between two years
```json
{
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
	"size": 100
}
```

##### Get data having patent citations and affiliations
```json
{
    "query": {
        "bool":{
            "must": [
                {"match": {"has_patent_citations": true}},
                {"match": {"has_affiliation": true}}
            ]
        }
    }
}
```

##### Query by Author's Name

```json
{
    "query": {
    	"match":{
    		"authors.first_name": "Sebastien"
    	}
    },
    "size": 10
}
```

##### Find record by external id and value
```json
{
    "query": {
        "bool":{
             "must":[
                 {"term":{"external_ids.value": "6359161"}},
                 {"term":{"external_ids.type": "pmid"}}
              ]
         }
    },
    "include":["patent_citation_count", "external_ids"]
}
```

OR using String Based Query

```json
{
    "query": "external_ids.value: 6359161 AND external_ids.type: pmid",
    "include":["patent_citation_count", "external_ids"]
}
```
