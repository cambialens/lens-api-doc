---
layout: page
title: Request
permalink: /request.html
---

The request fields are used in queries and sort operations.

{:.table-contents}
- [Request Structure](#request-structure)
- [Searchable Fields](#searchable-fields)
- [Filters](#filtering)
- [Pagination](#pagination)
- [Sorting](#sorting)
- [Projection](#projection)
- [Supported Query Types](#supported-query-types)

### Request Structure
The request payload should comply with following `json` schema.

Fields | Description |  Required
------- | ------| -------
**[query](#supported-query-types)** | Valid json search request | true
**[sort](#sorting)** | Use available fields to sort results by ascending/descending order. | false
**[include](#projection)** | Only get specific fields from API response. By default all fields are selected. | false
**[exclude](#projection)** | Get all fields except undesired ones in search result. | false
**[size](#pagination)** | Integer value to specify number of items per page | false
**[from](#pagination)** | Integer value, defines the offset from the first result | false
**[scroll_id](#pagination)** | Pagination parameter | false (true for next requests)
**[scroll](#pagination)** | Lifespan of Scroll scroll context in minute (e.g. 1m) | false (true for scroll context)

### Searchable Fields
For searching, following fields are supported by the system

Field | Type | Case Sensitive | Description
-------- | --------- | -------
**lens_id** | String | true | Unique lens identifier e.g. `100-004-910-081-14X`
**patent_citation.lens_id** | String | true | ID of Referenced by patents
**patent_citation_count** | Integer | false | Number of patent citations
**doi** | String | true | DOI Identifier
**pmid** | String | true | PubMed ID Identifier
**pmcid** | String | true | PubMed Central ID Identifier
**magid** | String | true | Microsoft Academic ID
**coreid** | String | true | DOI Identifier
**created** | Date | false | Record created date e.g. `2016-08-01T00:00:00+00:00`
**publication_type** | String | false | Publication Type e.g. `Conference Proceedings`
**publication_supplementary_type** | String | false | Supplementary publication type e.g. `review`
**author.collective_name** | String |  true | Author Collective Name
**author.first_name** | String | true| The author's first name e.g. `Alexander`
**author.last_name** | String | true | The author's last name e.g. `Kupco`
**author.initials** | String | true | Author Initials e.g. `A`
**author.display_name** | String | true | Author's full name e.g. `Alexander Kupco`
**author.affiliation.name** | String | true | The institution associated with the author affiliations. e.g. `Stony Brook University`
**author.affiliation.grid_id** | String | true | Affiliation grid id e.g. `grid.9018.0`
**author.affiliation.country_code** | String | true | Country Code e.g. `DE`
**title** | String | true | Title of the scholarly work e.g. `Malaria`
**start_page** | String | false | Start page e.g. `893`
**end_page** | String | false | End page  e.g. `916`
**volume** | String | false | Volume  `32`
**issue** | String | false | Issue `4`
**language** | String | true | Languages e.g. `["ENG"]`
**chemical.mesh_id** | String | true | MeSH term id e.g. `D000293`
**chemical.registry_number** | String | true | Chemical registration number e.g. `5Q7ZVV76EI`
**chemical.substance_name** | String | true | Substance name e.g. `Antimalarials`
**clinical_trial.id** | String | true | Clinical trial Identifier e.g. `nct00105716`
**clinical_trial.registry** | String | true | Clinical Trial Registry e.g. `10.18810/clinical-trials-gov`
**field_of_study** | String | true | Fields Of Study e.g. `Immunology`, `Malaria`
**abstract** | String | true | Scholarly work abstract text
**full_text** | String | false | Full Text
**date_published** | Date | false | Date of publication e.g. `2009-05-22`
**year_published** | Integer | false | Year of publication e.g. `1986`
**conference.name** | String | true | Conference Name e.g. `International Electron Devices Meeting`
**conference.instance** | String | true | Conference Instance Name e.g. `CHI 1985`
**conference.location** | String | true | The location of the conference e.g. `Lihue, Kauai, HA, USA`
**author_count** | Integer | false | Number of Authors
**reference_count** | Integer | false | The number of works in the reference list of a scholarly work
**scholarly_citation_count** | Integer | false | The number of scholarly works that cite this scholarly work
**open_access.license** |  String | true | The Open Access license type e.g. `cc-by`
**open_access.colour** |  String | true | The Open Access colour category e.g. `gold`
**source.title** | String | false | The name of source publication in which the scholarly work appears e.g. `Journal name, Book title, Confernce proceedings`
**source.type** | String | false | Source Type e.g. `Journal`
**source.publisher** | String | true | The publisher of the source publication `W.B. Saunders Ltd`
**source.issn** | String | true | The International Standard Serial Number of the source publication, without hyphenation e.g. `00222836`
**source.country** |  String | true | The publisher's country e.g. `United Kingdom`
**source.asjc_codes** |  String | false | The All Science Journal Classification (ASJC) code e.g. `2735`
**source.asjc_subjects** |  String | false | Subject is derived from journals descriptions in Crossref metadata based on the Science Journal Classification Codes e.g. `Pediatrics`
**keyword** | String | false | Search Keywords
**mesh_term.mesh_id** | String | true | MeSH term unique identifier. MeSH terms are the National Library of Medicine’s controlled vocabulary or subject heading list. e.g. `D000293`
**mesh_term.mesh_heading** | String | true | MeSH terms are the National Library of Medicine’s controlled vocabulary or medical subject headings assigned to PubMed entries. e.g. `Adolescent`
**mesh_term.qualifier_id** | String | true | Mesh Term Qualifier ID e.g. `Q000032`
**mesh_term.qualifier_name** | String | true | Mesh Term Qualifier Name e.g. `analysis`
**funding.organisation** | String | true | Name of the funding organisation e.g. `NIDCR NIH HHS`
**funding.funding_id** | String | true | The funding organisation's project identifier e.g.`U01 DE018902`
**funding.country** | String | true | The country of the funding body e.g. `United States`

### Filtering
You can use following pre-defined filters to refine search results:

Field | Description |  Possible Value
------- | ------| -------
has_patent_citations | Indicates if the scholarly work has been cited by a patent document. | `true`/`false`
has_affiliation | Has affiliation | `true`/`false`
has_affiliation_grid | Has affiliation grid | `true`/`false`
has_mesh_term | Has MeSH term | `true`/`false`
has_chemical | Indicates if the scholarly work has an associated chemical substance  | `true`/`false`
has_keyword | Indicates if the scholarly work has keyword | `true`/`false`
has_clinical_trial | Indicates if the scholarly work has clinical trial | `true`/`false`
has_field_of_study | Flags if the scholarly work has a Field of Study | `true`/`false`
has_abstract | Indicates if the scholarly work has abstract | `true`/`false`
has_fulltext | Indicates if the scholarly work has fulltext | `true`/`false`
has_funding | Indicates if the scholarly work has funding information | `true`/`false`
is_open_access | Flags if the scholarly work has is Open Access | `true`/`false`

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

**Offset/Size Based Pagination:**

Use parameter `from` to define the offset and `size` to specify number of records expected.
```json
{
	"query": "Malaria",
	"from": 100,
	"size":50
}
```
**Cursor Based Pagination:**

You can specify records per page using `size` (default 20 and max 1000) and context alive time `scroll` (default 1 minute). You will receive a `scroll_id` in response, which should be passed via request body to access next set of results. Since the `scroll_id` tends to change every time after each successful requests, please use the most recent `scroll_id` to access next page. This is not suited for real time user requests.

```json
{
    "scroll_id": "MjAxOTEw;DnF1ZXJ...R2NZdw==",
    "scroll": "1m"
}
```
> Note: The lifespan of scroll_id is limited to 1 minute for the current API version. Using expired scroll_id will result bad request HTTP response.
> Parameter `size` will be used for first scroll query and will remain the same for whole scroll context. Hence, using size in each scroll request will not have any effect.

### Sorting
Result can be retrieved in ascending or descending order. Use the following formats and [fields](#fields) to apply sorting to the API response.
```json
{
  "sort": [
      {"patent_citation_count":"asc"},
      {"year_published": "desc"}
  ]
}
```

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
> Note: Both *include* and *exclude* cannot be used in same request.

### Supported Query Types

Following queries are supported by current version of Lens API:

##### String Based Query
Query different terms with explicit operators `AND`/`OR`/`NOT` to create a compact query string.
>Example: Find works from institution published between two dates having some title.
```json
{"query": "(title:Dimensions AND author.affiliation.institution:(Harvard University)) AND year_published:[2000 TO 2018]"}
```

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
[Bool Query] allows to combine multiple queries to create complex query providing precise result.
> Example: Get `journal article` scholarly works of Author with last name Kondratyev having patent citations.
```json
 {
	"query": {
		"bool": {
			"must": {
				"match": {
					"has_patent_citations": true
				}
			},
			"should": [{
					"match": {
						"publication_type": "journal article"
					}
				},
				{
					"match": {
						"author.last_name": "Kondratyev"
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
[Term query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html>
[Match query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html>
[Match phrase query]: <https://www.elastic.co/guide/en/elasticsearch/reference/6.2/query-dsl-match-query-phrase.html>
[Range query]: <https://www.elastic.co/guide/en/elasticsearch/reference/6.7/query-dsl-range-query.html>
