---
layout: post-sidebar
title: Aggregations
permalink: /aggregations.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Overview
        url: aggregations.html#overview
      - page: Types of aggregation
        url: aggregations.html#types-of-aggregation
      - page: Aggregations supported in The Lens
        url: aggregations.html#aggregations-supported-in-the-lens
      - page: Nesting using sub-aggregations
        url: aggregations.html#nesting-using-sub-aggregations
      - page: Examples - Scholarly Aggregation
        url: aggregations.html#scholarly-aggregation-examples
      - page: Examples - Patent Aggregation
        url: aggregations.html#patent-aggregation-examples
---

### Overview

Lens Aggregation API enables users to calculate metrics, summarize data that can be useful for analysis. Aggregation request follows similar structure as [elasticSearch aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html).

Following aggregation endpoints are supported in The Lens:
- `POST` `/patent/aggregate`
- `POST` `/scholarly/aggregate`

Aggregation API usage endpoints: 
- `GET` `/subscriptions/patent_aggregation_api/usage`
- `GET` `/subscriptions/scholarly_aggregation_api/usage`

### Types of Aggregation

#### Metrics aggregation
These aggregations compute the metrics based on value aggregated. e.g. `cardinality`, `avg`, `max`, `min`, `sum`

#### Bucket aggregation
These aggregations do not compute metrics. They group the values if they fall into specific bucket and returns number of documents for each bucket. e.g. `terms`, `histogram` `date_histogram`, `field`, `filters`. 
Bucket aggregation supports sub-aggregations which are aggregated for the buckets created by parent aggregation.

### Aggregation Request
Following fields are supported for aggregation requests.
- `field` (required) : Supported field from tables below to aggregate results on
- `aggregations` (optional) : Sub-aggregations that can be applied for bucket based aggregation (described below)  

> Note: Some aggregation supports additional request configuration fields e.g. `interval` for `date_histogram` aggregation

> We strongly recommend applying aggregations with specific `query` and keeping the result size small to avoid slow responses or timeouts.

### Aggregations supported in The Lens

#### cardinality

Calculates approximate count of distinct values.

Product | Supported Fields
------- |-------------
**Scholarly** | `affiliation.type`, `affiliation_count`, `author.affiliation.address.city`, `author.affiliation.address.country_code`, `author.affiliation.grid.address.state_code`, `author.affiliation.grid_id`, `author.affiliation.name.exact`, `author.display_name.exact`, `author.display_name_id`, `author.display_name_orcid`, `author_count`, `author_first.display_name.exact`, `author_first.display_name_id`, `author_last.display_name.exact`, `author_last.display_name_id`, `chemical.substance_name.exact`, `citation_id_type`, `conference.name.exact`, `field_of_study`, `funding.organisation.exact`, `keyword`, `mesh_term.mesh_heading`, `open_access.colour`, `open_access.license`, `open_access.source`, `publication_type`, `reference.lens_id`, `referenced_by`, `referenced_by_count`, `referenced_by_patent.lens_id`, `referenced_by_patent_count`, `source.asjc_code`, `source.asjc_subject.exact`, `source.country`, `source.publisher.exact`, `source.title.exact`, `source.type`, `year_published`
**Patent** | `agent.country`, `agent.name.exact`, `agent_count`, `applicant.name.exact`, `applicant.residence`, `applicant_count`, `cited_by.patent.lens_id`, `cited_by.patent_count`, `class_cpc.symbol`, `class_ipcr.symbol`, `class_national.symbol`, `family.extended.id`, `family.extended.member.lens_id`, `family.extended.size`, `family.simple.id`, `family.simple.member.lens_id`, `family.simple.size`, `inventor.name.exact`, `inventor.residence`, `inventor_count`, `jurisdiction`, `kind`, `legal_status.patent_status`, `owner_all.country`, `owner_all.name.exact`, `owner_all_count`, `publication_type`, `reference_cited.npl.record_lens_id`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent.lens_id`, `reference_cited.patent_count`, `sequence.count`, `sequence.organism.name.exact`

e.g. 
```json
"citing_patents": {
    "cardinality": {
        "field": "referenced_by_patent.lens_id"
    }
}
```

#### avg

Computes the average of numeric values extracted from the aggregated documents

Product | Supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

e.g.
```json
"patent_citations": {
    "avg": {
        "field": "cited_by.patent_count"
    }
}
```

#### max

Computes the maximum of numeric values extracted from the aggregated documents

Product | Supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

e.g.
```json
"scholarly_citations": {
    "max": {
        "field": "referenced_by_count"
    }
}
```

#### min

Computes the minimum of numeric values extracted from the aggregated documents

Product | Supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

e.g.
```json
"scholarly_citations": {
    "min": {
        "field": "referenced_by_count"
    }
}
```

#### sum

Computes the sum of numeric values extracted from the aggregated documents
 
Product | Supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

e.g.
```json
"scholarly_citations": {
    "sum": {
        "field": "referenced_by_count"
    }
}
```

#### histogram

This aggregation can be applied to select integer fields. It allows the user to specify an interval value for the bucket size.

Additional request config fields:
- `interval` : supported for `histogram` with integer values.

Product | Supported Fields
------- |-------------
**Scholarly** | `patent_citation_count`, `scholarly_citation_count`, `reference_count`.
**Patent** | `cited_by.patent_count`, `reference_cited.patent_count`, `reference_cited.npl_resolved_count`, `reference_cited.npl_count`.

e.g. 
```json
{
    "query": "EV battery",
    "aggregations": {
        "refernces_cited": {
            "histogram": {
                "field": "reference_count",
                "interval": 10
            }
        }
    },
    "size": 0
}
```


#### date_histogram

This aggregation can be applied to date values extracted from documents. It allows the user to specify the interval and the values are rounded down to the closest date range bucket.

Additional request config fields:
- `interval` : supported for `date_histogram` with possible values: `QUARTER`, `YEAR`(default) and `MONTH`

Product | Supported Fields
------- |-------------
**Scholarly** | `date_published`
**Patent** | `application_reference.date`, `date_published`, `earliest_priority_claim_date`, `legal_status.anticipated_term_date`, `legal_status.grant_date`

e.g. 
```json
"date published histogram": {
    "date_histogram": {
        "field": "date_published",
        "interval": "YEAR"
    }
}
```

#### terms

It is a bucket aggregation where the buckets are dynamically built based on unique value of the field.

Additional request config fields:
- `size`: Number of (default to `10` upto `100`)
- `order`: List of sort order, default to descending document count. Following field can be used:
  - `field_value`: sort by terms value themselves  
  - `doc_count`: sort by document count
  - sub-aggregation-name - sort by user defined sub aggregation name

Product | Supported Fields
------- |-------------
**Scholarly** | `affiliation.type`, `author.affiliation.address.city`, `author.affiliation.address.country_code`, `author.affiliation.address.state_code`, `author.affiliation.name.exact`, `author.display_name.exact`, `author.display_name_id`, `author.display_name_orcid`, `author_first.display_name.exact`, `author_first.display_name_id`, `author_last.display_name.exact`, `author_last.display_name_id`, `citation_id_type`, `conference.name.exact`, `field_of_study`, `funding.country.exact`, `funding.funding_name.exact`, `funding.organisation.exact`, `mesh_term.mesh_heading`, `open_access.colour`, `open_access.license`, `open_access.source`, `publication_type`, `source.asjc_code`, `source.asjc_subject.exact`, `source.country`, `source.publisher.exact`, `source.title.exact`, `source.type`
**Patent** | `agent.country`, `agent.name.exact`, `applicant.name.exact`, `applicant.residence`, `assistant_examiner.name.exact`, `class_cpc.symbol`, `class_ipcr.symbol`, `class_national.symbol`, `examiner.name.exact`, `inventor.name.exact`, `inventor.residence`, `jurisdiction`, `kind`, `legal_status.patent_status`, `owner_all.country`, `owner_all.name.exact`, `primary_examiner.name.exact`, `publication_type`, `sequence.organism.name.exact`

e.g.

```json
{
  "query": {
    "match": {
      "title": "malaria"
    }
  },
  "aggregations": {
    "affiliation types": {
      "terms": {
        "field": "author_last.display_name.exact",
        "size": 10,
        "order": {
          "doc_count": "desc"
        }
      }
    }
  }
}
```

#### filter

It narrows the documents which matches the filter query.

- `filter` : required valid query of type `match`, `term`, `terms`, `range`

e.g.
```json
  "works_cited_by_patents": {
        "filter": {
            "term": {
                "is_referenced_by_patent": true
            }
        }
    }
```

#### filters

It is a multiple bucket aggregation that supports multiple queries.

- `filters` : required valid queries with type `match`, `term`, `terms`, `range`

e.g.
```json
  "works_cited_by": {
    "filters": {
      "filters": {
        "patent": {
          "term": {
            "is_referenced_by_patent": true
          }
        },
        "scholarly": {
          "term": {
            "is_referenced_by_scholarly": true
          }
        }
      }
    }
  }
```

#### Nesting using sub-aggregations

Bucket aggregations (`date_histogram`, `terms`, `filter`, `filters`) supports sub-aggregation.

e.g.
```json
"aggregations": {
    "date published histogram open access color": {
        "date_histogram": {
            "field": "date_published",
            "interval": "YEAR",
            "aggregations": {
                "groupings": {
                    "filters": {
                        "filters": {
                            "journal article": {
                                "match": {
                                    "publication_type": "journal article"
                                }
                            },
                            "field_of_study - biology": {
                                "match": {
                                    "field_of_study": "Biology"
                                }
                            },
                            "referenced by patent": {
                                "match": {
                                    "is_referenced_by_patent": true
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### Scholarly Aggregation Examples

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
    "aggregations": {
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
    "aggregations": {
        "date_histo": {
            "date_histogram": {
                "field": "date_published",
                "interval": "YEAR",
                "aggregations": {
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
    "aggregations": {
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
    "aggregations": {
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
    "aggregations": {
        "date_histo": {
            "date_histogram": {
                "field": "date_published",
                "interval": "YEAR",
                "aggregations": {
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

### Patent Aggregation Examples

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
    "aggregations": {
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
    "aggregations": {
        "date_histo": {
            "date_histogram": {
                "field": "date_published",
                "interval": "YEAR",
                "aggregations": {
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
    "aggregations": {
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
    "aggregations": {
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
    "aggregations": {
        "applicants": {
            "terms": {
                "field": "applicant.name.exact",
                "size": 20,
                "aggregations": {
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
    "aggregations": {
        "applicants": {
            "terms": {
                "field": "applicant.name.exact",
                "size": 20,
                "order": {
                    "patent_citations": "asc"
                },
                "aggregations": {
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
