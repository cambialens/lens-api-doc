---
layout: post-sidebar
title: Scholar Response
permalink: /response-scholar.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Response Fields
        url: response-scholar.html#response-fields
      - page: Sample API Response
        url: response-scholar.html#sample-api-response
---

### Response Fields

 Field | Type |  Description  | Example
------- |:------| :------- |---------
 **patent_citations** | Array of [Patent Citation](#patent-citation) | Referenced by patents |  |
 **patent_citations_count** | Integer | Number of patent citations | `10`
 **lens_id** | String | Unique lens identifier | `100-004-910-081-14X`
 **created** | Date | Record created date | `2016-08-01T00:00:00+00:00`
 **publication_type** | String | Publication Type | `journal article`
 **publication_supplementary_type** | Array of String | Supplementary publication type | `["review"]`
 **authors** | Array of [Author](#author) | Authors| |
 **title** | String | Title of the scholarly work | `Malaria`
 **external_ids** | Array of [Ids](#ids) | The external identifier(s) for a scholarly work (DOI, PubMed ID, PubMed Central ID, Microsoft Academic ID or CORE) | |
 **start_page** | String | Start page | `893`
 **end_page** | String | End page | `916`
 **volume** | String | Volume | `32`
 **issue** | String | Issue | `4`
 **languages** | Array of String | Languages | `["en"]`
 **references** | List of [Reference](#reference) | References |  |
 **scholarly_citations** | List of Lens Ids | Scholarly Citations  | `["091-720-300-990-437"]`
 **chemicals** | List of [Chemical](#chemical) | Chemicals |  |
 **clinical_trials** | List of [Clinical Trial](#clinical-trial) | Clinical Trials |  |
 **fields_of_study** | List of String |Fields Of Study | `["Immunology", "Malaria"]`
 **source_urls** | List of [Source URL](#source-url) | Source Urls |
 **abstract** | String | Scholarly work abstract text |
 **date_published** | Date | Date of publication | `2009-05-22`
 **date_published_parts** | Array of Integer | Consist of year, month and day | `[1974, 1, 6]`
 **year_published** | Integer | Year of publication | `1986`
 **conference** | [Conference](#conference) | The conference instance or edition |
 **author_count** | Integer | Number of Authors | `4`
 **references_count** | Integer | The number of works in the reference list of a scholarly work | `2`
 **scholarly_citations_count** | Integer | The number of scholarly works that cite this scholarly work | `3`
 **open_access** | [Open Access](#open-access) |
 **source** | [Source](#source) | Source publication in which the scholarly work appears |
 **keywords** | Array of String | Keywords |
 **mesh_terms** | Array of [MeSH Term](#mesh-term) | MeSH term |
 **funding** | Array of [Funding](#funding) |  Funding |
{: .param-def }

#### Patent Citation

 Field | Type |  Description | Example
------- |:------| -------|---------
**lens_id** | String | Unique lens identifier | `141-171-521-309-804`
{: .param-def }
#### Author

 Field | Type |  Description  | Example
------- |:------| -------|---------
**collective_name** | String | Author Collective Name |
**first_name** | String | The author's first name | `Alexander`
**last_name** | String | The author's last name | `Kupco`
**initials** | String | Author Initials | `A`
**affiliations** | Array of [Affiliation](#affiliation) | The institution/affiliations associated with Author.
**ids** | Array of [Ids](#ids) | Author's MAG, ORCID identifiers | `[{"type": "magid", "value": "1234567890"}]`
{: .param-def }

#### Affiliation

 Field | Type |  Description | Example
------- |:------| -------|---------
**name** | String | The institution associated with the author affiliations. | `Stony Brook University`
**grid_id** | String | Affiliation grid id. **NB** This field is being deprecated, please use the [ids](#ids) field instead. | `grid.9018.0`
**country_code** | String | Comma separated country codes | `DE`
**ids** | Array of [Ids](#ids) | The external institution identifiers associated with the author's affiliation
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
**issn** | Array of Object | [ISSN](#ISSN) | `[{"value": "10797114"}]`
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

#### ISSN

Field | Type |  Description | Example
------- |:------:| -------|---------
**value** | String | The International Standard Serial Number  | `10797114`
**type** | String | ISSN type | `print`, `electronic`
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

#### Ids

 Field | Type |  Description | Example
------- |:------:| -------|---------
**type** | String | The type/s of external identifiers for the scholarly work, author, institution, etc. | `doi`, `pmid`, `magid`, `orcid`, `grid`, `ror`, etc.
**value** | String | The external identifier(s) for the scholarly work, author, institution, etc. | `10.1016/s0031-3955(16)34861-1`, `0000-0003-3902-2234`, `grid.425957.8`, `056x7d368`, etc.
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
    "data":
    [
        {
            "lens_id": "086-713-276-176-892",
            "title": "A randomised non-comparative phase II trial of cixutumumab (IMC-A12) or ramucirumab (IMC-1121B) plus mitoxantrone and prednisone in men with metastatic docetaxel-pretreated castration-resistant prostate cancer",
            "publication_type": "journal article",
            "year_published": 2015,
            "date_published": "2015-06-13T00:00:00.000000+00:00",
            "date_published_parts":
            [
                2015,
                6,
                13
            ],
            "created": "2018-05-12T02:39:28.395000+00:00",
            "external_ids":
            [
                {
                    "type": "magid",
                    "value": "2113210954"
                },
                {
                    "type": "coreid",
                    "value": "82196673"
                },
                {
                    "type": "pmid",
                    "value": "26082390"
                },
                {
                    "type": "pmcid",
                    "value": "pmc5024789"
                },
                {
                    "type": "doi",
                    "value": "10.1016/j.ejca.2015.05.019"
                }
            ],
            "patent_citations":
            [
                {
                    "lens_id": "122-064-734-901-067"
                }
            ],
            "patent_citations_count": 1,
            "open_access":
            {
                "license": "cc-by-nc-nd",
                "colour": "hybrid"
            },
            "authors":
            [
                {
                    "first_name": "Maha",
                    "last_name": "Hussain",
                    "initials": "M",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2105158973"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "University of Michigan",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "27837315"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.214458.e"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100007270"
                                },
                                {
                                    "type": "ror",
                                    "value": "00jmfr291"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Dana E.",
                    "last_name": "Rathkopf",
                    "initials": "DE",
                    "ids":
                    [
                        {
                            "type": "orcid",
                            "value": "0000-0002-4503-7582"
                        },
                        {
                            "type": "magid",
                            "value": "722834404"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Memorial Sloan Kettering Cancer Center",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "1334819555"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.51462.34"
                                },
                                {
                                    "type": "ror",
                                    "value": "02yrq0923"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Glenn",
                    "last_name": "Liu",
                    "initials": "G",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2133546628"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "University of Wisconsin-Madison",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "135310074"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.14003.36"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100007015"
                                },
                                {
                                    "type": "wikidata",
                                    "value": "q838330"
                                },
                                {
                                    "type": "ror",
                                    "value": "01y2jtd41"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Andrew J.",
                    "last_name": "Armstrong",
                    "initials": "AJ",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2172156363"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Duke University",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "170897317"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.26009.3d"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100006510"
                                },
                                {
                                    "type": "wikidata",
                                    "value": "q168751"
                                },
                                {
                                    "type": "ror",
                                    "value": "00py81415"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Kevin",
                    "last_name": "Kelly",
                    "initials": "K",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2097407452"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Thomas Jefferson University",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "149251103"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.265008.9"
                                },
                                {
                                    "type": "ror",
                                    "value": "00ysqcn41"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Anna C.",
                    "last_name": "Ferrari",
                    "initials": "AC",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2312728207"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "New York University",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "57206974"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.137628.9"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100006732"
                                },
                                {
                                    "type": "wikidata",
                                    "value": "q49210"
                                },
                                {
                                    "type": "ror",
                                    "value": "0190ak572"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "John D.",
                    "last_name": "Hainsworth",
                    "initials": "JD",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2145549068"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Sarah Cannon Research Institute",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "172427033"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.477834.b"
                                },
                                {
                                    "type": "wikidata",
                                    "value": "q30270369"
                                },
                                {
                                    "type": "ror",
                                    "value": "03cp5cj42"
                                }
                            ],
                            "country_code": "GB"
                        }
                    ]
                },
                {
                    "first_name": "Adarsh",
                    "last_name": "Joshi",
                    "initials": "A",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2097035297"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Eli Lilly and Company",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "168537998"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.417540.3"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100004312"
                                },
                                {
                                    "type": "ror",
                                    "value": "01qat3289"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Rebecca R.",
                    "last_name": "Hozak",
                    "initials": "RR",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2182553763"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Eli Lilly and Company",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "168537998"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.417540.3"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100004312"
                                },
                                {
                                    "type": "ror",
                                    "value": "01qat3289"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Ling",
                    "last_name": "Yang",
                    "initials": "L",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2250633597"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Eli Lilly and Company",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "168537998"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.417540.3"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100004312"
                                },
                                {
                                    "type": "ror",
                                    "value": "01qat3289"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Jonathan D.",
                    "last_name": "Schwartz",
                    "initials": "JD",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2155041711"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Eli Lilly and Company",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "168537998"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.417540.3"
                                },
                                {
                                    "type": "fundref",
                                    "value": "100004312"
                                },
                                {
                                    "type": "ror",
                                    "value": "01qat3289"
                                }
                            ],
                            "country_code": "US"
                        }
                    ]
                },
                {
                    "first_name": "Celestia S.",
                    "last_name": "Higano",
                    "initials": "CS",
                    "ids":
                    [
                        {
                            "type": "magid",
                            "value": "2560077320"
                        }
                    ],
                    "affiliations":
                    [
                        {
                            "name": "Fred Hutchinson Cancer Research Center",
                            "ids":
                            [
                                {
                                    "type": "magid",
                                    "value": "1326427960"
                                },
                                {
                                    "type": "grid",
                                    "value": "grid.475296.b"
                                },
                                {
                                    "type": "ror",
                                    "value": "00wdsp051"
                                }
                            ],
                            "country_code": "ZA"
                        }
                    ]
                }
            ],
            "source":
            {
                "title": "European journal of cancer (Oxford, England : 1990)",
                "type": "Journal",
                "publisher": "Elsevier Limited",
                "issn":
                [
                    {
                        "type": "unknown",
                        "value": "18790852"
                    },
                    {
                        "type": "print",
                        "value": "09598049"
                    }
                ],
                "country": "United Kingdom",
                "asjc_codes":
                [
                    "1306",
                    "2730"
                ],
                "asjc_subjects":
                [
                    "Oncology",
                    "Cancer Research"
                ]
            },
            "fields_of_study":
            [
                "Internal medicine",
                "Oncology",
                "Cixutumumab",
                "Prednisone",
                "Ramucirumab",
                "Prostate cancer",
                "Mitoxantrone",
                "Docetaxel",
                "Regimen",
                "Phases of clinical research",
                "Medicine"
            ],
            "keywords":
            [
                "Cixutumumab",
                "Mitoxantrone",
                "Prednisone",
                "Prostate cancer",
                "Ramucirumab"
            ],
            "publication_supplementary_type":
            [
                "clinical trial, phase ii",
                "multicenter study",
                "randomized controlled trial",
                "research support, non-u.s. gov't"
            ],
            "volume": "51",
            "issue": "13",
            "languages":
            [
                "en"
            ],
            "references":
            [
                {
                    "lens_id": "003-415-704-045-340"
                },
                {
                    "lens_id": "006-027-163-131-418"
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
                    "lens_id": "043-546-849-370-25X"
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
            "mesh_terms":
            [
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
                    "mesh_heading": "Antibodies, Monoclonal, Humanized",
                    "mesh_id": "D061067"
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
            "chemicals":
            [
                {
                    "substance_name": "Antibodies, Monoclonal",
                    "registry_number": "0",
                    "mesh_id": "D000911"
                },
                {
                    "substance_name": "Antibodies, Monoclonal, Humanized",
                    "registry_number": "0",
                    "mesh_id": "D061067"
                },
                {
                    "substance_name": "Taxoids",
                    "registry_number": "0",
                    "mesh_id": "D043823"
                },
                {
                    "substance_name": "Docetaxel",
                    "registry_number": "15H5577CQD",
                    "mesh_id": "D000077143"
                },
                {
                    "substance_name": "cixutumumab",
                    "registry_number": "2285XW22DR",
                    "mesh_id": "C557414"
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
            "clinical_trials":
            [
                {
                    "id": "nct00683475",
                    "registry": "10.18810/clinical-trials-gov"
                }
            ],
            "funding":
            [
                {
                    "org": "NCI NIH HHS",
                    "funding_id": "P30 CA008748",
                    "country": "United States"
                }
            ],
            "source_urls":
            [
                {
                    "type": "html",
                    "url": "https://www.scholars.northwestern.edu/en/publications/a-randomised-non-comparative-phase-ii-trial-of-cixutumumab-imc-a1"
                },
                {
                    "type": "html",
                    "url": "https://www.sciencedirect.com/science/article/pii/S0959804915004505"
                },
                {
                    "type": "html",
                    "url": "https://core.ac.uk/display/82196673"
                },
                {
                    "type": "html",
                    "url": "https://www.ncbi.nlm.nih.gov/pubmed/26082390"
                },
                {
                    "type": "html",
                    "url": "https://europepmc.org/abstract/MED/26082390"
                },
                {
                    "type": "html",
                    "url": "https://pubmed.ncbi.nlm.nih.gov/26082390/"
                },
                {
                    "type": "unknown",
                    "url": "https://www.sciencedirect.com/science/article/abs/pii/S0959804915004505#!"
                },
                {
                    "type": "core_fulltext",
                    "url": "https://core.ac.uk/download/pdf/82196673.pdf"
                }
            ],
            "abstract": "Abstract Background Cixutumumab, a human monoclonal antibody  (HuMAb), targets the insulin-like growth factor receptor...",
            "references_count": 36,
            "scholarly_citations_count": 26,
            "start_page": "1714",
            "end_page": "1724",
            "scholarly_citations":
            [
                "000-201-187-558-654",
                "003-526-658-910-015",
                "003-873-121-875-383",
                "007-302-126-599-214",
                "010-213-946-021-323",
                "013-615-059-072-408",
                "013-724-699-030-436",
                "014-223-693-822-29X",
                "018-109-129-610-567",
                "021-609-846-309-864",
                "026-107-871-228-662",
                "026-389-814-274-812",
                "028-262-672-178-175",
                "030-115-779-382-725",
                "035-630-845-016-108",
                "037-016-998-061-439",
                "041-068-995-918-23X",
                "046-312-772-821-709",
                "054-371-103-868-542",
                "055-935-439-115-752",
                "062-343-220-167-149",
                "067-043-485-486-441",
                "085-619-841-835-92X",
                "086-063-652-233-255",
                "145-126-752-104-913",
                "153-500-774-834-922"
            ],
            "author_count": 12,
            "is_open_access": true
        }
    ],
    "results": 1
}
```

[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
