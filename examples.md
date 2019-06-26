---
layout: page
title: Examples
permalink: /examples.html
---
##### Find 20 records from offset 10 that match provided query
```json
{
    "query": "X-ray analysis of protein crystals",
    "size": 20,
    "from": 10
}
```

##### Get the patent citations, scholarly citations and references for a list of scholarly works using the `lens_id`
```json
{
    "query": {
        "terms":{
            "lens_id": ["017-767-306-508-482", "017-624-265-921-255"]
        }
    },
    "include": ["lens_id", "patent_citations", "scholarly_citations", "references"]
}
```

##### Get title and patent citations for a scholarly work using a `doi`
```json
{
    "query": {
    	"match":{
    		"doi": "10.1109/ee.1934.6540358"
    	}
    },
    "include":["title","patent_citations"]
}
```
##### Get the metadata for scholarly works that are cited by a list of patents using the patent lens_id
```json
{
	"query": {
		"terms": {
			"patent_citation.lens_id":["198-832-374-467-397", "092-513-162-449-806"]
		}
	}
}
```

##### Find the 10 most recently published works from an institution (sorted by published date)

```json
{
	"query": {
		"match_phrase": {
			"author.affiliation.name": "Harvard University"
		}
	},
	"sort": [{
		"date_published": "desc"
	}],
	"size": 10
}
```

##### Get 30 works from an institution published between two years
```json
{
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
	"size": 30
}
```

##### Get scholarly works having patent citations and affiliations
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

##### Query by author name

```json
{
    "query": {
        "match_phrase": {"author.display_name": "Craig Venter"}
    },
    "sort": [{"year_published": "desc"}],
    "size": 10
}
```

##### Find scholarly works with a Pubmed identifier published in 2012
```json
{
    "query": {
        "bool":{
             "must":[
                {"match":{"external_id_type": "pmid"}},
			          {"match":{"year_published": 2012}}
              ]
        }
    },
    "include":["patent_citations_count", "external_ids"]
}
```

OR using String Based Query

```json
{
    "query": "external_id_type: pmid AND year_published: 2012",
    "include":["patent_citations_count", "external_ids"]
}
```
