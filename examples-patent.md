---
layout: post-sidebar
title: Patent Examples
permalink: /examples-patent.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Find 20 records
        url: examples-patent.html#find-the-20-most-recently-published-patent-records-from-offset-10-that-match-the-provided-string-query
      - page: Granted Applications
        url: examples-patent.html#us-applications-granted-after-2018
      - page: Expiring Patents
        url: examples-patent.html#us-granted-patents-expiring-between-2020-10-10-to-2020-10-20
      - page: Patents with CRISPR in the title, abstract or claims
        url: examples-patent.html#chinese-patents-with-crispr-in-the-title-or-abstract-or-claims-published-between-2010-09-01-to-2020-09-30
      - page: CRISPR Cas9 Patent applications
        url: examples-patent.html#patent-applications-from-2012-to-2020-with-crispr-cas9-in-the-claims
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

##### US Granted patents expiring between 2020-10-10 to 2020-10-20
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

##### Chinese patents with CRISPR in the title or abstract or claims published between 2010-09-01 to 2020-09-30 
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
