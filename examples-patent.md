---
layout: post-sidebar
title: Patent Examples
permalink: /examples-patent.html
show_sidebar: true
sidebar: toc
toc:
  - title: Patent API Examples
    subfolderitems:
      - page: Find 20 records
        url: examples-patent.html#find-the-20-most-recently-published-patent-records-from-offset-10-that-match-the-provided-string-query
      - page: Granted Applications
        url: examples-patent.html#us-applications-granted-after-2018	
      - page: Expiring Patents
        url: examples-patent.html#us-granted-patents-expiring-between-2020-10-10---2020-10-20	
      - page: Patents with CRISPR in the title, abstract or claims
        url: examples-patent.html#chinese-patents-with-crispr-in-the-title,-abstract-or-claims-published-between-2010-09-01---2020-09-30
      - page: CRISPR Cas9 Patent applications
      	url: examples-patent.html#patent-applications-from-2012-to-2020-with-crispr-cas9-in-the-claims
<!--	
      - page: 10 most recently published works
        url: examples-patent.html#find-the-10-most-recently-published-works-from-an-institution-sorted-by-published-date
      - page: Publication year of articles cited by patents
        url: examples-patent.html#get-publication-year-of-journal-articles-cited-by-patents
      - page: 30 works published between two years
        url: examples-patent.html#get-30-works-from-an-institution-published-between-two-years
      - page: Works having patent citations and affiliations
        url: examples-patent.html#get-scholarly-works-having-patent-citations-and-affiliations
      - page: Query by author name
        url: examples-patent.html#query-by-author-name
      - page: Pubmed identifier published in 2012
        url: examples-patent.html#find-scholarly-works-with-a-pubmed-identifier-published-in-2012
      - page: Access your collection
        url: examples-patent.html#access-your-collection
      - page: Using GET Requests
        url: examples-patent.html#using-get-requests
-->
---

##### Find the 20 most recently published patent records from offset 10 that match the provided string query
```json
{
    "query": "title:\"X-ray crystallography\"",
    "size": 20,
    "from": 10,
    "sort": [
        {
            "date_published": "desc"
        }
    ]
}
```

##### US applications granted after `2018`
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match" : {
                        "legal_status.granted": true
                    }
                },
                {
                    "term" : {
                        "publication_type": "PATENT_APPLICATION"
                    }
                },
                {
                    "term" : {
                        "jurisdiction": "US"
                    }
                },
                {
                    "range": {
                        "year_published": {
                            "gte": 2018
                        }
                    }
                }
            ]
        }
    }
}
```

##### US Granted patents expiring between `2020-10-10` - `2020-10-20`
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match" : {
                        "legal_status.granted": true
                    }
                },
                {
                    "term" : {
                        "jurisdiction": "US"
                    }
                },
                {
                    "range": {
                        "legal_status.anticipated_term_date": {
                            "gte": "2020-10-10",
                            "lte": "2020-10-20"
                        }
                    }
                }
            ]
        }
    }
}
```

##### Chinese patents with `CRISPR` in the title, abstract or claims published between 2010-09-01 - 2020-09-30 
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": [
                            {
                                "match" : {
                                    "title": "CRISPR"
                                }
                            },
                            {
                                "match" : {
                                    "abstract": "CRISPR"
                                }
                            },
                            {
                                "match" : {
                                    "claim": "CRISPR"
                                }
                            }
                        ]
                    }
                },
                {
                    "term" : {
                        "jurisdiction": "CN"
                    }
                
                },
                {
                    "range" : {
                        "date_published": {
                            "gte": "2010-09-01",
                            "lte": "2020-09-30"
                        }
                    }
                
                }
            ]
        }
    },
    "size" : 10,
    "include": ["lens_id", "biblio.publication_reference", "biblio.invention_title.text", "abstract.text", "claims.claims.claim_text"]
}
```
##### Patent applications from 2012 to 2020 with `CRISPR cas9` in the claims
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "term" : {
                        "publication_type": "PATENT_APPLICATION"
                    }
                
                },
                {
                    "match" :{
                        "claim": "CRISPR cas9"
                    }
                },
                {
                    "range" : {
                        "date_published": {
                            "gte": "2012-01-01",
                            "lte": "2020-09-30"
                        }
                    }
                
                }
            ]
        }
    }
}
```

<!--
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
##### Get scholarly works using multiple pmid
```json
{
	"query": {
		"terms": {
			"pmid": ["14297189", "17475107"]
		}
	}
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
  "query": {"match_phrase": {"author.affiliation.name": "Harvard University"}},
  "sort": [{"date_published": "desc"}],
  "size": 10
}
```
##### Get publication year of journal articles cited by patents
```json
{
   "query": {
       "bool" : {
        "must": [
            {"terms": { "patent_citation.lens_id": ["020-159-299-402-960", "014-680-767-794-441"]}},
            {"match": {"source.type": "Journal"}}
        ]
      }
   },
   "include": ["year_published"],
   "size": 50
}
```
##### Get 30 works from an institution published between two years
```json
{
  "query": {
    "bool": {
      "must": {"match_phrase": {"author.affiliation.name": "Harvard University"}},
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
##### Access your collection
> `[POST] https://api.lens.org/collections/123456`
```json
{
  "query": {"match": {"title": "Malaria"}},
  "include":["title","lens_id", "authors.first_name"],
  "size":10
}
```
##### Using GET Requests
> `[GET] https://api.lens.org/collections/123456?token=[your-access-token]&size=10&query=Malaria&include=authors,lens_id&sort=desc(date_published)`

> `[GET] https://api.lens.org/scholarly/search?token=[your-access-token]&size=10&query=Malaria&include=authors,lens_id&sort=desc(date_published)`
-->
