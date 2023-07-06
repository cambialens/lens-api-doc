---
layout: post-sidebar
title: Scholar Examples
permalink: /examples-scholar.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Find 20 records
        url: examples-scholar.html#find-20-records-from-offset-10-that-match-provided-query
      - page: Get the patent citations
        url: examples-scholar.html#get-the-patent-citations-scholarly-citations-and-references-for-a-list-of-scholarly-works-using-the-lens_id
      - page: Get works using a `doi`
        url: examples-scholar.html#get-title-and-patent-citations-for-a-scholarly-work-using-a-doi
      - page: Using multiple pmid
        url: examples-scholar.html#get-scholarly-works-using-multiple-pmid
      - page: Cited by patent lens_id
        url: examples-scholar.html#get-the-metadata-for-scholarly-works-that-are-cited-by-a-list-of-patents-using-the-patent-lens_id
      - page: 10 most recently published works
        url: examples-scholar.html#find-the-10-most-recently-published-works-from-an-institution-sorted-by-published-date
      - page: Publication year of articles cited by patents
        url: examples-scholar.html#get-publication-year-of-journal-articles-cited-by-patents
      - page: 30 works published between two years
        url: examples-scholar.html#get-30-works-from-an-institution-published-between-two-years
      - page: Works having patent citations and affiliations
        url: examples-scholar.html#get-scholarly-works-having-patent-citations-and-affiliations
      - page: Query by author name
        url: examples-scholar.html#query-by-author-name
      - page: Pubmed identifier published in 2012
        url: examples-scholar.html#find-scholarly-works-with-a-pubmed-identifier-published-in-2012
      - page: Access your collection
        url: examples-scholar.html#access-your-collection
      - page: Using GET Requests
        url: examples-scholar.html#using-get-requests
  - title: Aggregation Examples
    subfolderitems:
      - page: Scholarly Metrics
        url: examples-scholar.html#scholarly-metrics-the-journal-of-contemporary-dental-practice
      - page: Nested Date Histogram
        url: examples-scholar.html#nested-date-histogram-the-journal-of-contemporary-dental-practice-scholarly-works-by-publication-type
      - page: Terms Aggregation - Publication Type
        url: examples-scholar.html#terms-aggregation-the-journal-of-contemporary-dental-practice-scholarly-works-by-publication-type
      - page: Terms Aggregation - Top Institutions
        url: examples-scholar.html#terms-aggregation-top-20-institutions-publishing-in-the-journal-of-contemporary-dental-practice
      - page: Nested Terms Aggregation - Scholarly Citations
        url: examples-scholar.html#nested-terms-aggregation-top-10-institutions-publishing-in-the-journal-of-contemporary-dental-practice-by-field-of-study-and-scholarly-citations
      - page: Nested Date Histogram - Open Access Colour Over Time
        url: examples-scholar.html#nested-date-histogram-the-journal-of-contemporary-dental-practice-open-access-colour-over-time    
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



# Aggregation Examples

##### Scholarly Metrics - The Journal of Contemporary Dental Practice
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "source.title.exact": "The Journal of Contemporary Dental Practice"
                    }
                },
                {
                    "match": {
                        "source.publisher.exact": "Jaypee Brothers Medical Publishers"
                    }
                }
            ]
        }
    },
    "aggs": {
        "works_cited_by_patents": {
            "filter": {
                "term": {
                    "is_referenced_by_patent": true
                }
            }
        },
        "citing_patents": {
            "cardinality": {
                "field": "referenced_by_patent.lens_id"
            }
        },
        "patent_citations": {
            "sum": {
                "field": "referenced_by_patent_count"
            }
        },
        "works_cited_by_scholarly": {
            "filter": {
                "term": {
                    "is_referenced_by_scholarly": true
                }
            }
        },
        "citing_scholarly_works": {
            "cardinality": {
                "field": "referenced_by"
            }
        },        
        "scholarly_citations": {
            "sum": {
                "field": "referenced_by_count"
            }
        },
        "cited_scholarly_works": {
            "cardinality": {
                "field": "reference.lens_id"
            }
        }
    },
    "size": 0
}
```

##### Nested Date Histogram - The Journal of Contemporary Dental Practice Scholarly Works by Publication Type
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "source.title.exact": "The Journal of Contemporary Dental Practice"
                    }
                },
                {
                    "match": {
                        "source.publisher.exact": "Jaypee Brothers Medical Publishers"
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

##### Terms Aggregation - The Journal of Contemporary Dental Practice Scholarly Works by Publication Type
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "source.title.exact": "The Journal of Contemporary Dental Practice"
                    }
                },
                {
                    "match": {
                        "source.publisher.exact": "Jaypee Brothers Medical Publishers"
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

##### Terms Aggregation - Top 20 Institutions Publishing in The Journal of Contemporary Dental Practice 
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "source.title.exact": "The Journal of Contemporary Dental Practice"
                    }
                },
                {
                    "match": {
                        "source.publisher.exact": "Jaypee Brothers Medical Publishers"
                    }
                }
            ]
        }
    },
    "aggs": {
        "pubtype": {
            "terms": {
                "field": "author.affiliation.name.exact",
                "size": 20,
                "order": {
                        "_count": "asc"
                    }
            }
        }
    },
    "size": 0
}
```

##### Nested Terms Aggregation - Top 10 Institutions Publishing in The Journal of Contemporary Dental Practice, by Field of Study and Scholarly Citations
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "source.title.exact": "The Journal of Contemporary Dental Practice"
                    }
                },
                {
                    "match": {
                        "source.publisher.exact": "Jaypee Brothers Medical Publishers"
                    }
                }
            ]
        }
    },
    "aggregations": {
        "institutions": {
            "terms": {
                "field": "author.affiliation.name.exact",
                "size": 10,
                "aggregations": {
                    "fields_of_study": {
                        "terms": {
                            "field": "field_of_study",
                            "size": 5
                        }
                    },
                    "scholarly_citations": {
                        "sum": {
                            "field": "referenced_by_count"
                        }
                    }
                }
            }
        }
    },
    "size": 0
}
```

##### Nested Date Histogram - The Journal of Contemporary Dental Practice Open Access Colour Over Time 
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "source.title.exact": "The Journal of Contemporary Dental Practice"
                    }
                },
                {
                    "match": {
                        "source.publisher.exact": "Jaypee Brothers Medical Publishers"
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
                    "oa-colour": {
                        "terms": {
                            "field": "open_access.colour",
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
