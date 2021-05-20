---
layout: post-sidebar
title: Patent Response
permalink: /response-patent.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Response Fields
        url: response-patent.html#response-fields
      - page: Sample Patent Record
        url: response-patent.html#sample-patent-record
---

### Response Fields

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**lens_id** | String | Unique lens identifier. Every document in the Lens has a unique 15-digit identifier called a Lens ID. | `186-488-232-022-055`
**jurisdiction** | String | The jurisidiction of the patent document. | `US`
**kind** | String | The patent document kind code (varies by jurisdiction). | `A1`
**date_published** | Date | Date of publication for the patent document. | `2009-05-22`
**doc_key** | String | The unique document key for the patent document. | `EP_0227762_B1_19900411`
**alias_lens_ids** | List | Derived lens Ids from docdb and full text identifiers 
**docdb_id** | Long | The DOCDB identifier for the patent document. | `499168393`
**publication_type** | String ([Document Types](#document-types)) | Type of patent document. | 
**lang** | String ([Language](#language)) | The original language of the patent document. | `EN`
**biblio** | [Bibliographic Data](#bibliographic-data) |  | 
**families** | [Families](#families) |  | 
**abstract** | List of [Abstract](#abstract) | The patent document abstract text. | 
**claims** | List of [Claims](#claims) | The Claims recorded in the patent document. | 
**description** | [Description](#description) | The description text of the patent document. | 
**legal_status** | [Legal Status Information](#legal-status-information) | The legal Status Information for the patent document. | 
{: .param-def }

### Bibliographic Data

 Field  |  Type  |  Description 
 --------  |  ---------  |  ------- 
**publication_reference** | [Document Id](#document-id) | The publication reference document Id. | 
**application_reference** | [Document Id](#document-id) | The application reference document Id. | 
**priority_claims** | [Priority Claims](#priority-claims) | The priotrity claims documents. | 
**invention_title** | List of [Title](#title) | Title of the patent / invention. | 
**parties** | [Parties](#parties) | The parties associated with the patent (applicants, inventors, owners, agents, etc.)  | 
**classifications_cpc** | [CPC Classifications](#cpc-classifications) | CPC Classifications | 
**classifications_ipcr** | [IPCR Classifications](#ipcr-classifications) | IPCR Classifications | 
**classifications_national** | [US Classifications](#us-classifications) | US Classifications | 
**references_cited** | [References Cited](#references-cited) | The references cited in the patent document (patents and non-patent literature (NPL) ). | 
**cited_by** | [Cited By](#cited-by) | The patents citing the patent document. |
{: .param-def }

### Families

Field  |  Type  |  Description 
--------  |  ---------  |  ------- 
**simple_family** | [Simple Family](#simple-family) | Simple patent family (based on [DOCDB simple patent family](https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/patent-families/docdb.html)). | 
**extended_family** | [Extended Family](#extended-family) | Extended patent family (based on [INPADOC extended patent family](https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/patent-families/inpadoc.html)). |   
{: .param-def }

### Simple Family

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**members** | List of [Simple Family Members](#simple-family-members) | List of simple family members. | 
**size** | Integer | The number of simple family member documents. | `12` 
{: .param-def }

### Simple Family Members

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | Simple family member document Id.  | 
**lens_id** | String (LensId) | Simple family member Lens Id.  | `186-488-232-022-055`
{: .param-def }

### Extended Family

Field  |  Type  |  Description | Example
--------  |  ---------  |  ------- | -------
**members** | List of [Extended Family Members](#extended-family-members) | List of extended family members. |  
**size** | Integer | The number of extended family member documents. | `18` 
{: .param-def }

### Extended Family Members

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | Extended family member document Id.  | 
**lens_id** |  String (LensId) | Extended family member Lens Id.  | `186-488-232-022-055`
{: .param-def }

### Abstract

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**text** | String | The patent document abstract text. | `A processor implements conditional vector operations in which an input vector containing multiple operands to be used in conditional operations is divided into two or more output…`
**lang** | String ([Language](#language)) | The language of the patent document abstract text. | `EN`
{: .param-def }

### Claims

 Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**claims** | List of [Claims Text](#claims-text) | The list of Claims recorded in the patent document. | 
**lang** | String ([Language](#language)) | The language of the patent document claims. | `EN`
{: .param-def }

### Claims Text

 Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**claim_text** | List of String | The Claim text recorded in the patent document. | `What is claimed is: 1. A method of performing a conditional vector output operation in a processor, the method comprising: receiving electrical signals representative of an input data vector…`
{: .param-def }

### Description

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**text** | String | The description text of the patent document. | `This invention was made in conjuction with U.S. Government support under U.S. Army Grant No. DABT63-96-C-0037.” BACKGROUND OF THE INVENTION 1. Field of the Invention The present invention is directed to…`
**lang** | String ([Language](#language)) | The language of the patent document description. | `EN`
{: .param-def }

### Legal Status Information 

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**granted** | Boolean | Indicates if the patent application has been granted in one or more jurisdictions. | `TRUE`
**grant_date** | Date | The date the patent application was granted (i.e. the application first grant date). | `2009-05-22`
**application_expiry_date** | Date | The expiry date of the patent application because of withdrawal or abandonment. | `2009-05-22`
**anticipated_term_date** | Date | The anticipated termination date for granted patents. The anticipated termination date is calculated based on the natural term date plus any extensions. | `2009-05-22`
**discontinuation_date** | Date | The discontinuation date of the patent due to "unnatural death" (i.e. lapse, withdrawn, abandoned). N.B. The patent can be revived within a certain time frame. | `2009-05-22`
**has_disclaimer** | Boolean | Indicates if this US patent subjected to a terminal disclaimer. | `TRUE`
**patent_status** | String ([Patent Status](#patent-status)) | The calculated legal status of the patent application. | `ACTIVE`
**has_spc** | Boolean | Indicates if the patent has a supplementary protection certificate. | `TRUE`
**calculation_log** | List of String | The legal status calculation log. | [`Application Filing Date: 2001-11-21`, `Earliest Filing Date: 2001-11-21 priority to EP01984746A`, `Granted date: 2009-07-29`]
{: .param-def }

**N.B.** Legal status information is derived from INPADOC data and may not be accurate. For more details, please see [Patent Legal Status Calculations](https://support.lens.org/help-resources/patents/patent-legal-status-calculations/)


### Priority Claims

 Field  |  Type  |  Description 
 --------  |  ---------  |  ------- 
**claims** | List of [Priority Claims Documents](#priority-claims-documents) | List of priority claims documents | 
{: .param-def }

### Priority Claims Documents

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**jurisdiction** | String ([Jurisdiction](#jurisidction)) | The jurisdiction of the priority document. | `DE`
**doc_number** | String | The document number of the priority document. | `1117265`
**kind** | String | The kind code of the priority document. | `A1`
**date** | LocalDate | The publication date of the priority document. | `2009-05-22`
**sequence** | Integer | The sequence of the Prioroty Claim Document | `3`
{: .param-def }

### Title

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**text** | String | Title of the patent / invention. | `Fidget Spinner`
**lang** | String ([Language](#language)) | The language of the patent / invention title. | `EN`
{: .param-def }

### Parties

 Field  |  Type  |  Description 
 --------  |  ---------  |  ------- 
**inventors** | List of [Inventors](#inventors) | List of inventors associated with the patent. | 
**applicants** | List of [Applicants](#applicants) | List of applicants associated with the patent. | 
**owners_all** | List of [Owners](#owners) | List of owners associated with the patent. | 
**agents** | List of [Agents and Attorneys](#agents-and-attorneys) | List of agents and attorneys associated with the patent. | 
{: .param-def }

<!-- **assignees** | List of [Assignees](#assignees) | List of assignees associated with the patent. |  -->

### Inventors

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**residence** | String | The country of residence of the inventor (ISO 2-digit country code). | `DE`
**sequence** | Integer | The sequence of the inventor listed on the patent document. | `3`
**extracted_name** | [Name](#name) | The patent inventor's name. | `Engebretson Steven P`
**extracted_address** | String | The address of the inventor. | `TORONTO, ONTARIA, CA`
{: .param-def }

<!--
### Inventor Name
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**value** | String | The patent inventor's name. | `Engebretson Steven P`
-->

### Applicants

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**residence** | String | The country of the applicant (ISO 2-digit country code). | `CA`
**sequence** | Integer | The sequence of the applicant listed on the patent document. | `2`
**extracted_name** | [Name](#name) | The patent applicant's name. | `IBM`
**extracted_address** | String | The applicant address as recorded on the patent. | `SEATTLE, WASHINGTON, US`
{: .param-def }

<!--
### Applicant Name
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**value** | String | The patent applicant's name. | `CPS Technology Holdings LLC`
-->

<!--
### Assignees
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**extracted_name** | [Name](#name) | The patent assignee's name. | `CPS Technology Holdings LLC`
**extracted_address** | String | The assignee address as recorded on the patent. | `TORONTO, ONTARIA, CA`
-->

<!--
### Assignee Name
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**value** | String | The assignee's name. | `CPS Technology Holdings LLC`
-->

### Owners

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**recorded_date** | Date | The ownership / assignment event record date. | `2009-05-22`
**execution_date** | Date | The date of execution of ownership / assignment. | `2009-05-22`
**extracted_name** | [Name](#name) | The patent owner name. | `CPS Technology Holdings LLC`
**extracted_address** | String | The owner address as recorded on the patent or legal event. | `TORONTO, ONTARIA, CA`
**extracted_country** | String | The owner's country code (ISO 2-digit country code). | `US`
{: .param-def }

<!--
### Owner Name
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**value** | String | The patent owner(s) name. | `CPS Technology Holdings LLC`
-->

### Agents and Attorneys

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**sequence** | Integer | The sequence of the agent/attorney as listed on the patent document. | `1`
**extracted_name** | [Name](#name) | The agent/attorney name. | `Chapman, Paul William et al.`
**extracted_address** | String | The agent/attorney address as recorded on the patent. | `20 Red Lion Street, GB-London WC1R 4PJ(GB)`
**extracted_country** | String | The country of the agent/attorney (ISO 2-digit country code). | `GB`
{: .param-def }

<!--
### Agent/Attorney Name
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**value** | String | The agent/attorney name. | `Chapman, Paul William et al.`
-->

### Name

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**value** | String | The party name. | `Chapman, Paul William et al.`, `CPS Technology Holdings LLC`, `Chapman, Paul William et al.`
{: .param-def }

### CPC Classifications

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**classifications** | List of [Classification Symbols](#classification-symbols) | List of CPC classification symbols. | `H01R11/01`
{: .param-def }

### IPCR Classifications

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**classifications** | List of [Classification Symbols](#classification-symbols) | List of IPCR classification symbols. | `H01R13/115`
{: .param-def }

### US Classifications

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**classifications** | List of [Classification Symbols](#classification-symbols) | List of US classification symbols. | `439/535`
{: .param-def }

### Classification Symbols

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**symbol** | String | Classification code symbol. | `H01R11/01`, `H01R13/115`, `439/535`
{: .param-def }

### References Cited

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**citations** | List of [Citations](#citations) | List of patent and NPL references cited. | 
**npl_resolved_count** | Integer | The number of resolved scholalry works cited by a patent. | `12`
**npl_count** | Integer | The number of scholalry works cited by a patent. | `2`
**patent_count** | Integer | The number of patents cited by a patent. | `2`
{: .param-def }
> Note: Citations can be duplicated because they appear in different phases of the patenting process.

### Citations

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**patcit** | [Patents Cited](#patents-cited) | Patents cited in the patent documnet. | 
**nplcit** | [NPL Cited](#npl-cited) | Non-patent literature cited in the patent document. | 
**sequence** | Integer | The sequence of the citation in the patent document. | `5`
**cited_phase** | String | The phase of the patenting process when the citation was added, see [Cited Phase](#cited-phase) | `SEA`
{: .param-def }

### Patents Cited

 Field  |  Type  |  Description | Example
 --------  |  ---------  |  ------- | ------- 
**document_id** | Array of [Document Id](#document-id) | The cited patent document Ids. | 
**lens_id** |  String (LensId) | The cited patent document Lens Id. | `118-962-823-688-691` |
{: .param-def }

### NPL Cited

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**text** | String | The original non-patent literature citation text in the patent document. | `Cormen et al., 'Introduction to Algorithms (MIT Electrical Engineering and Computer Science Series,' MIT Press, ISBN 0262031418, pp. 665-667, 695-697.`
**lens_id** |  String (LensId) | The Lens Id of the resolved non-patent literature citations (i.e. scholarly work Lens Id). | `168-663-423-050-326`
**external_ids** | List of String | List of external identifiers for non-patent literature citation (DOI, PubMed ID, PubMed Central ID or Microsoft Aacademic ID).  | `[10.1038/nature03090; 12345678919]`
{: .param-def }

### Cited By

 Field  |  Type  |  Description 
 --------  |  ---------  |  ------- 
**patents** | List of [Cited By Patents](#cited-by-patents) | List of patents citing the patent documnet. | 
{: .param-def }

### Cited By Patents

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | The citing patent document Id. | 
**lens_id** |  String (LensId) | The citing patent Lens Id. | `118-962-823-688-691` |
{: .param-def }

### Document Id

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**jurisdiction** | String ([Jurisdiction](#jurisidction)) | The jurisidiction of the patent document. | `US`
**doc_number** | String | The document number assigned to a patent application on publication. | `20130227762`
**kind** | String | The patent document kind code (varies by jurisdiction). | `A1`
**date** | LocalDate | Date of publication for the patent document, or filing date for the application reference. | `2009-05-22`
{: .param-def }

---

### Enums

#### Document Types
`AMENDED_PATENT`, `AMENDED_PATENT`, `DESIGN_RIGHT`, `GRANTED_PATENT`, `LIMITED_PATENT`, `PATENT_APPLICATION`, `PLANT_PATENT`, `SEARCH_REPORT`, `STATUTORY_INVENTION_REGISTRATION`, `SPC`, `UNKNOWN`

##### Jurisidction
Jurisidction codes: `US`, `EP`, `WO`, `DE`, `CN`, `JP`, `GB`, etc.

##### Language
Language codes:  `EN`, `FR`, `DE`, `CN` etc.

##### Patent Status
 - `ACTIVE` - Granted patent is in force
 - `PENDING` - Application is pending
 - `DISCONTINUED` - Application discontinued, withdrawn or rejected, i.e. discontinuation before grant
 - `INACTIVE` - Granted patent not in force because of lapse, non-fee payment, etc. The patent hasn't reached the term date and can be revived
 - `EXPIRED` - Patent has reached the term date and is no longer in force
 - `PATENTED` - PCT applications that have been granted in one or more designated states, or non-PCT granted patents without enough information to calculate the term date
 - `UNKNOWN` -  Not enough information to calculate status 

##### Cited Phase
- `SEA` - Originates from the Search report, date search report completed
- `ISR` - Originates from International Search Report, date international search report completed
- `SUP` - Originates from Supplementary Search Report, date supplementary search report completed
- `PRS` - Origin Pre-Grant/Pre-Search national, date search report completed
- `APP` - Cited by the Applicant, date information available in EPO systems
- `EXA` - Revealed during the Examination phase (citing document is kind-code 'A'), date information available in EPO systems
- `OPP` - Revealed during the Opposition phase, date opposition letters filed
- `APL` - Filed for appeal by applicant / proprietor / patentee, date appeal filed
- `FOP` - Filed for opposition by any third party, date observation letters filed
- `TPO` - Third party observation, date observation letters filed
- `CH2` - Chapter 2, date international search report completed


<!--
##### Source
`USPTO_FULLTEXT`, `USPTO_ASSIGNMENT`, `EPO_FULLTEXT`, `WIPO_FULLTEXT`, `IP_AUSTRALIA_FULLTEXT`, `DOCDB`, `DOCDB_NATIONAL_OFFICE`, `DOCDB_TRANSCRIPT`, `DOCDB_TRANSLATION`, `DOCDB_EPO`, `DOCDB_PAJ`, `INPADOC`, `LENS`, `UNKNOWN`
##### Prosecution Stage
`FILING`,`EXAMINATION`,`PRE_GRANT_CHALLENGE`,`GRANT,POST_GRANT_CHALLENGE`,`INACTIVE`,`TERMINATION`
-->

---

### Sample Patent Record

```json
{
    "lens_id": "031-156-664-516-153",
    "jurisdiction": "EP",
    "doc_number": "2471949",
    "kind": "A1",
    "date_published": "2012-07-04",
    "doc_key": "EP_2471949_A1_20120704",
    "docdb_id": 364714255,
    "lang": "en",
    "biblio": {
        "publication_reference": {
            "jurisdiction": "EP",
            "doc_number": "2471949",
            "kind": "A1",
            "date": "2012-07-04"
        },
        "application_reference": {
            "jurisdiction": "EP",
            "doc_number": "10197481",
            "kind": "A",
            "date": "2010-12-31"
        },
        "priority_claims": {
            "claims": [
                {
                    "jurisdiction": "EP",
                    "doc_number": "10197481",
                    "kind": "A",
                    "date": "2010-12-31",
                    "sequence": 1
                }
            ]
        },
        "invention_title": [
            {
                "text": "Verfahren zur Identifizierung durch Molekulartechniken von genetischen Varianten, die kein D-Antigen (D-) und das veränderte C-Antigen (C+W) codieren",
                "lang": "de"
            },
            {
                "text": "Method for the identification by molecular techniques of genetic variants that encode no D antigen (D-) and altered C antigen (C+W)",
                "lang": "en"
            },
            {
                "text": "Procédé pour l'identification par des techniques moléculaires de variantes génétiques ne codant pas d'antigène D (D-) et qui codent l'antigène C modifié (C+W)",
                "lang": "fr"
            }
        ],
        "parties": {
            "applicants": [
                {
                    "residence": "ES",
                    "extracted_name": {
                        "value": "PROGENIKA BIOPHARMA SA"
                    }
                }
            ],
            "inventors": [
                {
                    "residence": "ES",
                    "sequence": 1,
                    "extracted_name": {
                        "value": "OCHOA JORGE"
                    }
                },
                {
                    "residence": "ES",
                    "sequence": 2,
                    "extracted_name": {
                        "value": "LOPEZ MONICA"
                    }
                },
                {
                    "residence": "ES",
                    "sequence": 3,
                    "extracted_name": {
                        "value": "TEJEDOR DIEGO"
                    }
                },
                {
                    "residence": "ES",
                    "sequence": 4,
                    "extracted_name": {
                        "value": "MARTINEZ ANTONIO"
                    }
                },
                {
                    "residence": "ES",
                    "sequence": 5,
                    "extracted_name": {
                        "value": "SIMON LAUREANO"
                    }
                }
            ],
            "agents": [
                {
                    "extracted_name": {
                        "value": "Casley, Christopher Stuart"
                    },
                    "extracted_address": "Mewburn Ellis LLP \n33 Gutter Lane, London\nEC2V 8AS",
                    "extracted_country": "GB"
                }
            ],
            "owners_all": [
                {
                    "recorded_date": "2013-12-11",
                    "extracted_name": {
                        "value": "PROGENIKA BIOPHARMA, S.A."
                    }
                }
            ]
        },
        "classifications_ipcr": {
            "classifications": [
                {
                    "symbol": "C12Q1/68"
                }
            ]
        },
        "classifications_cpc": {
            "classifications": [
                {
                    "symbol": "A61K35/14"
                },
                {
                    "symbol": "C12Q1/6881"
                },
                {
                    "symbol": "C12Q1/6881"
                },
                {
                    "symbol": "C12Q2600/156"
                },
                {
                    "symbol": "C12Q2600/156"
                }
            ]
        },
        "references_cited": {
            "citations": [
                {
                    "sequence": 1,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2006075254",
                            "kind": "A2",
                            "date": "2006-07-20"
                        },
                        "lens_id": "185-701-234-511-622"
                    }
                },
                {
                    "sequence": 2,
                    "nplcit": {
                        "text": "AVENT N D ET AL: \"The bloodgen project of the European Union, 2003-2009\", TRANSFUSION MEDICINE AND HEMOTHERAPY 2009 S. KARGER AG CHE LNKD- DOI:10.1159/000218192, vol. 36, no. 3, June 2009 (2009-06-01), pages 162 - 167, XP002633276, ISSN: 1660-3796",
                        "lens_id": "004-047-148-411-345",
                        "external_ids": [
                            "pmc2980524",
                            "10.1159/000218192",
                            "21113258"
                        ]
                    }
                },
                {
                    "sequence": 3,
                    "nplcit": {
                        "text": "WESTHOFF CONNIE M ET AL: \"DIIIa and DIII Type 5 are encoded by the same allele and are associated with altered RHCE*ce alleles: clinical implications\", TRANSFUSION (MALDEN), vol. 50, no. 6, June 2010 (2010-06-01), pages 1303 - 1311, XP002633277, ISSN: 0041-1132",
                        "lens_id": "125-529-168-227-632",
                        "external_ids": [
                            "10.1111/j.1537-2995.2009.02573.x",
                            "pmc2908519",
                            "20088832"
                        ]
                    }
                },
                {
                    "sequence": 4,
                    "nplcit": {
                        "text": "PHAM BACH-NGA ET AL: \"Heterogeneous molecular background of the weak C, VS+, hr(B)-, Hr(B)- phenotype in black persons\", TRANSFUSION (MALDEN), vol. 49, no. 3, March 2009 (2009-03-01), pages 495 - 504, XP002633278, ISSN: 0041-1132",
                        "lens_id": "086-240-354-498-516",
                        "external_ids": [
                            "10.1111/j.1537-2995.2008.02005.x",
                            "19040491"
                        ]
                    }
                },
                {
                    "sequence": 5,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2006032897",
                            "kind": "A2",
                            "date": "2006-03-30"
                        },
                        "lens_id": "071-147-450-571-460"
                    }
                },
                {
                    "sequence": 6,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "DE",
                            "doc_number": "10049363",
                            "kind": "A1",
                            "date": "2001-10-31"
                        },
                        "lens_id": "033-566-032-105-609"
                    }
                },
                {
                    "sequence": 7,
                    "nplcit": {
                        "text": "FAAS B H W ET AL: \"Rh E/e genotyping by allele-specific primer amplification\", BLOOD, AMERICAN SOCIETY OF HEMATOLOGY, US, vol. 85, no. 3, 1 January 1995 (1995-01-01), pages 829 - 832, XP002614101, ISSN: 0006-4971",
                        "lens_id": "017-174-583-162-658",
                        "external_ids": [
                            "7833484",
                            "10.1182/blood.v85.3.829.bloodjournal853829"
                        ]
                    }
                },
                {
                    "sequence": 8,
                    "nplcit": {
                        "text": "MAASKANT-VAN WIJK P A ET AL: \"GENOTYPING OR RHD BY MULTIPLEX POLYMERASE CHAIN REACTIONS ANALYSIS OF SIX RHD-SPECIFIC EXONS\", TRANSFUSION, AMERICAN ASSOCIATION OF BLOOD BANKS, BETHESDA, MD, US, vol. 11, no. 38, 1 November 1998 (1998-11-01), pages 1015 - 1021, XP008005129, ISSN: 0041-1132, DOI: DOI:10.1046/J.1537-2995.1998.38111299056309.X",
                        "lens_id": "059-652-196-800-856",
                        "external_ids": [
                            "10.1046/j.1537-2995.1998.38111299056309.x",
                            "9838930"
                        ]
                    }
                },
                {
                    "sequence": 9,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2011003921",
                            "kind": "A2",
                            "date": "2011-01-13"
                        },
                        "lens_id": "187-498-666-224-100"
                    }
                },
                {
                    "sequence": 1,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2009000084",
                            "kind": "A1",
                            "date": "2008-12-31"
                        },
                        "lens_id": "096-184-763-479-702"
                    }
                },
                {
                    "sequence": 2,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010000210",
                            "kind": "A1",
                            "date": "2010-01-07"
                        },
                        "lens_id": "082-610-612-867-442"
                    }
                },
                {
                    "sequence": 3,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010000380",
                            "kind": "A1",
                            "date": "2010-01-07"
                        },
                        "lens_id": "080-193-167-878-372"
                    }
                },
                {
                    "sequence": 4,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010000635",
                            "kind": "A1",
                            "date": "2010-01-07"
                        },
                        "lens_id": "160-241-370-254-307"
                    }
                },
                {
                    "sequence": 5,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010000972",
                            "kind": "A1",
                            "date": "2010-01-07"
                        },
                        "lens_id": "189-848-800-128-321"
                    }
                },
                {
                    "sequence": 6,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010002366",
                            "kind": "A1",
                            "date": "2010-01-07"
                        },
                        "lens_id": "091-724-438-661-108"
                    }
                },
                {
                    "sequence": 7,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010002367",
                            "kind": "A1",
                            "date": "2010-01-07"
                        },
                        "lens_id": "180-004-304-457-874"
                    }
                },
                {
                    "sequence": 8,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010003113",
                            "kind": "A1",
                            "date": "2010-01-07"
                        },
                        "lens_id": "014-308-334-256-321"
                    }
                },
                {
                    "sequence": 9,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010003649",
                            "kind": "A1",
                            "date": "2010-01-14"
                        },
                        "lens_id": "149-519-969-815-807"
                    }
                },
                {
                    "sequence": 10,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010003664",
                            "kind": "A1",
                            "date": "2010-01-14"
                        },
                        "lens_id": "134-590-889-498-511"
                    }
                },
                {
                    "sequence": 11,
                    "patcit": {
                        "document_id": {
                            "jurisdiction": "WO",
                            "doc_number": "2010003809",
                            "kind": "A2",
                            "date": "2010-01-14"
                        },
                        "lens_id": "087-699-367-879-444"
                    }
                },
                {
                    "sequence": 12,
                    "nplcit": {
                        "text": "M. E. REID; C. LOMAS-FRANCIS: \"The Blood Group Antigen FactsBook\", 2004, ELSEVIER LTD."
                    }
                },
                {
                    "sequence": 13,
                    "nplcit": {
                        "text": "CONNIE M.; WESTHOFF, SUNITHA VEGE; CHRISTINE HALTER-HIPSKY; TRINA WHORLEY; KIM HUE-ROYE; CHRISTINE LOMAS-FRANCIS; MARION E.: \"Dllla and Dill Type 5 are encoded by the same allele and are associated with altered RHCE*ce alleles: clinical implications\", REID. TRANSFUSION, vol. 50, 2010, pages 1303 - 1311",
                        "lens_id": "125-529-168-227-632",
                        "external_ids": [
                            "10.1111/j.1537-2995.2009.02573.x",
                            "pmc2908519",
                            "20088832"
                        ]
                    }
                },
                {
                    "sequence": 14,
                    "nplcit": {
                        "text": "BACH-NGA PHAM; THIERRY PEYRARD; GENEVIEVE JUSZCZAK; ISABELLE DUBEAUX; DOMINIQUE GIEN; ANTOINE BLANCHER; JEAN-PIERRE CARTRON; PHILI: \"Heterogeneous molecular background of the weak C, VS+, hrB-, HrB- phenotype in black persons\", TRANSFUSION, vol. 49, 2009, pages 495 - 504",
                        "lens_id": "086-240-354-498-516",
                        "external_ids": [
                            "10.1111/j.1537-2995.2008.02005.x",
                            "19040491"
                        ]
                    }
                },
                {
                    "sequence": 15,
                    "nplcit": {
                        "text": "MARTINE G.H.M.; TAX, C.; ELLEN VAN DER SCHOOT; RENE' VAN DOORN; LOTTE DOUGLAS-BERGER; DICK J.; VAN RHENEN; PETRA A.; MAASKANT-VAN: \"RHC and RHc genotyping in different ethnic groups\", TRANSFUSION, vol. 42, 2002, pages 6234 - 644",
                        "lens_id": "028-957-496-647-171",
                        "external_ids": [
                            "10.1046/j.1537-2995.2002.00096.x",
                            "12084173"
                        ]
                    }
                },
                {
                    "sequence": 16,
                    "nplcit": {
                        "text": "M. E. REID; C. LOMAS-FRANCIS.: \"The Blood group antigen FactsBook\", 2004, ELSEVIER LTD."
                    }
                }
            ],
            "npl_resolved_count": 8,
            "npl_count": 10
        },
        "cited_by": {
            "patents": [
                {
                    "document_id": {
                        "jurisdiction": "US",
                        "doc_number": "9359643",
                        "kind": "B2"
                    },
                    "lens_id": "007-584-344-944-889"
                },
                {
                    "document_id": {
                        "jurisdiction": "US",
                        "doc_number": "9637788",
                        "kind": "B2"
                    },
                    "lens_id": "138-800-291-931-331"
                },
                {
                    "document_id": {
                        "jurisdiction": "US",
                        "doc_number": "10253366",
                        "kind": "B2"
                    },
                    "lens_id": "172-445-088-115-557"
                },
                {
                    "document_id": {
                        "jurisdiction": "WO",
                        "doc_number": "2012171990",
                        "kind": "A1"
                    },
                    "lens_id": "084-623-881-707-629"
                },
                {
                    "document_id": {
                        "jurisdiction": "WO",
                        "doc_number": "2014135331",
                        "kind": "A1"
                    },
                    "lens_id": "089-849-576-069-505"
                },
                {
                    "document_id": {
                        "jurisdiction": "WO",
                        "doc_number": "2014135331",
                        "kind": "A1"
                    },
                    "lens_id": "089-849-576-069-505"
                }
            ],
            "count": 6
        }
    },
    "families": {
        "simple_family": {
            "members": [
                {
                    "document_id": {
                        "jurisdiction": "EP",
                        "doc_number": "2471949",
                        "kind": "B1",
                        "date": "2013-12-25"
                    },
                    "lens_id": "033-643-087-926-128"
                },
                {
                    "document_id": {
                        "jurisdiction": "EP",
                        "doc_number": "2471949",
                        "kind": "A1",
                        "date": "2012-07-04"
                    },
                    "lens_id": "031-156-664-516-153"
                },
                {
                    "document_id": {
                        "jurisdiction": "US",
                        "doc_number": "20120172239",
                        "kind": "A1",
                        "date": "2012-07-05"
                    },
                    "lens_id": "095-621-040-202-546"
                },
                {
                    "document_id": {
                        "jurisdiction": "ES",
                        "doc_number": "2445709",
                        "kind": "T3",
                        "date": "2014-03-04"
                    },
                    "lens_id": "192-287-095-019-170"
                },
                {
                    "document_id": {
                        "jurisdiction": "US",
                        "doc_number": "20160060696",
                        "kind": "A1",
                        "date": "2016-03-03"
                    },
                    "lens_id": "126-336-041-308-107"
                }
            ],
            "size": 5
        },
        "extended_family": {
            "members": [
                {
                    "document_id": {
                        "jurisdiction": "EP",
                        "doc_number": "2471949",
                        "kind": "B1",
                        "date": "2013-12-25"
                    },
                    "lens_id": "033-643-087-926-128"
                },
                {
                    "document_id": {
                        "jurisdiction": "EP",
                        "doc_number": "2471949",
                        "kind": "A1",
                        "date": "2012-07-04"
                    },
                    "lens_id": "031-156-664-516-153"
                },
                {
                    "document_id": {
                        "jurisdiction": "ES",
                        "doc_number": "2445709",
                        "kind": "T3",
                        "date": "2014-03-04"
                    },
                    "lens_id": "192-287-095-019-170"
                },
                {
                    "document_id": {
                        "jurisdiction": "US",
                        "doc_number": "20120172239",
                        "kind": "A1",
                        "date": "2012-07-05"
                    },
                    "lens_id": "095-621-040-202-546"
                },
                {
                    "document_id": {
                        "jurisdiction": "US",
                        "doc_number": "20160060696",
                        "kind": "A1",
                        "date": "2016-03-03"
                    },
                    "lens_id": "126-336-041-308-107"
                }
            ],
            "size": 5
        }
    },
    "legal_status": {
        "granted": true,
        "grant_date": "2013-12-25",
        "anticipated_term_date": "2030-12-31",
        "calculation_log": [
            "Application Filing Date: 2010-12-31",
            "Granted date: 2013-12-25"
        ],
        "patent_status": "ACTIVE"
    },
    "abstract": [
        {
            "text": "The invention relates to the field of genotyping and blood cell antigen determination. In particular, the invention adresses the problem of discriminating the RHD*DIIIa-CE(4-7)-D or RHD*DIIIa-CE(4-7)-D )-like blood type variants, which express the C +w antigen and lack a D antigen, from RHD*DIIIa , RHD*DIVa-2 and other blood type variants. The invention provides methods for genotyping a subject, comprising: a) determining at least 4 markers in a sample that has been obtained from the subject, wherein the markers comprise: (i) the presence or absence of an RHCE*C allele; (ii) the presence or absence of an RHD/RHCE hybrid exon 3 (RHD/CE Hex03) allele; (iii) the absence of, or a single nucleotide polymorphism (SNP) variant within, of any one of the SNPs at position 602 of RHD exon 4, position 667 of RHD exon 5, or position 819 of RHD exon 6; and (iv) the absence of, or SNP variant within, of the SNP at position 1048 of RHD exon 7. The invention also provides products, in particular, probes, primers and kits for use in such methods.",
            "lang": "en"
        }
    ],
    "claims": [
        {
            "claims": [
                {
                    "claim_text": [
                        "A method of genotyping a subject, the method comprising:\n determining at least 4 markers in a sample that has been obtained from the subject, wherein the markers comprise:\n (i) the presence or absence of an RHCE*C allele; \n (ii) the presence or absence of an RHD/RHCE hybrid exon 3 (RHD/CE Hex03) allele; \n (iii) the absence of, or a single nucleotide polymorphism (SNP) variant within, any one of RHD exon 4,  RHD  exon 5, or  RHD  exon 6; and \n (iv) the absence of, or SNP variant within, RHD exon 7."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to claim 1, wherein:\n a) the SNP variant within  RHD  exon 4 is at position 602 of the  RHD  coding sequence (rs1053355), the SNP variant within  RHD  exon 5 is at position 667 of the  RHD  coding sequence (rs1053356), the SNP variant within  RHD  exon 6 is at position 819 of the  RHD  coding sequence; and/or \n b) the SNP variant within  RHD  exon 7 is at position 1048 of the  RHD  coding sequence (rs41307826)."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to claim 1 or 2, wherein the markers further comprise:\n (v) the presence or absence of an RHD exon 3 allele."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to any one of the preceding claims, wherein:\n a) the method further comprises determining the RHD and RHC antigen phenotypes of the subject; and/or \n b) the method comprises detecting the presence or absence of a blood type variant selected from:  RHD*DIIIa ;  RHD*DIVa-2;  or  RHD*DIIIa-CE(4-7)-D  or  RHD*DIIIa-CE(4-7)-D )-like blood type variants, e.g. wherein the method comprises detecting the presence or absence of  RHD*DIIIa-CE(4-7)-D  or  RHD*DIIIa-CE(4-7)-D )-like blood type variants; and/or \n c) marker (iii) is the SNP within RHD exon 4 at position 602 of the RHD coding sequence (rs1053355); and/or \n d) the RHCE*C allele is determined by determining the..."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to any one of the preceding claims, wherein the sample comprises nucleic acid and the method comprises amplifying the nucleic acid or a portion thereof by PCR using primers, e.g. wherein:\n a) the PCR primers for determining the RHCE*C allele are a forward PCR primer specific for RHCE*C, and a non-specific reverse PCR primer, e.g. wherein\n (i) the non-specific reverse primer is shared with RHD, RHC*C and/or RHC*c; and/or \n (ii) the PCR primers comprise:\n Forward: 5'-GGCCACCACCATTTGAA-3' (SEQ ID NO: 3) \n Reverse: 5'-CCATGAACATGCCACTTCAC-3'..."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to claim 5, wherein the amplified nucleic acid comprises a label, e.g. wherein\n a) the label comprises a biotinylated nucleotide; and/or \n b) the label comprises a fluorescent moiety."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to any one of the preceding claims, wherein the sample comprises nucleic acid, and the method comprises amplifying the nucleic acid or a portion thereof by PCR using primers, fragmenting the amplified nucleic acid, and labelling the fragmented nucleic acid with biotinylated ddNTPS using a terminal deoxynucleotidyl transferase (TdT) enzyme."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to any one of the preceding claims, wherein determining the presence, absence or SNP variant of a marker comprises contacting nucleic acid containing each marker with one or more probes, e.g. wherein:\n a) as dependent from claim 3, the probes for determining the presence or absence of RHD/CE Hex03 or RHD exon 3 contact an SNP located in both RHD/CE Hex03 and RHD exon 3, wherein one SNP variant is specific for RHD/CE Hex03, and another SNP variant is specific for RHD exon 3, e.g. wherein\n (i) the SNP is at position 410 of the coding sequence, located within both RHD/CE Hex03 and RHD exon 3; and/or \n (ii) the probes comprise:\n (1) 5'-TTTTACAGACGCCTGCTACCATG-3'..."
                    ]
                },
                {
                    "claim_text": [
                        "A method according to claim 8, wherein\n a) one or more of the probes comprise a label, e.g. wherein the label is a fluorescent moiety; and/or \n b) one or more of the probes is attached to a solid support or conjugated to one or more particles.."
                    ]
                },
                {
                    "claim_text": [
                        "A set of primers for amplifying nucleic acid comprising at least four of the markers described in claim 1, 2, 3, 4(c), and 4(d), e.g. wherein the set of primers comprises at least three primer pairs selected from the primers set forth in:\n (i) claim 5(a), \n (ii) claim 5(b), \n (iii) any one of claims 5(c), 5(d) or 5(e) \n (iv) claim 5(f), and \n (v) claim 5(g)."
                    ]
                },
                {
                    "claim_text": [
                        "A set of primers for amplifying nucleic acid comprising at least three primer pairs selected from the primers set forth in:\n (i) claim 3(a)(ii), \n (ii) claim 3(b)(i), \n (iii) any one of claims 3(c)(i), 3(d)(i) or 3(e)(i), \n (iv) claim 3(f)(i), and \n (v) claim 3(g)(i)."
                    ]
                },
                {
                    "claim_text": [
                        "A set of primers for amplifying nucleic acid , wherein at least 50% are the primer pairs described in claim 10 or 11."
                    ]
                },
                {
                    "claim_text": [
                        "A set of probes for determining the presence, absence or single nucleotide polymorphism (SNP) variant of at least three of the markers described in claim 1, 2, 3, 2(c) and 2(d), e.g. wherein:\n a) the set of probes comprises the probes described in claims 8(a), 8(b) and 8(c)."
                    ]
                },
                {
                    "claim_text": [
                        "A set of probes according to claim 13, wherein:\n a) the probes are immobilised on a solid support or conjugated to one or more particles, e.g. wherein the solid support comprises one or more attached labels, e.g. wherein the label is a fluorochrome; and/or \n b) one or more probes comprise a label, e.g wherein the label is a fluorescent moiety."
                    ]
                },
                {
                    "claim_text": [
                        "A kit for genotyping a subject, the kit comprising a set of PCR primers according to any one of claims 10 to 12, and a set of probes according to any one of claims 13 or 14." 
                    ]
                }
            ],
            "lang": "en"
        }
    ],
    "description": {
        "text": "Field of the Invention The invention relates to methods for genotyping and blood cell antigen determination, which in particular may discriminate the  RHD*DIIIa-CE(4-7)-D  or  RHD*DIIIa-CE(4-7)-D )-like blood type variants, which express the C +W  antigen and lack a D antigen, from  RHD*DIIIa ,  RHD*DIVa-2  and other blood type variants. The invention also relates to products, in particular, probes, primers and kits for use in such methods. Background to the Invention The success of blood transfusion often depends on the degree of compatibility between donor and recipient. The degree of compatibility, in turn...",
        "lang": "en"
    },
    "publication_type": "PATENT_APPLICATION"
}
```

[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
