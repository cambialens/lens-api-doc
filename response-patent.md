---
layout: post-sidebar
title: Patent Response
permalink: /response-patent.html
show_sidebar: true
sidebar: toc
toc:
  - title: Patent API Response
    subfolderitems:
      - page: Metadata Fields
        url: response-patent.html#metadata-fields
      - page: Sample Patent Record
        url: response-patent.html#sample-patent-record
---
<!--
{:.table-contents}
- [Metadata Fields](#metadata-fields)
- [Sample Patent Record](#sample-patent-record)
-->
### Metadata Fields

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**lens_id** | String | Unique lens identifier. Every document in the Lens has a unique 15-digit identifier called a Lens ID. | `186-488-232-022-055`
**jurisdiction** | String | The jurisidiction of the patent document. | `US`
**kind** | String | The patent document kind code (varies by jurisdiction). | `A1`
**date_published** | Date | Date of publication for the patent document. | `2009-05-22`
**doc_key** | String | The unique document key for the patent document. | `EP_0227762_B1_19900411`
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

### Families

Field  |  Type  |  Description 
--------  |  ---------  |  ------- 
**simple_family** | [Simple Family](#simple-family) | Simple patent family (based on [DOCDB simple patent family](https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/patent-families/docdb.html)). | 
**extended_family** | [Extended Family](#extended-family) | Extended patent family (based on [INPADOC extended patent family](https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/patent-families/inpadoc.html)). |   

### Simple Family

Field  |  Type  |  Description 
--------  |  ---------  |  -------
**members** | List of [Simple Family Members](#simple-family-members) | List of simple family members. | 

### Simple Family Members

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | Simple family member document Id.  | 
**lens_id** | String (LensId) | Simple family member Lens Id.  | `186-488-232-022-055`

### Extended Family

Field  |  Type  |  Description | Example
--------  |  ---------  |  ------- | -------
**members** | List of [Extended Family Members](#extended-family-members) | List of extended family members. |  

### Extended Family Members

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | Extended family member document Id.  | 
**lens_id** |  String (LensId) | Extended family member Lens Id.  | `186-488-232-022-055`

### Abstract

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**text** | String | The patent document abstract text. | `A processor implements conditional vector operations in which an input vector containing multiple operands to be used in conditional operations is divided into two or more output…`
**lang** | String ([Language](#language)) | The language of the patent document abstract text. | `EN`

### Claims

 Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**claims** | List of [Claims Text](#claims-text) | The list of Claims recorded in the patent document. | 
**lang** | String ([Language](#language)) | The language of the patent document claims. | `EN`

### Claims Text

 Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**claim_text** | List of String | The Claim text recorded in the patent document. | `What is claimed is: 1. A method of performing a conditional vector output operation in a processor, the method comprising: receiving electrical signals representative of an input data vector…`

### Description

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**text** | String | The description text of the patent document. | `This invention was made in conjuction with U.S. Government support under U.S. Army Grant No. DABT63-96-C-0037.” BACKGROUND OF THE INVENTION 1. Field of the Invention The present invention is directed to…`
**lang** | String ([Language](#language)) | The language of the patent document description. | `EN`

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
**publication_count** | Integer | The number of publications for the DocDB application | `12`
**has_spc** | Boolean | Indicates if the patent has a supplementary protection certificate. | `TRUE`

### Priority Claims

 Field  |  Type  |  Description 
 --------  |  ---------  |  ------- 
**claims** | List of [Priority Claims Documents](#priority-claims-documents) | List of priority claims documents | 

### Priority Claims Documents

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**jurisdiction** | String ([Jurisdiction](#jurisidction)) | The jurisdiction of the priority document. | `DE`
**doc_number** | String | The document number of the priority document. | `1117265`
**kind** | String | The kind code of the priority document. | `A1`
**date** | LocalDate | The publication date of the priority document. | `2009-05-22`
**sequence** | Integer | The sequence of the Prioroty Claim Document | `3`

### Title

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**text** | String | Title of the patent / invention. | `Fidget Spinner`
**lang** | String ([Language](#language)) | The language of the patent / invention title. | `EN`

### Parties

 Field  |  Type  |  Description 
 --------  |  ---------  |  ------- 
**inventors** | List of [Inventors](#inventors) | List of inventors associated with the patent. | 
**applicants** | List of [Applicants](#applicants) | List of applicants associated with the patent. | 
**assignees** | List of [Assignees](#assignees) | List of assignees associated with the patent. | 
**owners_all** | List of [Owners](#owners) | List of owners associated with the patent. | 
**agents** | List of [Agents and Attorneys](#agents-and-attorneys) | List of agents and attorneys associated with the patent. | 

### Inventors

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**residence** | String | The country of residence of the inventor (ISO 2-digit country code). | `DE`
**sequence** | Integer | The sequence of the inventor listed on the patent document. | `3`
**extracted_name** | [Name](#name) | The patent inventor's name. | `Engebretson Steven P`
**extracted_address** | String | The address of the inventor. | `TORONTO, ONTARIA, CA`

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

<!--
### Applicant Name
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**value** | String | The patent applicant's name. | `CPS Technology Holdings LLC`
-->

### Assignees

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**extracted_name** | [Name](#name) | The patent assignee's name. | `CPS Technology Holdings LLC`
**extracted_address** | String | The assignee address as recorded on the patent. | `TORONTO, ONTARIA, CA`

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

### CPC Classifications

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**classifications** | List of [Classification Symbols](#classification-symbols) | List of CPC classification symbols. | `H01R11/01`

### IPCR Classifications

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**classifications** | List of [Classification Symbols](#classification-symbols) | List of IPCR classification symbols. | `H01R13/115`

### US Classifications

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**classifications** | List of [Classification Symbols](#classification-symbols) | List of US classification symbols. | `439/535`

### Classification Symbols

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**symbol** | String | Classification code symbol. | `H01R11/01`, `H01R13/115`, `439/535`

### References Cited

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**citations** | List of [Citations](#citations) | List of patent and NPL references cited. | 
**npl_resolved_count** | Integer | The number of resolved scholalry works cited by a patent. | `12`
**npl_count** | Integer | The number of scholalry works cited by a patent. | `2`

### Citations

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**patcit** | [Patents Cited](#patents-cited) | Patents cited in the patent documnet. | 
**nplcit** | [NPL Cited](#npl-cited) | Non-patent literature cited in the patent document. | 
**sequence** | Integer | The sequence of the citation in the patent document. | `5`

### Patents Cited

 Field  |  Type  |  Description | Example
 --------  |  ---------  |  ------- | ------- 
**document_id** | Array of [Document Id](#document-id) | The cited patent document Ids. | 
**lens_id** |  String (LensId) | The cited patent document Lens Id. | `118-962-823-688-691` |

### NPL Cited

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**text** | String | The original non-patent literature citation text in the patent document. | `Cormen et al., 'Introduction to Algorithms (MIT Electrical Engineering and Computer Science Series,' MIT Press, ISBN 0262031418, pp. 665-667, 695-697.`
**lens_id** |  String (LensId) | The Lens Id of the resolved non-patent literature citations (i.e. scholarly work Lens Id). | `168-663-423-050-326`
**external_ids** | List of String | List of external identifiers for non-patent literature citation (DOI, PubMed ID, PubMed Central ID or Microsoft Aacademic ID).  | `[10.1038/nature03090; 12345678919]`

### Cited By

 Field  |  Type  |  Description 
 --------  |  ---------  |  ------- 
**patents** | List of [Cited By Patents](#cited-by-patents) | List of patents citing the patent documnet. | 

### Cited By Patents

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | The citing patent document Id. | 
**lens_id** |  String (LensId) | The citing patent Lens Id. | `118-962-823-688-691` |

### Document Id

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**jurisdiction** | String ([Jurisdiction](#jurisidction)) | The jurisidiction of the patent document. | `US`
**doc_number** | String | The document number assigned to a patent application on publication. | `20130227762`
**kind** | String | The patent document kind code (varies by jurisdiction). | `A1`
**date** | LocalDate | Date of publication for the patent document. | `2009-05-22`

---

### Enums

#### Document Types
`AMENDED_PATENT`, `AMENDED_PATENT`, `DESIGN_RIGHT`, `GRANTED_PATENT`, `LIMITED_PATENT`, `PATENT_APPLICATION`, `PLANT_PATENT`, `SEARCH_REPORT`, `STATUTORY_INVENTION_REGISTRATION`, `SPC`, `UNKNOWN`

##### Jurisidction
Jurisidction codes: `US`, `EP`, `WO`, `DE`, `CN`, `JP`, `GB`, etc.

##### Language
Language codes:  `EN`, `FR`, `DE`, `CN` etc.

##### Patent Status
 - `PENDING` - Application pending
 - `DISCONTINUED` - Discontinued, Withdrawn or Rejected
 - `PATENTED` - In case of WO application is grant in some designated state
 - `ACTIVE` - Patent is in force
 - `INACTIVE` - Patent is inactive with chance of revivals
 - `EXPIRED` - Patent is not in force

<!--
##### Source
`USPTO_FULLTEXT`, `USPTO_ASSIGNMENT`, `EPO_FULLTEXT`, `WIPO_FULLTEXT`, `IP_AUSTRALIA_FULLTEXT`, `DOCDB`, `DOCDB_NATIONAL_OFFICE`, `DOCDB_TRANSCRIPT`, `DOCDB_TRANSLATION`, `DOCDB_EPO`, `DOCDB_PAJ`, `INPADOC`, `LENS`, `UNKNOWN`
##### Prosecution Stage
`FILING`,`EXAMINATION`,`PRE_GRANT_CHALLENGE`,`GRANT,POST_GRANT_CHALLENGE`,`INACTIVE`,`TERMINATION`
-->

---

## Sample Patent Record

```json
{
  "lens_id": "008-525-073-655-546",
  "jurisdiction": "EP",
  "pub_key": "EP_1944033_A2",
  "pub_date": "2008-07-16",
  "filing_key": "EP_07022824_A_20011121",
  "filing_date": "2001-11-21",
  "type": "Patent Application",
  "inventor": [
    "KUNZ MARKWART",
    "MUNIR MOHAMMAD",
    "VOGEL MANFRED"
  ],
  "applicant": [
    "NUTRICIA NV"
  ],
  "owner": [],
  "classification_cpc": [
    "C12Y301/01011",
    "A23L29/231",
    "A61K31/732",
    "C08B37/0045",
    "C12P19/04",
    "C12Y302/01015",
    "C12Y402/0201"
  ],
  "classification_ipc": [
    "A23K1/16",
    "A61K31/732",
    "A23B4/00",
    "A23L29/231",
    "A61P1/12",
    "A61P31/04",
    "A61P35/00",
    "A61P35/02",
    "A61P35/04",
    "A61P37/08",
    "A61P43/00",
    "C08B37/00",
    "C08B37/06",
    "C12P19/04",
    "C12P19/14"
  ],
  "classification_us": [],
  "npl_cit": [
    {
      "cit_text": "RAZ; LOTAN, CANCER METASTASIS REV., vol. 6, 1987, pages 433"
    },
    {
      "cit_text": "CANCER RESEARCH, vol. 48, 1988, pages 6933 - 6937"
    },
    {
      "cit_text": "KESTER ET AL., J. BIOL. CHEM., vol. 274, 1999, pages 37053 - 37059"
    },
    {
      "cit_text": "ENDRESS ET AL., LEBENSM.-WISS. U. -TECHNOL., vol. 24, 1991, pages 80 - 85"
    }
  ],
  "family": {
    "simple": {
      "lens_id": [
        "195-080-781-069-750",
        "164-658-285-491-42X",
        "189-163-739-442-204",
        "072-032-313-269-851"
      ],
      "size": 43
    },
    "extended": {
      "lens_id": [
        "195-080-781-069-750",
        "164-658-285-491-42X",
        "056-142-840-402-420",
        "083-375-113-340-231"
      ],
      "size": 43
    }
  },
  "title": [
    {
      "lang": "DE",
      "text": "Verwendung von Pektinhydrolyseprodukten"
    },
    {
      "lang": "EN",
      "text": "Use of pectin hydrolysis products"
    },
    {
      "lang": "FR",
      "text": "Utilisation de produits d'hydrolyse de pectine"
    }
  ],
  "abstract": [
    {
      "lang": "EN",
      "text": "Pectin hydrolysis products are produced by the two-stage hydrolysis of a pectin or pectin-containing plant material with pectin-hydrolysing enzymes. Production of pectin hydrolysis products comprises: (a) treatment of a pectin or pectin-containing plant material in aqueous solution or suspension with a pectin-hydrolysing enzyme (A); and (b) treatment of the product with a pectin-hydrolysing enzyme (B). The products obtained contain galacturonides with at least one 4,5-unsaturated galacturonic acid molecule and are esterified with methanol to >= 20%. An independent claim is also included for a pharmaceutical or dietetic preparation containing the pectin hydrolysis products and a carrier. ACTIVITY : Antibacterial. No data is given. MECHANISM OF ACTION : None given in the source material."
    },
    {
      "lang": "DE",
      "text": "Die vorliegende Erfindung betrifft die Verwendung eines Pektinhydrolyseprodukts, das zumindest ein ungesättigtes Galakturonsäuremolekül enthält und mit Methanol zu >= 20% verestert ist, für die Prophylaxe und Therapie von Infektionskrankheiten, Vergiftungen und Allergien."
    }
  ],
  "pat_cit": [
    {
      "pub_key": "US_5834442_A",
      "lens_id": "172-621-027-075-635"
    },
    {
      "pub_key": "EP_0716605_B1",
      "lens_id": "118-962-823-688-691"
    },
    {
      "pub_key": "WO_1995_007084_A1",
      "lens_id": "102-644-968-906-309"
    }
  ]
}
```

[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
