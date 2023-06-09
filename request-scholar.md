---
layout: post-sidebar
title: Scholar Request
permalink: /request-scholar.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Request Structure
        url: request-scholar.html#request-structure
      - page: Searchable Fields
        url: request-scholar.html#searchable-fields
      - page: Filters
        url: request-scholar.html#filtering
      - page: Pagination
        url: request-scholar.html#pagination
      - page: Sorting
        url: request-scholar.html#sorting
      - page: Projection
        url: request-scholar.html#projection
      - page: Supported Query Types
        url: request-scholar.html#supported-query-types
---

### Request Structure
The request fields are used in queries and sort operations. The request payload should comply with following `json` schema.

Fields | Description |  Required
------- | ------| -------
**[query](#supported-query-types)** | Valid json search request | true
**[sort](#sorting)** | Use available fields to sort results by ascending/descending order. | false
**[include](#projection)** | Only get specific fields from API response. By default all fields are selected. | false
**[exclude](#projection)** | Get all fields except undesired ones in search result. | false
**[size](#pagination)** | Integer value to specify number of items per page | false
**[from](#pagination)** | Integer value, defines the offset from the first result | false
**[scroll_id](#pagination)** | Pagination parameter | false (true for next scroll requests)
**[scroll](#pagination)** | Lifespan of Scroll scroll context in minute (e.g. 1m) | false (true for scroll context)
**[stemming](#stemming)** | Change the ability to reduce the search word into root form | false (true by default)
**[regex](#regex)** | For Query String based queries containing regular expressions | false (false by default)
**[min_score](#minimum-score)** | For limiting the response to the most relevant results, e.g. `"min_score": 14` | false
{: .param-def }

### Searchable Fields
For searching, the following fields are supported in the API:

Field | Type | Description
-------- | --------- | -------
**lens_id** | String | Unique lens identifier e.g. `100-004-910-081-14X`
**patent_citation.lens_id** | String | ID of Referenced by patents
**patent_citation_count** | Integer | Number of patent citations
**external_id_type** | String | External Identifier type (Crossref: `doi`, Microsoft Academic: `magid`, PubMed: `pmid`, PubMed Central: `pmcid`, CORE: `coreid`)
**ids.doi** | String | Crossref DOI Identifier
**ids.pmid** | String | PubMed ID Identifier
**ids.pmcid** | String | PubMed Central ID Identifier
**ids.magid** | String | Microsoft Academic ID
**ids.coreid** | String | CORE Identifier
**ids.openalex** | String | OpenAlex Identifier
**created** | Date | Record created date e.g. `2018-05-12`, `2016-08-01T00:00:00+00:00`
**publication_type** | String | Publication Type `conference proceedings`, `book chapter`, `journal article`, `component`, `conference proceedings article`, `dataset`, `libguide`, `reference entry`, `book`. N.B. this field is case sensitive.
**publication_supplementary_type** | String | Supplementary publication type e.g. `review`, `comparative study`, `research support`. N.B. this field is case sensitive.
**author.collective_name** | String | Author Collective Name
**author.first_name** | String | The author's first name e.g. `Alexander`
**author.last_name** | String | The author's last name e.g. `Kupco`
**author.initials** | String | Author Initials e.g. `A`
**author.display_name** | String | Author's full name e.g. `Alexander Kupco`
**author.magid** | String | Author MAG identifier 
**author.orcid** | String | Author ORCID identifier e.g. `0000-0001-5352-4498`
**author.affiliation.name** | String | The institution associated with the author affiliations. e.g. `Stony Brook`
**author.affiliation.name.exact** | String | Exactly matches the full institution name, e.g. `Stony Brook University`. N.B. this field is case sensitive.
**author.affiliation.name_original** | String | The author's original affiliation including the institution name and address. e.g. `School of Engineering and Applied Sciences, Harvard University, Cambridge, Massachusetts USA`
**author.affiliation.grid_id** | String | The institution GRID identifier e.g. `grid.9018.0`. N.B. GRID identifiers will be deprecated in future and replaced with [ROR identifiers](https://ror.org/).
**author.affiliation.ror_id** | String | The institution ROR identifier e.g. `03yrm5c26`. N.B. this field is case sensitive.
**author.affiliation.country_code** | String | The institution Country Code e.g. `US`,`DE`,`CH`,`FR`, etc. *N.B* this field will be deprecated in future, we recommend using the `author.affiliation.address.country_code` field instead. 
**author.affiliation.address.country_code** | String | The alpha-2 country code of the institution e.g. `US`,`DE`,`CH`,`FR`, etc. N.B. this field is case sensitive.
**author.affiliation.address.city** | String | The institution city e.g. `Tokyo`. N.B. this field is case sensitive.
**author.affiliation.address.state_code** | String | The institution state e.g. `US-NY`. N.B. this field is case sensitive.
**author.affiliation.type** | String | The institution type e.g. `Government`, `Company`, `Facility`, `Healthcare`, `Education`. N.B. this field is case sensitive.
**title** | String | Title of the scholarly work e.g. `Malaria`
**language** | String | Languages e.g. `en`, `de`, `fr`, `zh_chs`
**chemical.mesh_ui** | String | Chemical MeSH term unique identifier e.g. `D000293`. N.B. this field is case sensitive.
**chemical.registry_number** | String | Chemical registration number e.g. `5Q7ZVV76EI`
**chemical.substance_name** | String | Substance name e.g. `Antimalarials`
**clinical_trial.id** | String | Clinical trial Identifier e.g. `nct00105716`. N.B. this field is case sensitive.
**clinical_trial.registry** | String | Clinical Trial Registry e.g. `10.18810/clinical-trials-gov`. N.B. this field is case sensitive.
**field_of_study** | String | Fields Of Study e.g. `Immunology`, `Malaria`
**abstract** | String | Scholarly work abstract text
**full_text** | String | Full Text
**date_published** | Date | Date of publication e.g. `2009-05-22`
**year_published** | Integer | Year of publication e.g. `1986`
**conference.name** | String | Conference Name e.g. `International Electron Devices Meeting`
**conference.instance** | String | Conference Instance Name e.g. `CHI 1985`. N.B. this field is case sensitive.
**conference.location** | String | The location of the conference e.g. `Lihue, Kauai, HA, USA`. N.B. this field is case sensitive.
**author_count** | Integer | Number of Authors
**reference_count** | Integer | The number of works in the reference list of a scholarly work
**reference.lens_id** | String | The Lens ID of scholarly works cited in the reference list e.g. `007-899-176-416-740`
**scholarly_citation_count** | Integer | The number of scholarly works that cite this scholarly work
**open_access.license** |  String | The Open Access license type e.g. `cc-by`. N.B. this field is case sensitive.
**open_access.colour** |  String | The Open Access colour category e.g. `gold`, `green`, `bronze`, `hybrid`, `unknown`. N.B. this field is case sensitive.
**source.title** | String | The name of source publication in which the scholarly work appears e.g. Journal name, Book title, Conference proceedings
**source.title.exact** | String | The full name of source publication for exact match. N.B. this field is case sensitive.
**source.type** | String | Source Type e.g. `Journal`, `Book Series`
**source.publisher** | String | The publisher of the source publication `Elsevier`, `Wiley`, `American Medical Association`
**source.issn** | String | The International Standard Serial Number of the source publication, without hyphenation e.g. `00222836`, `1474547x`. N.B. this field is case sensitive.
**source.country** |  String | The publisher's country e.g. `United States`, `United Kingdom`. N.B. this field is case sensitive.
**source.asjc_codes** |  String | The All Science Journal Classification (ASJC) code e.g. `2735`
**source.asjc_subjects** |  String | Subject is derived from journals descriptions in Crossref metadata based on the Science Journal Classification Codes e.g. `Pediatrics`, `Microbiology`, `Biophysics`
**keyword** | String | Keywords for the scholarly work from PubMed. N.B. this field is case sensitive.
**mesh_term.mesh_ui** | String | MeSH term unique identifier. MeSH terms are the National Library of Medicine’s controlled vocabulary or subject heading list. e.g. `D000293`. N.B. this field is case sensitive.
**mesh_term.mesh_heading** | String | MeSH terms are the National Library of Medicine’s controlled vocabulary or medical subject headings assigned to PubMed entries. e.g. `Phosphates`, `Immunochemistry`. N.B. this field is case sensitive.
**mesh_term.qualifier_id** | String | Mesh Term Qualifier ID e.g. `Q000032`
**mesh_term.qualifier_name** | String | Mesh Term Qualifier Name e.g. `pathology`, `immunology`, `analysis`
**funding.organisation** | String | Name of the funding organisation e.g. `NIDCR NIH HHS`
**funding.organisation.exact** | String | For exact matches of full organisational name. N.B. this field is case sensitive.
**funding.funding_id** | String | The funding organisation's project identifier e.g.`U01 DE018902`. N.B. this field is case sensitive.
**funding.country** | String | The country of the funding body e.g. `United States`, `Germany`, `United Kingdom`
{: .param-def }

### Filtering
You can use following pre-defined filters to refine search results:

Field | Description |  Possible Value
------- | ------| -------
**is_referenced_by_scholarly** | Indicates if the scholarly work has been cited by a another scholarly work at least once. | `true`/`false`
**has_patent_citations** | Indicates if the scholarly work has been cited by a patent document. | `true`/`false`
**has_affiliation** | Has affiliation | `true`/`false`
**has_affiliation_grid** | Has affiliation GRID identifier. N.B. GRID identifiers will be deprecated in future and replaced with [ROR identifiers](https://ror.org/) | `true`/`false`
**has_affiliation_ror** | Has affiliation ROR identifier | `true`/`false`
**has_orcid** | Has an author ORCID identifier | `true`/`false`
**has_mesh_term** | Has MeSH term | `true`/`false`
**has_chemical** | Indicates if the scholarly work has an associated chemical substance  | `true`/`false`
**has_keyword** | Indicates if the scholarly work has keyword | `true`/`false`
**has_clinical_trial** | Indicates if the scholarly work has clinical trial | `true`/`false`
**has_field_of_study** | Flags if the scholarly work has a Field of Study | `true`/`false`
**has_abstract** | Indicates if the scholarly work has abstract | `true`/`false`
**has_fulltext** | Indicates if the scholarly work has fulltext | `true`/`false`
**has_funding** | Indicates if the scholarly work has funding information | `true`/`false`
**is_open_access** | Flags if the scholarly work has is Open Access | `true`/`false`
**in_analytics_set** | Indicates if the scholarly work is part of the analytic dataset. | `true`/`false`
**source.is_diamond** | Non-APC Journal flag - Indicates if the journal does not have article processing charges (APCs), i.e. Diamond Open Access journals. | `true`/`false`

{: .param-def }

 Example:
```json
{
  "query": {
     "match":{
     	  "has_patent_citations": true
     }
  }
}
```

### Pagination
Lens API provides two type of pagination based on their use:

##### Offset/Size Based Pagination

Use parameter `from` to define the offset and `size` to specify number of records expected. This is useful when you want to skip some records and select desired ones. Example below skips first 100 and select 50 records after that.
```json
{
  "query": "Malaria",
  "from": 100,
  "size":50
}
```
Similarly for `GET` requests, the following parameters are applicable: `size=50&from=100`
> **Note**: 
> - Offset/size based paginations is suitable for small result sets only and does not work on result sets of more that **10,000** records. For larger volume data downloads, use Cursor Based Pagination.

##### Cursor Based Pagination

You can specify records per page using `size` (default 20 and max 1000) and context alive time `scroll` (default 1 minute). You will receive a `scroll_id` in response, which should be passed via request body to access next set of results. Since the `scroll_id` tends to change every time after each successful requests, please use the most recent `scroll_id` to access next page. This is not suited for real time user requests.

```json
{
  "scroll_id": "MjAxOTEw;DnF1ZXJ...R2NZdw==",
  "scroll": "1m"
}
```
> **Note**: 
> - The lifespan of scroll_id is limited to 1 minute for the current API version. Using expired scroll_id will result bad request HTTP response.
> - Parameter `size` will be used for first scroll query and will remain the same for whole scroll context. Hence, using size in each scroll request will not have any effect.
> - Cursor based pagination is only applicable to `POST` requests.
> - For optimal performance, we recommend limiting the number of items (e.g. `lens_ids`) in a single terms query to 10,000.


### Sorting
Result can be retrieved in ascending or descending order. Use the following format and [fields](#searchable-fields) to apply sorting to the API response. Results can also be sorted by relevance score using `relevance`.
```json
{
  "sort": [
      {"patent_citation_count":"desc"},
      {"year_published": "asc"},
      {"relevance": "desc"}
  ]
}
```
For `GET` requests following structure is applicable: `sort=desc(patent_citation_count),asc(date_published),desc(relevance)`

### Projection
You can control the output fields in the API [Response] using projection. There are two possible ways to do that.
1. **include**: Only request specific fields from the API endpoint
2. **exclude**: Fields to be excluded from result

```json
 {"include":["title","patent_citations","authors.affiliations.name"]}
```
```json
 {"exclude":["external_ids","references"]}
```
For `GET` requests following structure is applicable.
`include=authors,lens_id`
> **Note**: Both *include* and *exclude* can be used in same request.

### Stemming
Stemming allows to reduce the words to root form. E.g. Constructed and constructing will be stemmed to root construct.
Since sometime the default stemming might not give you exact result, disabling it will just search for provided form of the word.
e.g. `"stemming": false`

### Regex
Regex allows the use of regular expressions in [Query String based query](#query-string-based-query), e.g. `"regex": true`
```json
{
    "query": "field_of_study:/.*[Ee]conom.*/",
    "regex": true
}
```
### Minimum Score
The minimum score represents the `relevance` score based on the query matching score used in Elasticsearch. This can be used to This can be used to limit the response to the most relevant results and can be used in 2-steps:

   1. Perform an initial API request to get the `max_score`. N.B. the size of the request needs to be greater than 0 to return the `max_score`.
   2. You can then filter by the `min_score` in subsequent requests.

For example, if the `max_score` is 14.9 and there are 236K results in total from the initial request, you can pass the `min_score` as 14 (i.e. less than max_score) in the subsequent request to limit the response to the most relevant results only.

> **Note**:
>  * The `max_score` will be returned as 0 if size is 0 or if a sort is applied.
>  * Passing the `min_score` as x% of `max_score` may not result in top x% results.
>  * The score is calculated for each query by Elasticsearch, and so the `max_score` value will be different for each query.
>  * The `max_score` will be returned as 0 if sorting by any fields other than `relevance`, i.e. `{"relevance": "desc"}`.

### Supported Query Types
Following queries are supported by current version of Lens API:
> **Note**: The Lens API query requests use a modified form of the Elasticsearch Query DSL. For more details on the Elasticsearch query syntax, we recommend reading this guide on the query syntax: [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

##### Term Query
[Term Query] operates in a single term and search for *exact term* in the field provided.
> Example: Find record by publication type
```json
{
    "query": {
        "term": {
            "publication_type": "journal article"
        }
    }
}
```

##### Terms Query
[Terms Query] allows you to search multiple *exact terms* for a provided field. A useful scenario is while searching multiple identifiers.
> Example: Search scholarly works for multiple pmid
```json
{
	"query": {
		"terms": {
			"pmid": ["14297189", "17475107"]
		}
	}
}
```
> **Note**: 
> Avoid using the [Term](#term-query) and [Terms](#terms-query) queries for text fields. To search text field values, we recommend using the [Match](#match-query) and [Match Phrase](#match-phrase-query) queries instead.

##### Match query
[Match query] accepts text/numbers/dates. The main use case of the match query is full-text search.
It matches each words separately. If you need to search whole phrase use [match phrase](#match-phrase-query) query.
> Example:
```json
{
  "query": {
      	"match":{
      		"author.affiliation.name": "Harvard University"
      	}
   }
}
```

##### Match Phrase query
[Match phrase query] accepts text/numbers/dates. The main use case for the match query is for full-text search.
> Example:
```json
{
  "query": {
      	"match_phrase":{
      		"author.affiliation.name": "Harvard University"
      	}
   }
}
```

> **Note**: Both **Match** and **Match Phrase** are used for text searching but the difference is how they do it. For example, searching for `"Cleveland, OH"` differs between Match and Match Phrase like this:
>* **Match**: standard search in which each word is matched separately (for example: `Cleveland` OR `OH`)
>* **Match Phrase**: matches the exact phrase provided. In this case it will match the exact text `Cleveland, OH`




##### Range query
[Range query] query to match records within the provided range.
> Example: Get record for year published between years 1980 and 2000
```json
{
  "query": {
      	"range": {
            "year_published": {
                "gte": "1980",
                "lte": "2000"
            }
        }
   }
}
```

##### Boolean query
[Bool Query] allows to combine multiple queries to create complex query providing precise result. It can be created using one or more of these clauses: `must`, `should`, `must_not` and `filter`. You can use `must` for `AND` operation and `should` for `OR`.
> Example: Get journal article scholarly works of Author with last name Kondratyev having patent citations.
```json
{
 "query": {
   "bool": {
     "must": [{
       "match": {
         "has_patent_citations": true
       }},
       {"bool": {
         "must": [
           {"match": {"publication_type": "journal article"}},
           {"match": {"author.last_name": "Kondratyev"}}
         ]
       }
       }
     ]
   }
 }
}
```

##### Query String Based Query
Query different terms with explicit operators `AND`/`OR`/`NOT` to create a compact query string.
>Example: Find works from institution published between two dates having some title.
```json
{"query": "(title:Dimensions AND author.affiliation.name:(Harvard University)) AND year_published:[2000 TO 2018]"}
```

If you need to use any [reserved special characters](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#_reserved_characters), you should escape them with leading backslash.
>Example: Getting by doi identifier using string based query
```json
{"query": "doi:10.1109\\/ee.1934.6540358"}
```
You can use json based format for string based query and mixed with complex boolean queries like this:

```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "query_string": {
                        "query": "\"X-ray analysis of protein crystals\"",
                        "fields": [
                            "title",
                            "abstract",
                            "full_text"
                        ],
                        "default_operator": "and"
                    }
                }
            ],
            "filter": [
                {
                    "term": {
                        "has_affiliation": true
                    }
                }
            ]
        }
    }
}
```

[//]: # (Reference Links)
[Response]: <{{site.baseurl}}/response.html>
[Bool Query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html>
[Terms Query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-terms-query.html>
[Term query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html>
[Match query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html>
[Match phrase query]: <https://www.elastic.co/guide/en/elasticsearch/reference/6.2/query-dsl-match-query-phrase.html>
[Range query]: <https://www.elastic.co/guide/en/elasticsearch/reference/6.7/query-dsl-range-query.html>
