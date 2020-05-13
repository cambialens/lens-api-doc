---
layout: page
title: Patent Metadata
permalink: /patent-metadata.html
---
{:.table-contents}
- [Metadata Fields](#metadata-fields)
- [Sample Patent Record](#sample-patent-record)

### Metadata Fields

 Field | Type |  Description  | Example
------- |:------| :------- |---------
**jurisdiction** | string | patent filing jurisdiction | `"WO"`
**lens_id** | string | patent Lens ID | `"008-525-073-655-546"`
**pub_key** | string | patent natural key | `"EP_1944033_A2"`
**title** | array | Array of patent [title](#title) | 
**abstract** | array | Array of patent [abstract](#abstract) | 
**doc_type** | string | patent document type | `"Patent Application"`
**pub_date** | date: yyyy-mm-dd | patent publication date | `"2008-07-16"`
**filing_date** | date: yyyy-mm-dd | patent filing date | `"2001-11-21"`
**filing_key** | string | patent filing key | `"EP_07022824_A_20011121"`
**family** | Array of [family](#family) objects | patent family data for both simple and extended family definitions - see https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/patent-families.html  | 
**applicant** | array of strings | patent applicants | `"NUTRICIA NV"`
**inventor** | array of strings | patent inventors | `"VOGEL MANFRED"`
**owner** | available for US patents | patent owners | `"RAINBOW MEDICAL LTD"`
**classification_us** | array of strings | United States Patent classification codes | 
**classification_cpc** | array of strings | CPC classification codes | `"A61K31/732"`
**pat_cit** | Array of [Cited Patents](#pat_cit) | cited patent publications | 
**npl_cit** | array of [Cited NPL](#npl_cit) objects | non-patent literature citations | 
**description** | array | Array of patent [description](#description). **N.B.** Description is only available for US patents. |
**claims** | array | Array of patent [claims](#claims). **N.B.** Claims are only available for US patents. |
{: .param-def }

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

#### description

 Field | Type |  Description | Example
------- |:------| -------|---------
**lang** | string | Two letter ISO country code representing the language of the associated text | `EN`
**text** | string | The description full text | `"CROSS-REFERENCE TO RELATED APPLICATIONS This application claims the benefit under 35 U.S.C. § 119(e) of U.S. provisional application Ser. No. 62/654,665, filed Apr. 9, 2018...`
{: .param-def }

#### claims

 Field | Type |  Description | Example
------- |:------| -------|---------
**lang** | string | Two letter ISO country code representing the language of the associated text | `EN`
**text** | string | The claims full text | `"1. A method, comprising:\n exposing tissue that comprises lipopigments when in a diseased state to an excitation source, wherein the lipopigments have at least a portion of an autofluorescence spectrum at wavelengths...`
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
  ],
  "description": [
    {
       "lang": "en",
       "text": "CROSS-REFERENCE TO RELATED APPLICATIONS This application claims the benefit under 35 U.S.C. § 119(e) of U.S. provisional application Ser. No. 62/654,665, filed Apr. 9, 2018, the disclosure of which is incorporated by reference in its entir..." // ...
    }
  ],
  "claims": [
    {
       "lang": "en",
        "text": "1. A method, comprising:\n exposing tissue that comprises lipopigments when in a diseased state to an excitation source, wherein the lipopigments have at least a portion of an autofluorescence spectrum at wavelengths..." //...
    }
  ]
}
```

[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
