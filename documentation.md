---
layout: page
title: Reference
permalink: /api/
---

{:.table-contents}
- [Requests](#requests)
- [Query](#query)
- [Pagination](#pagination)
- [Sort](#sort)
- [Projection](#projection)
- [Filter](#filtering)
- [Fields](#fields)

### Requests
The request payload should comply with following `json` schema.

Fields | Description |  Required
------- | ------| -------
**[query](#query)** | Valid json search request | true
**[sort](#sort)** | Use available fields to sort results by ascending/descending order. | false
**[include](#projection)** | Only get specific fields from API response. By default all fields are selected. | false
**[exclude](#projection)** | Get all fields except undesired ones in search result. | false
**[size](#pagination)** | Integer value to specify number of items per page | false
**[from](#pagination)** | Integer value, defines the offset from the first result | false
**[scroll_id](#pagination)** | Pagination parameter | false (true for next requests)
**[scroll](#pagination)** | Lifespan of Scroll scroll context in minute (e.g. 1m) | false (true for scroll context)

### Query

Following queries are supported by current version of Lens APIs:

##### String Based Query
Query different terms with explicit operators `AND`/`OR`/`NOT` to create a compact query string.

>Example: Find works from institution published between two dates having some title.
>```json
>{"query": "(title:Dimensions AND authors.affiliations.institution:(Harvard University)) AND year_published:[2000 TO 2018]"}
>```

##### Term Query
[Term Query] operates in a single term and search for *exact term* in the field provided.
>Example:
>```json
>{
>    "query": {
>        "term": {
>            "publication_type": "journal article"
>        }
>    }
>}
>```

##### Match query
[Match query] accepts text/numbers/dates. The main use case of the match query is full-text search.
It matches each words separately. If you need to search whole phrase use [match phrase](#match-phrase-query) query.
> Example:
>```json
>{
>  "query": {
>      	"match":{
>      		"authors.affiliations.name": "Harvard University"
>      	}
>   }
>}
>```

##### Match Phrase query
[Match phrase query] accepts text/numbers/dates. The main use case for the match query is for full-text search.

>Example:
>```json
>{
>  "query": {
>      	"match_phrase":{
>      		"authors.affiliations.name": "Harvard University"
>      	}
>   }
>}
>```

##### Range query
[Range query] query to match records within the provided range.
> Example: Get record for year published between years 1980 and 2000
>```json
>{
>  "query": {
>      	"range": {
>            "year_published": {
>                "gte": "1980",
>                "lte": "2000"
>            }
>        }
>   }
>}
>```

##### Boolean query
[Bool Query] allows to combine multiple queries to create complex query providing precise result.
> Example: Get `journal article` scholarly works of Author with last name Kondratyev having patent citations.
>```json
> {
>	"query": {
>		"bool": {
>			"must": {
>				"match": {
>					"has_patent_citations": true
>				}
>			},
>			"should": [{
>					"match": {
>						"publication_type": "journal article"
>					}
>				},
>				{
>					"match": {
>						"authors.last_name": "Kondratyev"
>					}
>				}
>			]
>		}
>	}
>}
>```

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

You can specify records per page using `size` (default 1000) and context alive time `scroll` (default 1m). You will receive a `scroll_id` in response,  
which should be passed via request body to access next set of results. Since the `scroll_id` tends to change every time after each successful requests,
please use most recent scroll_id to access next page. This is not suited for real time user requests.

```json
{
    "scroll_id": "MjAxOTEw;DnF1ZXJ...R2NZdw==",
    "scroll": "1m"
}
```
> Note: The lifespan of scroll_id is limited to 1 minute for the current API version. Using expired scroll_id will result bad request HTTP response.
> Parameter `size` will be used for first scroll query and will remain the same for whole scroll context. Hence, using size in each scroll request will not have any effect.

### Sort
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
You can control the output fields in the API result using projection. There are two possible ways to do that.
1. **include**: Only request specific fields from the API endpoint
2. **exclude**: Fields to be excluded from result
> Note: Both *include* and *exclude* cannot be used in same request.

```json
 {"include":["title","patent_citations","authors.affiliations.name"]}
```
```json
 {"exclude":["external_ids","references"]}
```

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

> Example:
>```json
>{
>  "query": {
>     "match":{
>     	  "has_patent_citations": true
>     }
>  }
>}
>```

### Fields

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
 **patent_citations** | Array of [Patent Citation](#patent-citation) | Referenced by patents |  |
 **patent_citation_count** | Integer | Number of patent citations | true | `10`
 **lens_id** | String | Unique lens identifier | true | `100-004-910-081-14X`
 **created** | Date | Record created date | false | `2016-08-01T00:00:00+00:00`
 **publication_type** | String | Publication Type | true | `report`, `Conference Proceedings`
 **publication_supplementary_type** | Array of String | Supplementary publication type | true | `review`
 **authors** | Array of [Author](#author) | Authors| |
 **title** | String | Title of the scholarly work | true | `Malaria`
 **external_ids** | Array of [Id](#id) | The external identifier(s) for a scholarly work (DOI, PubMed ID, PubMed Central ID, Microsoft Academic ID or CORE) | |
 **start_page** | String | Start page | false | `893`
 **end_page** | String | End page | false | `916`
 **volume** | String | Volume | false | `32`
 **issue** | String | Issue | false | `4`
 **languages** | Array of String | Languages | true | `["ENG"]`
 **references** | List of [Reference](#reference) | References |  |
 **scholarly_citations** | List of Lens Ids | Scholarly Citations | true  | `["091-720-300-990-437"]`
 **chemicals** | List of [Chemical](#chemical) | Chemicals |  |
 **clinical_trials** | List of [Clinical Trial](#clinical-trial) | Scholarly Citations |  |
 **fields_of_study** | List of String |Fields Of Study | true | `["Immunology", "Malaria"]`
 **source_urls** | List of [Source URL](#source-url) | Source Urls | false |
 **abstract** | String | Scholarly work abstract text | true |
 **full_text** | String | Full Text | true |
 **date_published** | Date | Date of publication | true | `2009-05-22`
 **year_published** | Integer | Year of publication | true | `1986`
 **conference** | [Conference](#conference) | The conference instance or edition | |
 **author_count** | Integer | Number of Authors | true | `4`
 **reference_count** | Integer | The number of works in the reference list of a scholarly work | true | `2`
 **scholarly_citation_count** | Integer | The number of scholarly works that cite this scholarly work | true | `3`
 **open_access** | [Open Access](#open-access) | |
 **source** | [Source](#source) | Source publication in which the scholarly work appears |
 **keywords** | Array of String | Keywords | true
 **mesh_terms** | Array of [MeSH Term](#mesh-term) | MeSH term |
 **funding** | Array of [Funding](#funding) |  Funding |

##### Patent Citation

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
lens_id | String | Unique lens identifier | true | `141-171-521-309-804`

##### Author

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
collective_name | String | Author Collective Name | true
first_name | String | The author's first name | true | `Alexander`
last_name | String | The author's last name | true | `Kupco`
initials | Integer | Author Initials | true | `A`
full_name | String | Author's full name | true | `Alexander Kupco`
affiliations | Array of [Affiliation](#affiliation) | The institution/affiliations associated with Author.

##### Affiliation

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
institution | String | The institution associated with the author affiliations. | true | `Stony Brook University`
name | String | The author's affiliated institution and address | true | `Stony Brook Medicine, Stony Brook, New York 11794, United States`
grid | Array of [Grid](#grid) | Affiliation Grid | true |

##### Grid

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
id | String | Affiliation grid id | true | `grid.9018.0`
country_code | String | Country Code | true | `DE`

##### Reference

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
lens_id | String | Unique lens identifier | true | `071-957-228-698-625`

##### Open Access

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
**license** |  String | The Open Access license type | true | `cc-by`
**colour** |  String | The Open Access colour category | true | `gold`

##### Source

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
**title** |  String | The name of source publication in which the scholarly work appears | true | `Journal name, Book title, Confernce proceedings`
**type** |  String | Source Type | true | `Journal`
**publisher** |  String | The publisher of the source publication | true | `W.B. Saunders Ltd`
**issn** |  Array of [Id](#id) | The International Standard Serial Number of the source publication, without hyphenation | true | `00222836`
**country** |  String | The publisher's country | true | `United Kingdom`
**asjc_codes** |  String | The All Science Journal Classification (ASJC) code | true | `2735`
**asjc_subjects** |  String | Subject is derived from journals descriptions in Crossref metadata based on the Science Journal Classification Codes | true | `Pediatrics`

##### Mesh Term

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
mesh_id | String | MeSH term unique identifier. MeSH terms are the National Library of Medicine’s controlled vocabulary or subject heading list. | true | `D000293`
mesh_heading | String | MeSH terms are the National Library of Medicine’s controlled vocabulary or medical subject headings assigned to PubMed entries. NB MeSH Headings are case sensitive. | true | `Adolescent`
qualifier_id | String | Mesh Term Qualifier ID | true | `Q000032`
qualifier_name | String | Mesh Term Qualifier Name | true | `analysis`

##### Funding

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
org | String | Name of the funding organisation | true | `NIDCR NIH HHS`
funding_id | String | The funding organisation's project identifier | true | `U01 DE018902`
country | String | The country of the funding body | true | `United States`

##### Conference

Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
**name** | String | Conference Name | true | `International Electron Devices Meeting`
**instance** | String | Conference Instance Name | true | `CHI 1985`
**location** | String | The location of the conference | true | `Lihue, Kauai, HA, USA`

##### Chemical

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
mesh_id | String | MeSH term id | true | `D000293`
registry_number | String | Chemical registration number | true | `5Q7ZVV76EI`
substance_name | String | Substance name | true | `Antimalarials`

##### Clinical Trial

 Field | Type |  Description  | Searchable | Example
 ------- |:------:| -------|:-----:|---------
id | String | Identifier | true | `nct00105716`
registry | String | Clinical Trial Registry | true | `10.18810/clinical-trials-gov`

##### Source URL

Field | Type |  Description  | Searchable | Example
 ------- |:------:| -------|:-----:|---------
type | String | Source URL Type | false | `html`
url | String | URL String |  false |  `http://cds.cern.ch/record/2291692`

##### ID

 Field | Type |  Description  | Searchable | Example
------- |:------:| -------|:-----:|---------
type | String | The type/s of external identifiers for the scholarly work | true | `doi`, `pmid`, `magid`
value | String | The external identifier(s) for a scholarly work | true | `10.1016/s0031-3955(16)34861-1`


[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
[Bool Query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html>
[Term query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html>
[Match query]: <https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html>
[Match phrase query]: <https://www.elastic.co/guide/en/elasticsearch/reference/6.2/query-dsl-match-query-phrase.html>
[Range query]: <https://www.elastic.co/guide/en/elasticsearch/reference/6.7/query-dsl-range-query.html>
