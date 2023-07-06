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
      - page: US Patents by document number
        url: examples-patent.html#us-patents-by-document-number
      - page: Search for Dcument Identifiers
        url: examples-patent.html#search-for-document-identifiers
  - title: Aggregation Examples
    subfolderitems:
      - page: Patent Metrics
        url: examples-patent.html#metrics-for-ibm-patents
      - page: Nested Date Histogram
        url: examples-patent.html#nested-date-histogram-for-ibm-patents-published-after-1980-by-document-type
      - page: Terms Aggregation - Document Type
        url: examples-patent.html#terms-aggregation-ibm-patents-by-document-type
      - page: Terms Aggregation - Top Applicants
        url: examples-patent.html#terms-aggregation-top-applicants-by-active-granted-patents-published-since-1980      
      - page: Nested Terms Aggregation - Top Applicants by Legal Status
        url: examples-patent.html#nested-terms-aggregation-top-applicants-granted-patents-published-since-1980-by-legal-status       
      - page: Nested Terms Aggregation - Top Applicants by Patent Citations
        url: examples-patent.html#nested-terms-aggregation-top-applicants-granted-patents-published-since-1980-by-patent-citations    
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

##### US Patents by document number
```json
{
    "query": {
        "bool": {
            "must": [
                {"terms": {"doc_number": ["8625931", "8626565","8626684"]}},
                {"term": {"jurisdiction": "US"}}
            ]
        }
    },
    "size": 10,
    "include": ["lens_id", "biblio.publication_reference", "biblio.invention_title", "abstract", "claims"]
}
```

##### Search for document identifiers
```json
{
    "query": {
        "terms": {
            "ids": ["US 8625931", "US_8626565_B2", "EP_0227762_B1_19900411", "EP 0227762 B1", "EP_0227762_B1", "EP0227762B1", "EP0227762", "145-564-229-856-440", "US 7,654,321 B2", "7,654,321", "US 2021/0191781 A1"]
        }
    },
    "size": 10,
    "include": ["lens_id", "biblio.publication_reference", "biblio.invention_title", "abstract", "claims"]
}
```


##### Using GET Requests

> `[GET] https://api.lens.org/patent/search?token=[your-access-token]&size=10&query=YOUR_QUERY&include=biblio,lens_id&sort=desc(date_published)`


# Aggregation Examples

##### Metrics for IBM patents
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "owner.name.exact": "International Business Machines Corporation"
                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "date_published": {
                            "gte": "1980-01-01"
                        }
                    }
                }
            ]
        }
    },
    "aggs": {
        "simple_families": {
            "cardinality": {
                "field": "family.simple.id"
            }
        },
        "extended_families": {
            "cardinality": {
                "field": "family.extended.id"
            }
        },
        "cites_patents": {
            "filter": {
                "term": {
                    "cites_patent": true
                }
            }
        },
        "cited_by_patents": {
            "filter": {
                "term": {
                    "cited_by_patent": true
                }
            }
        },
        "citing_patents": {
            "cardinality": {
                "field": "cited_by.patent.lens_id"
            }
        },
        "patent_citations": {
            "avg": {
                "field": "cited_by.patent_count"
            }
        },
        "cited_patents": {
            "cardinality": {
                "field": "reference_cited.patent.lens_id"
            }
        },
        "cites_npl": {
            "filter": {
                "term": {
                    "cites_npl": true
                }
            }
        },
        "npl_citations": {
            "sum": {
                "field": "reference_cited.npl_count"
            }
        },
        "cites_resolved_npl": {
            "filter": {
                "term": {
                    "cites_resolved_npl": true
                }
            }
        },
        "resolved_npl_citations": {
            "avg": {
                "field": "reference_cited.npl_resolved_count"
            }
        },
        "citied_scholarly_works": {
            "cardinality": {
                "field": "reference_cited.npl.record_lens_id"
            }
        }
    },
    "size": 0
}
```

##### Nested Date Histogram for IBM patents published after `1980` by document type 
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "owner.name.exact": "International Business Machines Corporation"
                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "date_published": {
                            "gte": "1980-01-01"
                        }
                    }
                }
            ]
        }
    },
    "aggs": {
        "date_histo": {
            "date_histogram": {
                "field": "date_published",
                "interval": "YEAR",
                "aggs": {
                    "pubtype": {
                        "terms": {
                            "field": "publication_type",
                            "size": 20
                        }
                    }
                }
            }
        }
    },
    "size": 0
}
```

##### Terms Aggregation - IBM patents by document type
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "owner.name.exact": "International Business Machines Corporation"
                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "date_published": {
                            "gte": "1980-01-01"
                        }
                    }
                }
            ]
        }
    },
    "aggs": {
        "pubtype": {
            "terms": {
                "field": "publication_type",
                "size": 20
            }
        }
    },
    "size": 0
}
```

#####  Terms Aggregation - Top Applicants by Active Granted Patents published since `1980`
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "legal_status.patent_status": "active"
                    }
                },
                {
                    "match": {
                        "publication_type": "granted_patent"
                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "date_published": {
                            "gte": "1980-01-01"
                        }
                    }
                }
            ]
        }
    },
    "aggs": {
        "top_applicants": {
            "terms": {
                "field": "applicant.name.exact",
                "size": 20
            }
        }
    },
    "size": 0
}
```
##### Nested Terms Aggregation - Top Applicants Granted Patents published since `1980` by Legal Status
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "publication_type": "granted_patent"
                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "date_published": {
                            "gte": "1980-01-01"
                        }
                    }
                }
            ]
        }
    },
    "aggs": {
        "applicants": {
            "terms": {
                "field": "applicant.name.exact",
                "size": 20,
                "aggs": {
                    "legal_status": {
                        "terms": {
                            "field": "legal_status.patent_status",
                            "size": 10
                        }
                    }
                }
            }
        }
    },
    "size": 0
}
```

##### Nested Terms Aggregation - Top Applicants Granted Patents published since `1980` by Patent Citations
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "publication_type": "granted_patent"
                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "date_published": {
                            "gte": "1980-01-01"
                        }
                    }
                }
            ]
        }
    },
    "aggs": {
        "applicants": {
            "terms": {
                "field": "applicant.name.exact",
                "size": 20,
                "order": {
                    "patent_citations": "asc"
                },
                "aggs": {
                    "patent_citations": {
                        "sum": {
                            "field": "cited_by.patent_count"
                        }
                    }
                }
            }
        }
    },
    "size": 0
}
```
