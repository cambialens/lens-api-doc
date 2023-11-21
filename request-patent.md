---
layout: post-sidebar
title: Patent Request
permalink: /request-patent.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Request Structure
        url: request-patent.html#request-structure
      - page: Searchable Fields
        url: request-patent.html#searchable-fields
      - page: Filters
        url: request-patent.html#filtering
      - page: Pagination
        url: request-patent.html#pagination
      - page: Sorting
        url: request-patent.html#sorting
      - page: Projection
        url: request-patent.html#projection
      - page: Supported Query Types
        url: request-patent.html#supported-query-types
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
**[language](#language)** | For multi-lingual fulltext search | false (`EN` by default)
**[regex](#regex)** | For Query String based queries containing regular expressions | false (false by default)
**[group_by](#group-by-family)** | For group by patent family queries. Supports group by `SIMPLE_FAMILY` and `EXTENDED_FAMILY` | false
**[min_score](#minimum-score)** | For limiting the response to the most relevant results, e.g. `"min_score": 14` | false
{: .param-def }

### Searchable Fields
For searching, the following fields are supported by the API:

 Group |  Field  |  Type  |  Description
 --------  |  ---------  |  ------- |  -------
General | **lens_id** | String | Unique lens identifier. Every document in the Lens has a unique 15-digit identifier called a Lens ID. e.g. `186-488-232-022-055`
General | **created** | Date | Earliest create date of the patent meta record
General | **Ids** | Document Identifiers | Use this field to search for patent records using publication identifiers or Lens Ids. e.g. `"EP_0227762_B1_19900411", "EP 0227762 B1", "EP_0227762_B1", "EP0227762B1", "EP0227762", "145-564-229-856-440", "US 7,654,321 B2", "7,654,321", "US 2021/0191781 A1"`
General | **doc_number** | String | The document number assigned to a patent application on publication. e.g. `20130227762`
General | **docdb_id** | Integer | The DOCDB identifier for the patent document. e.g. `499168393`
General | **jurisdiction** | String | The jurisidiction of the patent document. e.g. `US`
General | **kind** | String | The patent document kind code (varies by jurisdiction). e.g. `A1`
General | **lang** | String | The original language of the patent document. e.g. `EN`
General | **date_published** | Date | Date of publication for the patent document. e.g. `2009-05-22`
General | **year_published** | Integer | The year of publication for the patent document. e.g. `2009`
General | **publication_type** | String | Type of patent document. e.g. `ABSTRACT`, `AMBIGUOUS`, `AMENDED_APPLICATION`, `AMENDED_PATENT`, `DESIGN_RIGHT`, `GRANTED_PATENT`, `LIMITED_PATENT`, `PATENT_APPLICATION`, `PATENT_OF_ADDITION`, `PLANT_PATENT`, `SEARCH_REPORT`, `SPC`, `STATUTORY_INVENTION_REGISTRATION`, `UNKNOWN`
General | **earliest_priority_claim_date** | Date | Earliest priority date. The earliest date of filing of a patent application, anywhere in the world, to protect an invention. The priority date may be earlier than the actual filing date of an application if an application claims priority to an earlier parent application, then its earliest priority date may be the same as the parent.
Application | **application_reference.jurisdiction** | String | The jurisdiction of the application. e.g. `US`
Application | **application_reference.date** | Date | The application filing date is the date when a patent application is first filed at a patent office. e.g. `2009-05-22`
Application | **application_reference.doc_number** | String | The document number of the application. e.g. `201715824814`
Application | **application_reference.kind** | String | The kind code of the application. e.g. `A1`
Priority | **priority_claim.jurisdiction** | String | The jurisdiction of the priority document. e.g. `DE`
Priority | **priority_claim.date** | Date | The publication date of the priority document. e.g. `2009-05-22`
Priority | **priority_claim.doc_number** | String | The document number of the priority document. e.g. `1117265`
Priority | **priority_claim.kind** | String | The kind code of the priority document. e.g. `A1`
Text Fields | **abstract** | String | Searches the patent document abstract text. e.g. `A processor implements conditional vector operations in which an input vector containing multiple operands to be used in conditional operations is divided into two or more output…`
Text Fields | **claim** | String | Searches the Claims recorded in the patent. e.g. `What is claimed is: 1. A method of performing a conditional vector output operation in a processor, the method comprising: receiving electrical signals representative of an input data vector…`
Text Fields | **description** | String | The description text of the patent document. e.g. `This invention was made in conjuction with U.S. Government support under U.S. Army Grant No. DABT63-96-C-0037.” BACKGROUND OF THE INVENTION 1. Field of the Invention The present invention is directed to…`
Text Fields | **title** | String | Title of the patent. e.g. `Fidget Spinner`
Families | **family.extended.member.document_id.jurisdiction** | String | The jurisdiction of the extended family member. e.g. `CN`
Families | **family.extended.member.document_id.date** | Date | The publication date of the extended family member. e.g. `2009-05-22`
Families | **family.extended.member.document_id.doc_number** | String | The document number of the extended family member. e.g. `1117265`
Families | **family.extended.member.document_id.kind** | String | The kind code of the extended family member. e.g. `B2`
Families | **family.extended.member.lens_id** | String | The Lens Id of the extended family member. e.g. `106-213-498-661-220`
Families | **family.extended.size** | Integer | The number of extended family member documents. e.g. `12`
Families | **family.simple.member.document_id.jurisdiction** | String | The jurisdiction of the simple family member. e.g. `EP`
Families | **family.simple.member.document_id.date** | Date | The publication date of the simple family member. e.g. `2009-05-22`
Families | **family.simple.member.document_id.doc_number** | String | The document number of the simple family member. e.g. `1117265`
Families | **family.simple.member.document_id.kind** | String | The kind code of the simple family member. e.g. `B2`
Families | **family.simple.member.lens_id** | String | The Lens Id of the simple family member. e.g. `106-213-498-661-220`
Families | **family.simple.size** | Integer | The number of simple family member documents. e.g. `5`
Applicants | **applicant.address** | String | The applicant address as recorded on the patent. e.g. `TORONTO, ONTARIA, CA`
Applicants | **applicant.name** | String | The patent applicant(s) name. e.g. `CPS Technology Holdings LLC`
Applicants | **applicant.name.exact** | String | The patent applicant(s) name. N.B. Use this field for exact name matches. e.g. `CPS TECHNOLOGY HOLDINGS LLC`
Applicants | **applicant.residence** | String | The country of the applicant (ISO 2-digit country code). e.g. `CA`
Applicants | **applicant_count** | Integer | The number of applicants. e.g. `2`
Inventors | **inventor.address** | String | The address of the inventor. e.g. `TORONTO, ONTARIA, CA`
Inventors | **inventor.name** | String | The patent inventor(s) name. e.g. `Engebretson Steven P`
Inventors | **inventor.name.exact** | String | The patent inventor(s) name. N.B. Use this field for exact name matches. e.g. `ENGEBRETSON STEVEN P`
Inventors | **inventor.residence** | String | The country of residence of the inventor (ISO 2-digit country code). e.g. `DE`
Inventors | **inventor_count** | Integer | The number of inventors. e.g. `3`
Owners | **owner_all.address** | String | The owner address as recorded on the patent or legal event. e.g. `TORONTO, ONTARIA, CA`
Owners | **owner_all.country** | String | The owner's country code (ISO 2-digit country code). e.g. `US`
Owners | **owner_all.execution_date** | Date | The date of execution of ownership / assignment. e.g. `2009-05-22`
Owners | **owner_all.name** | String | The patent owner(s) name. e.g. `CPS Technology Holdings LLC`
Owners | **owner_all.name.exact** | String | The patent owner(s) name. N.B. Use this field for exact name matches. e.g. `CPS Technology Holdings LLC`
Owners | **owner_all.recorded_date** | Date | The ownership / assignment event record date. e.g. `2009-05-22`
Owners | **owner_all_count** | Integer | The count of all owners of the patent. N.B. Includes current and former owners. e.g. `5`
Examiners | **examiner.name** | String | The patent examiner name. e.g. `Jack W Keith`
Examiners | **examiner.name.exact** | String | The patent examiner name. N.B. Use this field for exact name matches.
Examiners | **examiner.department** | String | The patent examiner department. e.g. `3646`
Examiners | **primary_examiner.name** | String | The primary patent examiner name. e.g. `Jack W Keith`
Examiners | **primary_examiner.name.exact** | String | The primary patent examiner name. N.B. Use this field for exact name matches.
Examiners | **primary_examiner.department** | String | The primary patent examiner department. e.g. `3646`
Examiners | **assistant_examiner.name** | String | The assistant patent examiner name. e.g. `Lily C Garner` 
Examiners | **assistant_examiner.name** | String | The assistant patent examiner name. N.B. Use this field for exact name matches. 
Citations | **cited_by.patent.document_id.jurisdiction** | String | The jurisdiction of the citing patent. e.g. `EP`
Citations | **cited_by.patent.document_id.doc_number** | String | The document number of the citing patent. e.g. `EP2020/063503`
Citations | **cited_by.patent.document_id.kind** | String | The kind code of the citing patent. e.g. `B2`
Citations | **cited_by.patent.lens_id** | String | The Lens Id of the citing patent. e.g. `008-840-176-449-446`
Citations | **cited_by.patent_count** | Integer | The count of citing patents (Cited by patent count). e.g. `10`
Citations | **reference_cited.npl.external_id** | String | The resolved external identifier(s) for cited non-patent literature (DOI, PubMed ID, PubMed Central ID or Microsoft Aacademic ID). e.g. `10.1038/nature03090`, `12345678919`
Citations | **reference_cited.npl.lens_id** | String | The Lens Id of the resolved non-patent literature citations (i.e. scholarly work Lens Id). e.g. `168-663-423-050-326`
Citations | **reference_cited.npl.text** | String | The original unresolved non-patent literature citation text. e.g. `Cormen et al., 'Introduction to Algorithms (MIT Electrical Engineering and Computer Science Series,' MIT Press, ISBN 0262031418, pp. 665-667, 695-697.`
Citations | **reference_cited.npl_count** | Integer | The number of original non-patent literature citations. e.g. `2`
Citations | **reference_cited.npl_resolved_count** | Integer | The number of resolved scholalry works cited by a patent. e.g. `12`
Citations | **reference_cited.patent.lens_id** | String | The Lens Id of the cited patent. e.g. `106-213-498-661-220`
Citations | **reference_cited.patent.document_id.jurisdiction** | String | The jurisdiction of the cited patent. e.g. `US`
Citations | **reference_cited.patent.document_id.date** | Date | The publication date of the cited patent. e.g. `2009-05-22`
Citations | **reference_cited.patent.document_id.doc_number** | String | The document number of the cited patent. e.g. `4590964`
Citations | **reference_cited.patent.document_id.kind** | String | The kind code of the cited patent. e.g. `A`
Citations | **reference_cited.patent_count** | Integer | Number of patents documents cited by a given patent. e.g. `21`
Legal Events | **legal_status.application_expiry_date** | Date | The expiry date of the patent application because of withdrawal or abandonment. e.g. `2009-05-22`
Legal Events | **legal_status.anticipated_term_date** | Date | The anticipated termination date for granted patents. The anticipated termination date is calculated based on the natural term date plus any extensions. e.g. `2009-05-22`
Legal Events | **legal_status.discontinuation_date** | Date | The discontinuation date of the patent due to "unnatural death" (i.e. lapse, withdrawn, abandoned). N.B. The patent can be revived within a certain time frame. e.g. `2009-05-22`
Legal Events | **legal_status.grant_date** | Date | The date the patent application was granted (i.e. the application first grant date). e.g. `2009-05-22`
Legal Events | **legal_status.granted** | Boolean | Indicates if the patent application has been granted in one or more jurisdictions. e.g. `TRUE`
Legal Events | **legal_status.has_disclaimer** | Boolean | Indicates if this US patent subjected to a terminal disclaimer. e.g. `TRUE`
Legal Events | **legal_status.has_grant_event** | Boolean | Indicates if the patent application/simple family has one or more Grant events in INPADOC. e.g. `TRUE`
Legal Events | **legal_status.has_entry_into_national_phase** | Boolean | Indicates if the patent application/simple family has entered the National Phase in INPADOC. e.g. `TRUE`
Legal Events | **legal_status.patent_status** | String | The calculated legal status of the patent application. e.g. `expired`, `inactive`, `active`, `patented`, `discontinued`, `withdrawn or rejected`, `pending`, `unknown`
Legal Events | **legal_status.has_spc** | Boolean | Indicates if the patent has a supplementary protection certificate. e.g. `TRUE`
Agents & Attorneys | **agent.address** | String | The agent/attorney address as recorded on the patent. e.g. `20 Red Lion Street, GB-London WC1R 4PJ(GB)`
Agents & Attorneys | **agent.country** | String | The country of the agent/attorney (ISO 2-digit country code). e.g. `GB`
Agents & Attorneys | **agent.name** | String | The agent/attorney name. e.g. `Chapman, Paul William et al.`
Agents & Attorneys | **agent.name.exact** | String | The patent agent/attorney name. N.B. Use this field for exact name matches. e.g. `Paul Chapman`
Agents & Attorneys | **agent_count** | Integer | The number of agents/attorneys listed on the patent. e.g. `1`
Classifications | **class_cpc.symbol** | String | CPC patent classification codes. e.g. `H01R11/01`
Classifications | **class_ipcr.symbol** | String | IPCR patent classification codes. e.g. `H01R13/115`
Classifications | **class_national.symbol** | String | US patent classification codes. e.g. `439/535`
Sequences | **sequence.count** | Integer | The number of biological sequences associated with a patent. e.g. `5`
Sequences | **sequence.data_source** | String | The data source of the disclosed sequence. `DDBJPAT`: DDBJ patent division, `EMBLPAT_EBI`: EMBL-EBI patent division, `USPTO_FULLTEXT_RB`: USPTO full-text, `EP_SEQL`: EPO, `GBPAT_NCBI`: GenBank patent division, `WIPO_SEQL`: WIPO, `GBPAT_EBI`, `CIPO_BSL`: CIPO, `GBPAT_DDBJ`, `USPTO_FULLTEXT_GB`, `USPTO_PSIPS`, `DE_MEGA`, `EP_MEGA`
Sequences | **sequence.document_location** | String | The patent document section of the disclosed sequence(s): `DDESC`: detailed description, `CLAIM`: claims, `BSUMM`: summary, `BDRAW`: drawings, `WDESC`: full-text
Sequences | **sequence.length_bucket** | String | Preset sequence length range (nucleotide: 0-100, 101-5000, 5001-100k, >100k; amino acids: 0-50, 51-300, >300). e.g. `NT_101-5000` or `AA_301`
Sequences | **sequence.organism.tax_id** | String | The NCBI taxonomic identifier of the organism which the biological sequence is from. e.g. `9616`
Sequences | **sequence.type** | String | The type of sequence e.g. `N` - nucleotide (including `DNA` and `RNA` sub-types), `P` - peptides/proteins
Sequences | **sequence.organism.name** | String | Organism name e.g. `Homo sapiens`
Sequences | **sequence.organism.name.exact** | String | Use this field for exact name matches e.g. `Homo sapiens`
Citations | **reference_cited.npl_resolved_count** | Integer | The number of resolved scholalry works cited by a patent. e.g. `12`
{: .param-def }

### Filtering
You can use the following pre-defined filters to refine your search results:

Field | Description |  Possible Value
------- | ------| -------
**cited_by_patent** | Indicates if a patent is cited by other patents. | `true`/`false`
**cites_npl** | Indicates if a patent has cited any non-patent literature in the references. | `true`/`false`
**cites_patent** | Indicates if a patent cites other patents. | `true`/`false`
**cites_resolved_npl** | Indicates if a patent document cites non-patent literature that have been resolved to a matching Lens Scholarly Work. | `true`/`false`
**has_abstract** | Indicates if the abstract is available for the patent document. | `true`/`false`
**has_agent** | Indicates if the patent record has agent/attorney information. | `true`/`false`
**has_applicant** | Indicates if the patent record has applicant information. | `true`/`false`
**has_claim** | Indicates if the claims are available for the patent document. | `true`/`false`
**has_description** | Indicates if the description is available for the patent document. | `true`/`false`
**has_full_text** | Indicates if the full text from the PTO is available for the patent document. | `true`/`false`
**has_owner** | Indicates if the patent record has owner information. | `true`/`false`
**has_examiner** | Indicates if the patent record has examiner information. | `true`/`false`
**has_inventor** | Indicates if the patent record has inevntor information. | `true`/`false`
**has_sequence** | Indicates if the patent record has sequence information. | `true`/`false`
**has_title** | Indicates if the title is available for the patent document. | `true`/`false`
**has_docdb** | Indicates if the DOCDB information is available for the patent document. | `true`/`false`
**has_inpadoc** | Indicates if the patent document has associated legal events in INPADOC. | `true`/`false` 
{: .param-def }

 Example:
```json
{
  "query": {
     "match":{
     	  "has_full_text": true
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
  "query": "nanotechnology",
  "from": 100,
  "size":50
}
```
Similarly for `GET` requests, the following parameters are applicable: `size=50&from=100`
> **Note**: 
> - Offset/size based paginations is suitable for small result sets only and does not work on result sets of more that **10,000** records. For larger volume data downloads, use Cursor Based Pagination.

##### Cursor Based Pagination
You can specify records per page using `size` (default 20 and max 100-500, refer to your API plan for your max records per request) and context alive time `scroll` (default 1 minute). You will receive a `scroll_id` in response, which should be passed via request body to access next set of results. Since the `scroll_id` tends to change every time after each successful requests, please use the most recent `scroll_id` to access next page. This is not suited for real time user requests.

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
> - If no further results found, the response will be `204` and scroll context gets invalidated. The subsequent response will be `400`, if same `scroll_id` is used again.

### Sorting
Result can be retrieved in ascending or descending order. Use the following format and [fields](#searchable-fields) to apply sorting to the API response. Results can also be sorted by relevance score using `relevance`.
```json
{
  "sort": [
      {"reference_cited.patent_count":"desc"},
      {"year_published": "asc"},
      {"relevance": "desc"}
  ]
}
```
For `GET` requests, the following structure is applicable: `sort=desc(reference_cited.patent_count),asc(date_published),desc(relevance)`

### Projection
You can control the output fields in the API [Response] using projection. There are two possible ways to do that.
1. **include**: Only request specific fields from the API endpoint
2. **exclude**: Fields to be excluded from result

```json
 {"include":["lens_id", "title","description","claim"]}
```
```json
 {"exclude":["legal_status","biblio.classifications_cpc"]}
```
For `GET` requests following structure is applicable.
`include=lens_id,title,description,claim`
> **Note**: Both *include* and *exclude* can be used in same request.


### Stemming
Stemming allows to reduce the words to root form. E.g. Constructed and constructing will be stemmed to root construct.
Since sometime the default stemming might not give you exact result, disabling it will just search for provided form of the word.
e.g. `"stemming": false`

### Language
Available search language codes: `AR`, `DE`, `EN`, `ES`, `FR`, `JA`, `KO`, `PT`, `RU`, `ZH`

### Regex
Regex allows the use of regular expressions in [Query String based query](#query-string-based-query), e.g. `"regex": true`
```json
{
    "query": "field_of_study:/.*[Ee]conom.*/",
    "regex": true
}
```

### Group by Family
Group by patent family queries supports group by `SIMPLE_FAMILY` and `EXTENDED_FAMILY`, e.g. `"group_by": "SIMPLE_FAMILY"`. This returns the top sorted patent document record for each family (sorted by relevance by default). 

>**Note**:
>  * Group by family does not work with `scroll` requests.


### Minimum Score
The minimum score represents the `relevance` score based on the query matching score used in Elasticsearch. This can be used to This can be used to limit the response to the most relevant results and can be used in 2-steps:

   1. Perform an initial API request to get the `max_score`. N.B. the size of the request needs to be greater than 0 to return the `max_score`.
   2. You can then filter by the `min_score` in subsequent requests.

For example, if the `max_score` is 14.9 and there are 236K results in total from the initial request, you can pass the `min_score` as 14 (i.e. less than max_score) in the subsequent request to limit the response to the most relevant results only.

>**Note**:
>  * The `max_score` will be returned as `0` if size is 0 or if a sort is applied.
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
            "publication_type": "GRANTED_PATENT"
        }
    }
}
```

##### Terms Query
[Terms Query] allows you to search multiple *exact terms* for a provided field. A useful scenario is while searching multiple identifiers.
> Example: Search for multiple document numbers
```json
{
	"query": {
		"terms": {
			"doc_number": ["20130227762", "1117265"]
		}
	}
}
```
> **Note**: 
> * Avoid using the [Term](#term-query) and [Terms](#terms-query) queries for text fields. To search text field values, we recommend using the [Match](#match-query) and [Match Phrase](#match-phrase-query) queries instead.

##### Match query
[Match query] accepts text/numbers/dates. The main use case of the match query is full-text search.
It matches each words separately. If you need to search whole phrase use [match phrase](#match-phrase-query) query.
> Example: Get patents filed by IBM
```json
{
  "query": {
      	"match":{
      		"applicant.name": "IBM"
      	}
   }
}
```

##### Match Phrase query
[Match phrase query] accepts text/numbers/dates. The main use case for the match query is for full-text search.
> Example: Get patents filed by IBM
```json
{
  "query": {
      	"match_phrase":{
      		"applicant.name": "IBM"
      	}
   }
}
```
> **Note**: Both **Match** and **Match Phrase** are used for text searching but the difference is how they do it. For example, searching for `"Cleveland, OH"` differs between Match and Match Phrase like this:
>* **Match**: standard search in which each word is matched separately (for example: `Cleveland` OR `OH`)
>* **Match Phrase**: matches the exact phrase provided. In this case it will match the exact text `Cleveland, OH`


##### Range query
[Range query] query to match records within the provided range.
> Example: Get patents published between years 1980 and 2000
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
> Example: Search for granted patents from inventors named "Engebretson" that have been cited by other patents.
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "cited_by_patent": "true"
                    }
                },
                {
                    "match": {
                        "publication_type": "GRANTED_PATENT"
                    }
                },
                {
                    "match": {
                        "inventor.name": "Engebretson"
                    }
                }
            ]
        }
    }
}
```

##### Query String Based Query
Query different terms with explicit operators `AND`/`OR`/`NOT` to create a compact query string.
>Example: Find patents with javascript in the title that have been filed by IBM and published between 2000 and 2018.
```json
{"query": "(title:javascript AND applicant.name:(IBM)) AND year_published:[2000 TO 2018]"}
```

If you need to use any [reserved special characters](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#_reserved_characters), you should escape them with leading backslash.
>Example: Searching by CPC code using string based query
```json
{"query": "class_cpc.symbol:Y02E10\\/70"}
```
You can use json based format for string based query and mixed with complex boolean queries like this:

```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "query_string": {
                        "query": "crispr-cas9",
                        "fields": [
                            "title",
                            "claims",
                            "description"
                        ],
                        "default_operator": "or"
                    }
                }
            ],
            "filter": [
                {
                    "term": {
                        "has_owner": true
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
