---
layout: page
title: Patent Response
permalink: /patent-response.html
---
{:.table-contents}
- [Response Fields](#response-fields)
- [Sample API Response](#sample-api-response)

### Patent Fields

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
**pat_cit** |  | cited patent publications | 
**npl_cit** | array of objects | non-patent literature citations | 
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
**lens_id ** | array of strings | patent publication Lens IDs of family members | `"195-080-781-069-750"`
{: .param-def }

#### Reference

 Field | Type |  Description | Example
------- |:------| -------|---------
**lens_id** | String | Unique lens identifier | `071-957-228-698-625`
{: .param-def }

#### Open Access

 Field | Type |  Description | Example
------- |:------| -------|---------
**license** |  String | The Open Access license type | `cc-by`
**colour** |  String | The Open Access colour category | `gold`
{: .param-def }

#### Source

 Field | Type |  Description | Example
------- |:------| -------|---------
**title** |  String | The name of source publication in which the scholarly work appears | `Journal name, Book title, Confernce proceedings`
**type** |  String | Source Type | `Journal`
**publisher** |  String | The publisher of the source publication | `W.B. Saunders Ltd`
**issn** |  Array of Object | The International Standard Serial Number of the source publication, without hyphenation | `[{"value": "10797114"}]`
**country** |  String | The publisher's country | `United Kingdom`
**asjc_codes** |  String | The All Science Journal Classification (ASJC) code | `2735`
**asjc_subjects** |  String | Subject is derived from journals descriptions in Crossref metadata based on the Science Journal Classification Codes | `Pediatrics`
{: .param-def }

#### Mesh Term

 Field | Type |  Description | Example
------- |:------|-------|---------
**mesh_id** | String | MeSH term unique identifier. MeSH terms are the National Library of Medicine’s controlled vocabulary or subject heading list. | `D000293`
**mesh_heading** | String | MeSH terms are the National Library of Medicine’s controlled vocabulary or medical subject headings assigned to PubMed entries. NB MeSH Headings are case sensitive. | `Adolescent`
**qualifier_id** | String | Mesh Term Qualifier ID | `Q000032`
**qualifier_name** | String | Mesh Term Qualifier Name | `analysis`
{: .param-def }

#### Funding

 Field | Type |  Description | Example
------- |:------:| -------|---------
**org** | String | Name of the funding organisation | `NIDCR NIH HHS`
**funding_id** | String | The funding organisation's project identifier | `U01 DE018902`
**country** | String | The country of the funding body | `United States`
{: .param-def }

#### Conference

Field | Type |  Description | Example
------- |:------:| -------|---------
**name** | String | Conference Name | `International Electron Devices Meeting`
**instance** | String | Conference Instance Name | `CHI 1985`
**location** | String | The location of the conference | `Lihue, Kauai, HA, USA`
{: .param-def }

#### Chemical

 Field | Type |  Description | Example
------- |:------:| -------|---------
**mesh_id** | String | MeSH term id | `D000293`
**registry_number** | String | Chemical registration number | `5Q7ZVV76EI`
**substance_name** | String | Substance name | `Antimalarials`
{: .param-def }

#### Clinical Trial

 Field | Type |  Description | Example
 ------- |:------:| ------- |---------
**id** | String | Identifier | `nct00105716`
**registry** | String | Clinical Trial Registry | `10.18810/clinical-trials-gov`
{: .param-def }

#### Source URL

Field | Type |  Description | Example
 ------- |:------:| -------|---------
**type** | String | Source URL Type | `html`
**url** | String | URL String | `http://cds.cern.ch/record/2291692`
{: .param-def }

#### ID

 Field | Type |  Description | Example
------- |:------:| -------|---------
**type** | String | The type/s of external identifiers for the scholarly work | `doi`, `pmid`, `magid`
**value** | String | The external identifier(s) for a scholarly work | `10.1016/s0031-3955(16)34861-1`
{: .param-def }

### Sample API Response
**Request:**
```json
{
  "query":{
  	"match":{"lens_id":"086-713-276-176-892"}
  }
}
```
**Response:**
```json
{
    "total": 1,
    "data": [
        {
            "patent_citations": [
                {
                    "lens_id": "122-064-734-901-067"
                }
            ],
            "patent_citations_count": 1,
            "lens_id": "086-713-276-176-892",
            "created": "2018-05-12T02:39:28.395000+00:00",
            "open_access": {
                "license": "cc-by-nc-nd",
                "colour": "hybrid"
            },
            "publication_type": "journal article",
            "publication_supplementary_type": [
                "clinical trial, phase ii",
                "multicenter study",
                "randomized controlled trial",
                "research support, non-u.s. gov't"
            ],
            "authors": [
                {
                    "collective_name": null,
                    "first_name": "Maha",
                    "last_name": "Hussain",
                    "initials": "M",
                    "affiliations": [
                        {
                            "name": "University of Michigan",
                            "grid_id": "grid.214458.e",
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Dana E.",
                    "last_name": "Rathkopf",
                    "initials": "DE",
                    "affiliations": [
                        {
                            "name": "Memorial Sloan Kettering Cancer Center",
                            "grid_id": "grid.51462.34",
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Glenn",
                    "last_name": "Liu",
                    "initials": "G",
                    "affiliations": [
                        {
                            "name": "University of Wisconsin-Madison",
                            "grid_id": "grid.14003.36",
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Andrew J.",
                    "last_name": "Armstrong",
                    "initials": "AJ",
                    "affiliations": [
                        {
                            "name": "Duke University",
                            "grid_id": "grid.26009.3d",
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Kevin",
                    "last_name": "Kelly",
                    "initials": "K",
                    "affiliations": [
                        {
                            "name": "Thomas Jefferson University",
                            "grid_id": "grid.265008.9",
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Anna C.",
                    "last_name": "Ferrari",
                    "initials": "AC",
                    "affiliations": [
                        {
                            "name": "New York University",
                            "grid_id": "grid.137628.9",
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "John D.",
                    "last_name": "Hainsworth",
                    "initials": "JD",
                    "affiliations": [
                        {
                            "name": "Sarah Cannon Research Institute",
                            "grid_id": "grid.477834.b",
                            "country_code": "GB"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Adarsh",
                    "last_name": "Joshi",
                    "initials": "A",
                    "affiliations": [
                        {
                            "name": "Eli Lilly and Company",
                            "grid_id": "grid.488258.b",
                            "country_code": "IT"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Rebecca R.",
                    "last_name": "Hozak",
                    "initials": "RR",
                    "affiliations": [
                        {
                            "name": "Eli Lilly and Company",
                            "grid_id": "grid.488258.b",
                            "country_code": "IT"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Ling",
                    "last_name": "Yang",
                    "initials": "L",
                    "affiliations": [
                        {
                            "name": "Eli Lilly and Company",
                            "grid_id": "grid.488258.b",
                            "country_code": "IT"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Jonathan D.",
                    "last_name": "Schwartz",
                    "initials": "JD",
                    "affiliations": [
                        {
                            "name": "Eli Lilly and Company",
                            "grid_id": "grid.488258.b",
                            "country_code": "IT"
                        }
                    ]
                },
                {
                    "collective_name": null,
                    "first_name": "Celestia S.",
                    "last_name": "Higano",
                    "initials": "CS",
                    "affiliations": [
                        {
                            "name": "University of Washington",
                            "grid_id": "grid.34477.33",
                            "country_code": "US"
                        }
                    ]
                }
            ],
            "title": "A randomised non-comparative phase II trial of cixutumumab (IMC-A12) or ramucirumab (IMC-1121B) plus mitoxantrone and prednisone in men with metastatic docetaxel-pretreated castration-resistant prostate cancer",
            "volume": "51",
            "issue": "13",
            "languages": [
                "en"
            ],
            "references": [
                {
                    "lens_id": "003-415-704-045-340"
                },
                {
                    "lens_id": "006-027-163-131-418"
                },
                {
                    "lens_id": "007-652-362-542-447"
                },
                {
                    "lens_id": "010-839-632-959-305"
                },
                {
                    "lens_id": "013-690-046-069-453"
                },
                {
                    "lens_id": "015-449-984-502-884"
                },
                {
                    "lens_id": "015-767-931-570-158"
                },
                {
                    "lens_id": "018-245-327-947-052"
                },
                {
                    "lens_id": "020-963-415-260-304"
                },
                {
                    "lens_id": "026-332-934-265-841"
                },
                {
                    "lens_id": "028-101-820-366-93X"
                },
                {
                    "lens_id": "032-523-762-689-478"
                },
                {
                    "lens_id": "037-117-740-052-570"
                },
                {
                    "lens_id": "038-557-040-762-884"
                },
                {
                    "lens_id": "040-239-601-782-040"
                },
                {
                    "lens_id": "042-246-996-698-043"
                },
                {
                    "lens_id": "043-024-349-674-734"
                },
                {
                    "lens_id": "043-201-312-439-671"
                },
                {
                    "lens_id": "046-041-414-632-674"
                },
                {
                    "lens_id": "046-648-350-541-685"
                },
                {
                    "lens_id": "046-852-526-558-260"
                },
                {
                    "lens_id": "054-808-246-993-497"
                },
                {
                    "lens_id": "059-727-763-246-876"
                },
                {
                    "lens_id": "065-982-455-260-233"
                },
                {
                    "lens_id": "069-612-901-254-771"
                },
                {
                    "lens_id": "070-794-057-102-152"
                },
                {
                    "lens_id": "083-233-359-584-62X"
                },
                {
                    "lens_id": "087-375-055-670-659"
                },
                {
                    "lens_id": "087-458-139-690-01X"
                },
                {
                    "lens_id": "090-234-280-758-859"
                },
                {
                    "lens_id": "094-489-992-059-749"
                },
                {
                    "lens_id": "095-400-716-937-253"
                },
                {
                    "lens_id": "096-654-301-744-608"
                },
                {
                    "lens_id": "101-625-667-760-940"
                },
                {
                    "lens_id": "113-073-836-369-700"
                },
                {
                    "lens_id": "128-335-721-572-401"
                },
                {
                    "lens_id": "155-152-241-876-905"
                }
            ],
            "keywords": [
                "Cixutumumab",
                "Mitoxantrone",
                "Prednisone",
                "Prostate cancer",
                "Ramucirumab"
            ],
            "mesh_terms": [
                {
                    "mesh_heading": "Adenocarcinoma",
                    "qualifier_name": "drug therapy",
                    "mesh_id": "D000230",
                    "qualifier_id": "Q000188"
                },
                {
                    "mesh_heading": "Adolescent",
                    "mesh_id": "D000293"
                },
                {
                    "mesh_heading": "Adult",
                    "mesh_id": "D000328"
                },
                {
                    "mesh_heading": "Aged",
                    "mesh_id": "D000368"
                },
                {
                    "mesh_heading": "Antibodies, Monoclonal",
                    "qualifier_name": "administration & dosage",
                    "mesh_id": "D000911",
                    "qualifier_id": "Q000008"
                },
                {
                    "mesh_heading": "Antineoplastic Combined Chemotherapy Protocols",
                    "qualifier_name": "adverse effects",
                    "mesh_id": "D000971",
                    "qualifier_id": "Q000009"
                },
                {
                    "mesh_heading": "Disease Progression",
                    "mesh_id": "D018450"
                },
                {
                    "mesh_heading": "Disease-Free Survival",
                    "mesh_id": "D018572"
                },
                {
                    "mesh_heading": "Docetaxel",
                    "mesh_id": "D000077143"
                },
                {
                    "mesh_heading": "Humans",
                    "mesh_id": "D006801"
                },
                {
                    "mesh_heading": "Kaplan-Meier Estimate",
                    "mesh_id": "D053208"
                },
                {
                    "mesh_heading": "Male",
                    "mesh_id": "D008297"
                },
                {
                    "mesh_heading": "Middle Aged",
                    "mesh_id": "D008875"
                },
                {
                    "mesh_heading": "Mitoxantrone",
                    "qualifier_name": "administration & dosage",
                    "mesh_id": "D008942",
                    "qualifier_id": "Q000008"
                },
                {
                    "mesh_heading": "Prednisone",
                    "qualifier_name": "administration & dosage",
                    "mesh_id": "D011241",
                    "qualifier_id": "Q000008"
                },
                {
                    "mesh_heading": "Proportional Hazards Models",
                    "mesh_id": "D016016"
                },
                {
                    "mesh_heading": "Prostatic Neoplasms, Castration-Resistant",
                    "qualifier_name": "drug therapy",
                    "mesh_id": "D064129",
                    "qualifier_id": "Q000188"
                },
                {
                    "mesh_heading": "Taxoids",
                    "qualifier_name": "therapeutic use",
                    "mesh_id": "D043823",
                    "qualifier_id": "Q000627"
                },
                {
                    "mesh_heading": "Time Factors",
                    "mesh_id": "D013997"
                },
                {
                    "mesh_heading": "Treatment Outcome",
                    "mesh_id": "D016896"
                },
                {
                    "mesh_heading": "United States",
                    "mesh_id": "D014481"
                },
                {
                    "mesh_heading": "Young Adult",
                    "mesh_id": "D055815"
                }
            ],
            "chemicals": [
                {
                    "substance_name": "Antibodies, Monoclonal",
                    "registry_number": "0",
                    "mesh_id": "D000911"
                },
                {
                    "substance_name": "Taxoids",
                    "registry_number": "0",
                    "mesh_id": "D043823"
                },
                {
                    "substance_name": "anti-IGF-1R antibody A12",
                    "registry_number": "0",
                    "mesh_id": "C557414"
                },
                {
                    "substance_name": "Docetaxel",
                    "registry_number": "15H5577CQD",
                    "mesh_id": "D000077143"
                },
                {
                    "substance_name": "Mitoxantrone",
                    "registry_number": "BZ114NVM5P",
                    "mesh_id": "D008942"
                },
                {
                    "substance_name": "ramucirumab",
                    "registry_number": "D99YVK4L0X",
                    "mesh_id": "C543333"
                },
                {
                    "substance_name": "Prednisone",
                    "registry_number": "VB0R961HZT",
                    "mesh_id": "D011241"
                }
            ],
            "clinical_trials": [
                {
                    "id": "nct00683475",
                    "registry": "10.18810/clinical-trials-gov"
                }
            ],
            "fields_of_study": [
                "M.2",
                "Immunology",
                "Cixutumumab",
                "Prednisone",
                "Ramucirumab",
                "Prostate cancer",
                "Mitoxantrone",
                "Docetaxel",
                "Regimen",
                "Medicine"
            ],
            "funding": [
                {
                    "org": "NCI NIH HHS",
                    "funding_id": "P30 CA008748",
                    "country": "United States"
                }
            ],
            "source_urls": [
                {
                    "type": "unknown",
                    "url": "http://www.ejcancer.com/article/S0959-8049(15)00450-5/pdf"
                },
                {
                    "type": "html",
                    "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5024789/"
                },
                {
                    "type": "html",
                    "url": "https://www.scholars.northwestern.edu/en/publications/a-randomised-non-comparative-phase-ii-trial-of-cixutumumab-imc-a1"
                },
                {
                    "type": "html",
                    "url": "https://www.sciencedirect.com/science/article/pii/S0959804915004505"
                },
                {
                    "type": "core_fulltext",
                    "url": "https://core.ac.uk/download/pdf/82196673.pdf"
                }
            ],
            "abstract": "Abstract Background Cixutumumab, a human monoclonal antibody (HuMAb), targets the insulin-like growth factor receptor. Ramucirumab is a recombinant HuMAb that binds to vascular endothelial growth factor receptor-2. A non-comparative randomised phase II study evaluated cixutumumab or ramucirumab plus mitoxantrone and prednisone (MP) in metastatic castration-resistant prostate cancer (mCRPC). Patients and methods Men with progressive mCRPC during or after docetaxel therapy received mitoxantrone 12 mg/m 2 on day 1 and prednisone 5 mg twice daily and were randomised 1:1 to receive either cixutumumab or ramucirumab 6 mg/kg intravenously weekly in a 21-day cycle. Primary end-point was composite progression-free survival (cPFS). Secondary end-points included safety, response, radiographic progression-free survival (PFS) and overall survival (OS). Sample size was based on a 50% increase in median cPFS from 2.6 (MP) to 3.9 months (either combination). Results 132 men were treated (66 per arm). Median cPFS was 4.1 months (95% confidence interval (CI), 2.2–5.6) for cixutumumab and 6.7 months (95% CI, 4.5–8.3) for ramucirumab. Median time to radiographic progression was 7.5 months for cixutumumab and 10.2 months for ramucirumab, with a median OS of 10.8 and 13.0 months, respectively. Fatigue was the most frequent adverse event (AE). Incidence of most non-haematologic grade 3–4 AEs was Conclusion Combinations of cixutumumab or ramucirumab plus MP were feasible and associated with moderate toxicities in docetaxel-pretreated men with mCRPC. Of the two regimens, the ramucirumab regimen is worthy of further testing based on the observed cPFS relative to the historical control.",
            "year_published": 2015,
            "references_count": 37,
            "scholarly_citations_count": 10,
            "external_ids": [
                {
                    "type": "magid",
                    "value": "2113210954"
                },
                {
                    "type": "pmid",
                    "value": "26082390"
                },
                {
                    "type": "doi",
                    "value": "10.1016/j.ejca.2015.05.019"
                }
            ],
            "start_page": "1714",
            "end_page": "1724",
            "source": {
                "title": "European Journal of Cancer",
                "type": "Journal",
                "publisher": "Elsevier BV",
                "issn": [
                    {
                        "value": "09598049"
                    }
                ],
                "country": "United Kingdom",
                "asjc_codes": [
                    "1306",
                    "2730"
                ],
                "asjc_subjects": [
                    "Oncology",
                    "Cancer Research"
                ]
            },
            "scholarly_citations": [
                "000-201-187-558-654",
                "026-107-871-228-662",
                "028-262-672-178-175",
                "030-115-779-382-725",
                "035-630-845-016-108",
                "037-016-998-061-439",
                "062-343-220-167-149",
                "067-043-485-486-441",
                "145-126-752-104-913",
                "174-636-795-252-301"
            ],
            "author_count": 12,
            "date_published": "2015-06-13T00:00:00+00:00"
        }
    ],
    "results": 1
}
```

[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
