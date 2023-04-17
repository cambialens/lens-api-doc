# Patent JSONL to CSV Parser

This project parses Patent jsonl file exported from The Lens into object models defined in `model.py` and produces csv file as output.

## How to use

`python patent_jsonl_parser.py lens-export.jsonl`

After execution of the script, csv file gets created in current working directory in a new folder `output-yyyy-mm-dd`. An optional output filename can be provided from argument.

`python patent_jsonl_parser.py lens-export.jsonl output.csv`

# Output schema

Field | Description | Example
---- | --- | ---
`lens_id` | Unique Lens Identifier | `100-004-910-081-14X`
`jurisdiction` | Jurisdiction of the patent document. | `US`
`kind` | Patent document kind code |`A1`
`display_key` | Unique document key | `US_9364525_B2_20160614`
`publication_date` | Date of publication for the patent document | `14/06/2016`
`publication_year` | Year of publication for the patent document | `14/06/2016`
`application_number` | Document number of the application | `37423807`
`application_date` | Date when a patent application is first filed at a patent office. | `16/07/2007`
`priority_numbers` | Document number of the priority document | `0614254`
`earliest_priority_date` | Earliest date of filing of a patent application, anywhere in the world | `18/07/2006`
`title` | Title of the patent | `Vaccines for malaria`
`abstract` | Abstract text | 
`applicants` | Patent applicant(s) name  | `COHEN JOSEPH D`
`inventors` | Patent inventor(s) name. | `MARCHAND MARTIN`
`owners` | Patent owner(s) name  | `CRUCELL HOLLAND B.V`
`document_type` | Type of Patent Document | `GRANTED_PATENT`
`cites_patent_count` | Number of patents documents cited by a given patent | `49`
`simple_family_size` | Number of simple family member documents | `51`
`extended_family_size` | Number of extended family member documents | `60`
`cpc_classification` | CPC patent classification codes | `A61K2039/6075`
`ipcr_classification` | IPCR patent classification codes | `C12N7/00`
`us_classification` | US patent classification codes | `530/389.1`
`npl_citation_count` | Number of original non-patent literature citations | `37`
`npl_resolved_citation_count` | Number of resolved scholarly works cited by a patent | `32`
`npl_resolved_lens_ids` | Lens Id of the resolved non-patent literature citations | `008-662-866-787-515`
`npl_resolved_external_ids` | Resolved external identifier(s) for cited non-patent literature | `10.1126/science.2416057`
`npl_citations` | Number of original non-patent literature citations | `37`
`legal_status` | Calculated legal status of the patent application | `ACTIVE`
