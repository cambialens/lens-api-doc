---
layout: page
title: Support
permalink: /support.html
---

- To report any bugs, issues and usability of APIs you can [create an issue].
- If you have any issues or concerns regarding your access plan, please email [subscriptions@lens.org](mailto:subscriptions@lens.org).
- For general questions or to provide feedback, please use the [Lens Feedback] form.

### Tips for creating issues:
- Please provide the API request and response if possible.
- Please provide your intention of creating the query request.

## Changelog

API Version | Schema Versions | Date Released | Notes
------- | ------| ------| -------
`2.19.0` | - Scholar: `1.6.8` <br/> - Patent: `1.6.4` | Dec 27, 2025 | - Added `funding.org_id` and `funding.funding_name` to the scholarly works response fields.
`2.19.0` | - Scholar: `1.6.7` <br/> - Patent: `1.6.4` | Dec 21, 2025 | - Added `biblio.application_number` to the patent response fields. <br/> - Added `application_number`to the supported patent request fields.
`2.16.2` | - Scholar: `1.6.7` <br/> - Patent: `1.6.3` | May 22, 2025 | - Added `x-rate-limit-retry-after-millis` to the response headers. <br/> - Added support for `multi_match` queries.
`2.16.0` | - Scholar: `1.6.7` <br/> - Patent: `1.6.3` | Mar 03, 2025 | - Added `retraction_update` object and fields to the scholar response fields. <br/> - Added `date_published_sort` to the supported scholar request fields. <br/> - Added support for <a href="https://docs.api.lens.org/aggregations.html#histogram">histogram aggregations</a> to the aggregation endpoint with support for a select number of integer fields. <br/> - Added a `ui_default` field for <a href="https://docs.api.lens.org/request-scholar.html#query-string-based-query">Query String Based Queries</a> in the scholar API. <br/> - Added support for Expand by Family to the patent API.
`2.13.0` | - Scholar: `1.6.6` <br/> - Patent: `1.6.2` | Sep 25, 2024 | - Added `biblio.parties.inventors.orcid` to the patent response fields. <br/> - Added `invetor.orcid`, `reference_cited.npl.category` and `reference_cited.npl.cited_phase` to the supported patent request fields. <br/> - Added `references_count`, `references_resolved_count` and `references.text` to the scholar response fields. <br/> - Added `retraction_update.date`, `retraction_update.nature` and `retraction_update.reason` to the scholar request fields. <br/> - Updated the API data schema endpoints.
`2.12.0` | - Scholar: `1.6.5` <br/> - Patent: `1.6.1` | Jul 08, 2024 | - Added support for `MONTH` interval in the date histogram aggregation. <br/> - Added `legal_status.term_extension_days` to the supported patent request fields.
`2.11.0` | - Scholar: `1.6.5` <br/> - Patent: `1.6.0` | Oct 25, 2023 | - Released the Aggregation API out of beta. <br/> - Added Aggregation API endpoints to Swagger UI. <br/>
`2.10.0` | - Scholar: `1.6.5` <br/> - Patent: `1.6.0` | Aug 2, 2023 | - Added and improved API error and validation messages. <br/> - Increased the size of result sets that are supported by offset/size based pagination to 10,000 results. <br/> - Released the beta Aggregation API.
`2.9.0` | - Scholar: `1.6.5` <br/> - Patent: `1.6.0` | May 17, 2023 | - Added `authors.affiliations.name_original` to the scholar API. <br/> - Added  support for `min_score` in the request body. <br/> - Added `max_score` to the API response.
`2.8.0` | - Scholar: `1.6.4` <br/> - Patent: `1.6.0` | Feb 20, 2023 | - Added `group_by` to the patent API to support group by patent family queries.  
`2.5.3` | - Scholar: `1.6.3` <br/> - Patent: `1.4.0` | Sep 12, 2022 | - Added scholarly request fields: `has_affiliation_ror` <br/> - Added query parser to normalise string based queries.
`2.5.0` | - Scholar: `1.6.2` <br/> - Patent: `1.4.0` | Jun 9, 2022 | - Added scholarly request fields: `ids.doi`, `ids.pmid`, `ids.pmcid`, `ids.magid`, `ids.coreid` and `ids.openalex`  <br/> - Added data schema endpoints.
`2.4.0` | - Scholar: `1.6.1` <br/> - Patent: `1.3.1` | Feb 15, 2022 | - Added scholarly request fields: `author.affiliation.ror_id`, `author.affiliation.name_original`, `source.is_diamond`, `author.affiliation.address.city`, `author.affiliation.address.state_code`, `author.affiliation.address.country_code`, `author.affiliation.type`, `has_affiliation_ror`  <br/> - Added scholarly response field: `authors.affiliations.ids` <br/> - Added `maxResultPerPage` subscription plan parameter to the API usage endpoints
`2.2.2` | - Scholar: `1.5.2` <br/> - Patent: `1.2.7` | Jun 29, 2021 | - Added Patent response fields `biblio.parties.examiners` <br/> - Added patent request fields `has_examiner` - Added `language` support in request <br/> - Added scholarly search fields `reference.lens_id`, `in_analytics_set`
`2.1.1` | - Scholar: `1.5.0` <br/> - Patent: `1.2.5` | May 19, 2021 | - Added Patent response fields `biblio.references_cited.citations.cited_phase`, `biblio.references_cited.patent_count` <br/> - Added patent request fields `earliest_priority_claim_date`, `sequence.organism.tax_id`, `sequence.organism.name`, `sequence.organism.name.exact` <br/> - Added scholarly fields `source.issn.type`, `date_published_parts`
`2.1.0` | - Scholar: `1.5.0` <br/> - Patent: `1.1.0` | February 22, 2021 | - Added Scholarly GET endpoint for retrieving scholarly works by `Lens_id`<br/> - Added `has_inpadoc`, `created` and `earliest_priority_date` to the Patent request fields <br/> - Expanded the coverage of the default search field for string based queries <br/> - Performance improvements for Scholarly endpoints |
`2.0.0` | - Scholar: `1.4.0` <br/> - Patent: `1.0.0` | December 16, 2020 | - Added Patent API endpoints <br/> - Added support for `un-stemmed` search |
`1.3.2` | Scholar: `1.3.2` | March 25, 2020 | - Added keyword fields `author.affiliation.name.exact`, `source.title.exact`, `funding.organisation.exact` for search request |
`1.3.0` | Scholar: `1.3.0`| March 5, 2020 | - Added `GET` endpoints for Scholarly Search and Collections <br/> - Added author identifier fields (MAG, ORCID) <br/> - See [Lens Release 6.7](https://about.lens.org/news/release-6-7/) notes for details|
`1.2.0` | Scholar: `1.2.0`| September 9, 2019 | - Added Lens partner option <br/> - Bug fixes <br/> - Performance improvements <br/> - See [Lens Release 6.4](https://about.lens.org/news/release-6-4/) notes for details|
`1.1.0` |  Scholar: `1.1.0`| July 22, 2019 | - Added the ability to search within a scholarly collection (user feedback) <br/> - Bug fixes|
`1.0.0` |  Scholar: `1.0.0`| June 27, 2019 | - API to access the full corpus of Scholarly works |
`beta` |  Scholar: `beta`| April 29, 2019 ||

[create an issue]: <https://github.com/cambialens/lens-api-doc/issues>
[Lens Feedback]: <https://www.lens.org/lens/feedback?returnTo=https:/>
