
### Lens Aggregation API
Aggregation request follows similar structure as [elasticSearch aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html).

Following aggregation endpoints are supported:
- `POST` `/patent/aggregate`
- `POST` `/scholarly/aggregate`

Fields | Description                                                                   |  Required
------- |-------------------------------------------------------------------------------| -------
**query** | Valid json search query                                                       | true
**[aggregations](#aggregation-request)**  | Aggregation request                                                           | true
**include** | Only select specific fields from response. | false
**exclude** | Exclude the fields from search result.                                        | false
**[size](#pagination)** | Integer value to specify number of items per page                             | false

#### Aggregation Request
- `field` : Field from table below for each aggregation types
- `aggregations` : Sub-aggregations that can be aggregated per date range buckets

> Note: Some aggregations supports additional request configuration fields too. e.g. `interval` for `date_histogram` aggregation

The request structure should be valid json schema as illustrated below:

```json
{
  "aggregations": {
    "{user defined name of aggregation}": {
      "{aggregation type from below}": {
        "field": "{supported field for this aggregation from table below}",
        "aggregations": {
          //sub-aggregation if allowed
        }
      }
    }
  }
}
```

### Aggregation Types
- **Single value metrics aggregation**: computes the metrics based on value aggregated. e.g. `cardinality`, `avg`, `max`, `min`, `sum`  
- **Bucket aggregation**: These aggregation do not compute metrics. They group the values if it falls into specific bucket and also returns the number of documents for each bucket. e.g. `terms`, `date_histogram`. Bucket aggregation supports `sub-aggregations` which are aggregated for the buckets created by parent aggregation.

##### cardinality

Calculates approximate count of distinct values.

Product | supported Fields
------- |-------------
**Scholarly** | `affiliation.type`, `affiliation_count`, `author.affiliation.address.city`, `author.affiliation.address.country_code`, `author.affiliation.grid.address.state_code`, `author.affiliation.grid_id`, `author.affiliation.name.exact`, `author.display_name.exact`, `author.display_name_id`, `author.display_name_orcid`, `author_count`, `author_first.display_name.exact`, `author_first.display_name_id`, `author_last.display_name.exact`, `author_last.display_name_id`, `chemical.substance_name.exact`, `citation_id_type`, `conference.name.exact`, `field_of_study`, `funding.organisation.exact`, `keyword`, `mesh_term.mesh_heading`, `open_access.colour`, `open_access.license`, `open_access.source`, `publication_type`, `reference.lens_id`, `referenced_by`, `referenced_by_count`, `referenced_by_patent.lens_id`, `referenced_by_patent_count`, `source.asjc_code`, `source.asjc_subject.exact`, `source.country`, `source.publisher.exact`, `source.title.exact`, `source.type`, `year_published`
**Patent** | `agent.country`, `agent.name.exact`, `agent_count`, `applicant.name.exact`, `applicant.residence`, `applicant_count`, `cited_by.patent.lens_id`, `cited_by.patent_count`, `class_cpc.symbol`, `class_ipcr.symbol`, `class_national.symbol`, `family.extended.id`, `family.extended.member.lens_id`, `family.extended.size`, `family.simple.id`, `family.simple.member.lens_id`, `family.simple.size`, `inventor.name.exact`, `inventor.residence`, `inventor_count`, `jurisdiction`, `kind`, `legal_status.patent_status`, `owner_all.country`, `owner_all.name.exact`, `owner_all_count`, `publication_type`, `reference_cited.npl.record_lens_id`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent.lens_id`, `reference_cited.patent_count`, `sequence.count`, `sequence.organism.name.exact`

##### avg

Computes the average of numeric values extracted from the aggregated documents

Product | supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

##### max

Computes the maximum of numeric values extracted from the aggregated documents

Product | supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

##### min

Computes the minimum of numeric values extracted from the aggregated documents

Product | supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

##### sum

Computes the sum of numeric values extracted from the aggregated documents
 
Product | supported Fields
------- |-------------
**Scholarly** | `affiliation_count`, `author_count`, `reference_count`, `referenced_by_count`, `referenced_by_patent_count`, `year_published`
**Patent** | `agent_count`, `applicant_count`, `cited_by.patent_count`, `family.extended.size`, `family.simple.size`, `inventor_count`, `owner_all_count`, `reference_cited.npl_count`, `reference_cited.npl_resolved_count`, `reference_cited.patent_count`, `sequence.count`

##### date_histogram

This aggregation can be applied to date values extracted from documents. It allows the user to specify the interval and the values are rounded down to the closest date range bucket.

Additional request config fields:
- `interval` : supported for `date_histogram` with possible values: `QUARTER`, `YEAR`(default)

Product | supported Fields
------- |-------------
**Scholarly** | `date_published_sort`
**Patent** | `application_reference.date`, `date_published`, `earliest_priority_claim_date`, `legal_status.anticipated_term_date`, `legal_status.grant_date`

##### terms

It is also bucket aggregation where the buckets are dynamically built based on unique value of the field.

Additional request config fields:
- `size`: Number of (default to `10` upto `100`)
- `order`: List of sort order, default to descending document count. Following field can be used:
  - `_key`: sort by terms value themselves  
  - `_count`: sort by document count
  - sub-aggregation - sort by user defined sub aggregation name

  e.g. `"order": { "_key": "asc" }`

Product | supported Fields
------- |-------------
**Scholarly** | `affiliation.type`, `author.affiliation.address.city`, `author.affiliation.address.country_code`, `author.affiliation.address.state_code`, `author.affiliation.name.exact`, `author.display_name.exact`, `author.display_name_id`, `author.display_name_orcid`, `author_first.display_name.exact`, `author_first.display_name_id`, `author_last.display_name.exact`, `author_last.display_name_id`, `citation_id_type`, `conference.name.exact`, `field_of_study`, `funding.country.exact`, `funding.funding_name.exact`, `funding.organisation.exact`, `has_abstract`, `has_affiliation`, `has_affiliation_ror`, `has_clinical_trial`, `has_field_of_study`, `has_full_text`, `has_funding`, `has_keyword`, `has_mesh_term`, `has_orcid`, `in_analytics_set`, `is_open_access`, `is_referenced_by_patent`, `is_referenced_by_scholarly`, `mesh_term.mesh_heading`, `open_access.colour`, `open_access.license`, `open_access.source`, `publication_type`, `source.asjc_code`, `source.asjc_subject.exact`, `source.country`, `source.is_diamond`, `source.publisher.exact`, `source.title.exact`, `source.type`
**Patent** | `agent.country`, `agent.name.exact`, `applicant.name.exact`, `applicant.residence`, `assistant_examiner.name.exact`, `cited_by_patent`, `cites_npl`, `cites_patent`, `cites_resolved_npl`, `class_cpc.symbol`, `class_ipcr.symbol`, `class_national.symbol`, `examiner.name.exact`, `has_abstract`, `has_applicant`, `has_claim`, `has_description`, `has_docdb`, `has_examiner`, `has_full_text`, `has_inpadoc`, `has_inventor`, `has_owner`, `has_sequence`, `has_title`, `inventor.name.exact`, `inventor.residence`, `jurisdiction`, `kind`, `legal_status.granted`, `legal_status.has_disclaimer`, `legal_status.has_entry_into_national_phase`, `legal_status.has_grant_event`, `legal_status.has_spc`, `legal_status.patent_status`, `owner_all.country`, `owner_all.name.exact`, `primary_examiner.name.exact`, `publication_type`, `sequence.organism.name.exact`
