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
**lang** | Language | The original language of the patent document. | `EN`
**biblio** | [Bibliographic Data](#bibliographic-data) |  | 
**families** | [Families](#families) |  | 
**abstract** | List of [Abstract](#abstract) | The patent document abstract text. | 
**claims** | List of [Claims](#claims) | The Claims recorded in the patent. | 
**description** | [Description](#description) | The description text of the patent document. | 
**legal_status** | [Legal Status Information](#legal-status-information) | The legal Status Information for the patent document. | 
{: .param-def }

### Bibliographic Data

 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**publication_reference** | [Document Id](#document-id) | The publication reference document Id. | 
**application_reference** | [Document Id](#document-id) | The application reference document Id. | 
**priority_claims** | [Priority Claims](#priority-claims) | The priotrity claims documents. | 
**invention_title** | List of [Title](#title) | Title of the patent / invention. | 
**parties** | [Parties](#parties) | The parties associated with the patent (applicants, inventors, owners, agents, etc.)  | 
**classifications_cpc** | [CPC Classifications](#cpc-classifications) | CPC Classifications | 
**classifications_ipcr** | [IPCR Classifications](#ipcr-classifications) | IPCR Classifications | 
**classifications_national** | [US Classifications](#us-classifications) | US Classifications | 
**references_cited** | [References Cited](#references-cited) | The references cited in the patent document (patents and non-patent literature). | 
**cited_by** | [Cited By](#cited-by) | The patents citing the patent document. | 

### Families

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**simple_family** | [Simple Family](#simple-family) | Simple patent family (based on [DOCDB simple patent family](https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/patent-families/docdb.html)). | 
**extended_family** | [Extended Family](#extended-family) | Extended patent family (based on [INPADOC extended patent family](https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/patent-families/inpadoc.html)). |   

### Simple Family

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**members** | List of [Simple Family Members](#simple-family-members) | List of simple family members. | 

### Simple Family Members

Field  |  Type  |  Description |  Example
--------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | Simple family member document Id.  | 
**lens_id** | LensId | Simple family member Lens Id.  | `186-488-232-022-055`

### Extended Family
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**members** | List of [Extended Family Members](#extended-family-members) | List of extended family members. | 

### Extended Family Members
 Field  |  Type  |  Description |  Example
 --------  |  ---------  |  ------- |  -------
**document_id** | [Document Id](#document-id) | Extended family member document Id.  | 
**lens_id** | LensId | Extended family member Lens Id.  | `186-488-232-022-055`
























#### title

 Field | Type |  Description | Example
------- |:------| -------|---------
**lang** | string | Two letter ISO country code representing the language of the associated text | `EN`
**text** | string | The title text | 
{: .param-def }

#### abstract

 Field | Type |  Description  | Example
------- |:------| -------|---------
**lang** | string | Two letter ISO country code representing the language of the associated text | `DE`
**text** | string | The abstract text | 
{: .param-def }

#### family 

 Field | Type |  Description | Example
------- |:------| -------|---------
**type** | string | simple | extended | `simple`
**size** | integer | patent family size | `43`
**lens_id** | array of strings | patent publication Lens IDs of family members | `"195-080-781-069-750"`
{: .param-def }

#### pat_cit

 Field | Type |  Description | Example
------- |:------| -------|---------
**pub_key** | string | patent natural key | `"US_5834442_A"`
**lens_id** | string | patent Lens ID - may be null if the natural key for the citation is not resolved | `"172-621-027-075-635"`
{: .param-def }

#### npl_cit

 Field | Type |  Description | Example
------- |:------| -------|---------
**cit_text** | string | citation free text string in the original form | `"W.C. Birtwell, et al., "The evolution of counterpulsation techniques", Medical Instrumentation, vol. 10, No. 5, Sep.-Oct. 1976."`
{: .param-def }



### Sample Patent Record
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
        // ...
        "189-163-739-442-204",
        "072-032-313-269-851"
      ],
      "size": 43
    },
    "extended": {
      "lens_id": [
        "195-080-781-069-750",
        "164-658-285-491-42X",
         // ...
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
