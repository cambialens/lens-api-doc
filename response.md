---
layout: page
title: Response
permalink: /response.html
---
{:.table-contents}
- [Response Fields](#response-fields)
- [Sample API Response](#sample-api-response)

### Response Fields

 Field | Type |  Description  | Example
------- |:------| :------- |---------
 **patent_citations** | Array of [Patent Citation](#patent-citation) | Referenced by patents |  |
 **patent_citation_count** | Integer | Number of patent citations | `10`
 **lens_id** | String | Unique lens identifier | `100-004-910-081-14X`
 **created** | Date | Record created date | `2016-08-01T00:00:00+00:00`
 **publication_type** | String | Publication Type | `report`, `Conference Proceedings`
 **publication_supplementary_type** | Array of String | Supplementary publication type | `review`
 **authors** | Array of [Author](#author) | Authors| |
 **title** | String | Title of the scholarly work | `Malaria`
 **external_ids** | Array of [Id](#id) | The external identifier(s) for a scholarly work (DOI, PubMed ID, PubMed Central ID, Microsoft Academic ID or CORE) | |
 **start_page** | String | Start page | `893`
 **end_page** | String | End page | `916`
 **volume** | String | Volume | `32`
 **issue** | String | Issue | `4`
 **languages** | Array of String | Languages | `["ENG"]`
 **references** | List of [Reference](#reference) | References |  |
 **scholarly_citations** | List of Lens Ids | Scholarly Citations  | `["091-720-300-990-437"]`
 **chemicals** | List of [Chemical](#chemical) | Chemicals |  |
 **clinical_trials** | List of [Clinical Trial](#clinical-trial) | Scholarly Citations |  |
 **fields_of_study** | List of String |Fields Of Study | `["Immunology", "Malaria"]`
 **source_urls** | List of [Source URL](#source-url) | Source Urls |
 **abstract** | String | Scholarly work abstract text |
 **full_text** | String | Full Text |
 **date_published** | Date | Date of publication | `2009-05-22`
 **year_published** | Integer | Year of publication | `1986`
 **conference** | [Conference](#conference) | The conference instance or edition |
 **author_count** | Integer | Number of Authors | `4`
 **reference_count** | Integer | The number of works in the reference list of a scholarly work | `2`
 **scholarly_citation_count** | Integer | The number of scholarly works that cite this scholarly work | `3`
 **open_access** | [Open Access](#open-access) |
 **source** | [Source](#source) | Source publication in which the scholarly work appears |
 **keywords** | Array of String | Keywords |
 **mesh_terms** | Array of [MeSH Term](#mesh-term) | MeSH term |
 **funding** | Array of [Funding](#funding) |  Funding |

#### Patent Citation

 Field | Type |  Description | Example
------- |:------| -------|---------
lens_id | String | Unique lens identifier | `141-171-521-309-804`

#### Author

 Field | Type |  Description  | Example
------- |:------| -------|---------
collective_name | String | Author Collective Name |
first_name | String | The author's first name | `Alexander`
last_name | String | The author's last name | `Kupco`
initials | Integer | Author Initials | `A`
full_name | String | Author's full name | `Alexander Kupco`
affiliations | Array of [Affiliation](#affiliation) | The institution/affiliations associated with Author.

#### Affiliation

 Field | Type |  Description | Example
------- |:------| -------|---------
institution | String | The institution associated with the author affiliations. | `Stony Brook University`
name | String | The author's affiliated institution and address | `Stony Brook Medicine, Stony Brook, New York 11794, United States`
grid | Array of [Grid](#grid) | Affiliation Grid | true |

#### Grid

 Field | Type |  Description | Example
------- |:------| -------|---------
id | String | Affiliation grid id | `grid.9018.0`
country_code | String | Country Code | `DE`

#### Reference

 Field | Type |  Description | Example
------- |:------| -------|---------
lens_id | String | Unique lens identifier | `071-957-228-698-625`

#### Open Access

 Field | Type |  Description | Example
------- |:------| -------|---------
**license** |  String | The Open Access license type | `cc-by`
**colour** |  String | The Open Access colour category | `gold`

#### Source

 Field | Type |  Description | Example
------- |:------| -------|---------
**title** |  String | The name of source publication in which the scholarly work appears | `Journal name, Book title, Confernce proceedings`
**type** |  String | Source Type | `Journal`
**publisher** |  String | The publisher of the source publication | `W.B. Saunders Ltd`
**issn** |  Array of [Id](#id) | The International Standard Serial Number of the source publication, without hyphenation | `00222836`
**country** |  String | The publisher's country | `United Kingdom`
**asjc_codes** |  String | The All Science Journal Classification (ASJC) code | `2735`
**asjc_subjects** |  String | Subject is derived from journals descriptions in Crossref metadata based on the Science Journal Classification Codes | `Pediatrics`

#### Mesh Term

 Field | Type |  Description | Example
------- |:------|-------|---------
mesh_id | String | MeSH term unique identifier. MeSH terms are the National Library of Medicine’s controlled vocabulary or subject heading list. | `D000293`
mesh_heading | String | MeSH terms are the National Library of Medicine’s controlled vocabulary or medical subject headings assigned to PubMed entries. NB MeSH Headings are case sensitive. | `Adolescent`
qualifier_id | String | Mesh Term Qualifier ID | `Q000032`
qualifier_name | String | Mesh Term Qualifier Name | `analysis`

#### Funding

 Field | Type |  Description | Example
------- |:------:| -------|---------
org | String | Name of the funding organisation | `NIDCR NIH HHS`
funding_id | String | The funding organisation's project identifier | `U01 DE018902`
country | String | The country of the funding body | `United States`

#### Conference

Field | Type |  Description | Example
------- |:------:| -------|---------
**name** | String | Conference Name | `International Electron Devices Meeting`
**instance** | String | Conference Instance Name | `CHI 1985`
**location** | String | The location of the conference | `Lihue, Kauai, HA, USA`

#### Chemical

 Field | Type |  Description | Example
------- |:------:| -------|---------
mesh_id | String | MeSH term id | `D000293`
registry_number | String | Chemical registration number | `5Q7ZVV76EI`
substance_name | String | Substance name | `Antimalarials`

#### Clinical Trial

 Field | Type |  Description | Example
 ------- |:------:| ------- |---------
id | String | Identifier | `nct00105716`
registry | String | Clinical Trial Registry | `10.18810/clinical-trials-gov`

#### Source URL

Field | Type |  Description | Example
 ------- |:------:| -------|---------
type | String | Source URL Type | `html`
url | String | URL String | `http://cds.cern.ch/record/2291692`

#### ID

 Field | Type |  Description | Example
------- |:------:| -------|---------
type | String | The type/s of external identifiers for the scholarly work | `doi`, `pmid`, `magid`
value | String | The external identifier(s) for a scholarly work | `10.1016/s0031-3955(16)34861-1`


### Sample API Response
```json
{
    "total": 1,
    "data": [
        {
            "patent_citation_count": 0,
            "lens_id": "057-666-896-534-696",
            "created": "2018-05-15T00:09:53.738000+00:00",
            "open_access": {
                "license": null,
                "colour": "green"
            },
            "publication_type": "journal article",
            "authors": [
                {
                    "first_name": "Luis",
                    "last_name": "Araujo",
                    "initials": "L",
                    "affiliations": [
                        {
                            "name": "Michigan State University, United States of America",
                            "grid": {
                                "id": "grid.17088.36",
                                "addresses": [
                                    {
                                        "country_code": "US"
                                    }
                                ]
                            },
                            "institution": "Michigan State University"
                        }
                    ]
                },
                {
                    "first_name": "Qingqing",
                    "last_name": "Cao",
                    "initials": "Q",
                    "affiliations": [
                        {
                            "name": "Michigan State University, United States of America",
                            "grid": {
                                "id": "grid.17088.36",
                                "addresses": [
                                    {
                                        "country_code": "US"
                                    }
                                ]
                            },
                            "institution": "Michigan State University"
                        }
                    ]
                },
                {
                    "first_name": "Raoul",
                    "last_name": "Minetti",
                    "initials": "R",
                    "affiliations": [
                        {
                            "name": "Michigan State University, United States of America",
                            "grid": {
                                "id": "grid.17088.36",
                                "addresses": [
                                    {
                                        "country_code": "US"
                                    }
                                ]
                            },
                            "institution": "Michigan State University"
                        }
                    ]
                },
                {
                    "first_name": "Pierluigi",
                    "last_name": "Murro",
                    "initials": "P",
                    "affiliations": [
                        {
                            "name": "Luiss University, Italy",
                            "institution": "Libera Università Internazionale degli Studi Sociali Guido Carli"
                        }
                    ]
                }
            ],
            "title": "Credit Crunches, Asset Prices and Technological Change",
            "volume": "32",
            "languages": [
                "en"
            ],
            "references": [
                {
                    "lens_id": "001-928-280-929-804"
                },
                {
                    "lens_id": "004-212-611-699-202"
                },
                {
                    "lens_id": "005-579-458-898-498"
                },
                {
                    "lens_id": "025-101-173-604-591"
                },
                {
                    "lens_id": "028-930-297-640-217"
                },
                {
                    "lens_id": "030-830-714-012-814"
                },
                {
                    "lens_id": "033-145-572-757-637"
                },
                {
                    "lens_id": "035-519-217-675-203"
                },
                {
                    "lens_id": "037-214-630-787-407"
                },
                {
                    "lens_id": "043-987-472-903-151"
                },
                {
                    "lens_id": "045-382-417-479-598"
                },
                {
                    "lens_id": "048-911-230-430-305"
                },
                {
                    "lens_id": "050-136-344-463-858"
                },
                {
                    "lens_id": "052-024-557-155-791"
                },
                {
                    "lens_id": "052-027-687-931-983"
                },
                {
                    "lens_id": "053-833-475-306-927"
                },
                {
                    "lens_id": "054-260-384-126-569"
                },
                {
                    "lens_id": "059-678-079-754-075"
                },
                {
                    "lens_id": "063-258-687-565-263"
                },
                {
                    "lens_id": "063-520-145-129-134"
                },
                {
                    "lens_id": "064-427-081-110-273"
                },
                {
                    "lens_id": "075-157-236-653-865"
                },
                {
                    "lens_id": "078-007-020-651-428"
                },
                {
                    "lens_id": "079-534-575-836-38X"
                },
                {
                    "lens_id": "084-673-955-657-405"
                },
                {
                    "lens_id": "095-221-615-702-697"
                },
                {
                    "lens_id": "097-640-096-741-30X"
                },
                {
                    "lens_id": "102-602-874-145-996"
                },
                {
                    "lens_id": "106-619-997-653-532"
                },
                {
                    "lens_id": "110-125-963-715-074"
                },
                {
                    "lens_id": "111-537-875-984-351"
                },
                {
                    "lens_id": "111-662-072-400-984"
                },
                {
                    "lens_id": "113-015-341-294-246"
                },
                {
                    "lens_id": "119-758-023-750-272"
                },
                {
                    "lens_id": "121-681-440-045-792"
                },
                {
                    "lens_id": "123-516-004-187-587"
                },
                {
                    "lens_id": "126-873-825-670-044"
                },
                {
                    "lens_id": "133-316-086-552-635"
                },
                {
                    "lens_id": "142-182-572-724-856"
                },
                {
                    "lens_id": "149-149-926-117-94X"
                },
                {
                    "lens_id": "149-406-626-016-05X"
                },
                {
                    "lens_id": "156-169-533-070-935"
                },
                {
                    "lens_id": "160-240-870-264-881"
                },
                {
                    "lens_id": "163-931-861-739-824"
                },
                {
                    "lens_id": "171-047-879-244-857"
                },
                {
                    "lens_id": "176-855-425-991-329"
                },
                {
                    "lens_id": "185-169-345-522-588"
                },
                {
                    "lens_id": "193-307-619-919-244"
                },
                {
                    "lens_id": "196-918-085-414-226"
                }
            ],
            "fields_of_study": [
                "Collateral management",
                "Business",
                "Credit risk",
                "Credit crunch",
                "Credit enhancement",
                "Credit derivative",
                "Restructuring",
                "Credit history",
                "Financial system",
                "Credit valuation adjustment"
            ],
            "source_urls": [
                {
                    "type": "html",
                    "url": "https://econpapers.repec.org/RePEc:lui:casmef:1204"
                },
                {
                    "type": "html",
                    "url": "https://ideas.repec.org/a/red/issued/18-267.html"
                },
                {
                    "type": "html",
                    "url": "https://www.sciencedirect.com/science/article/pii/S1094202518302965"
                },
                {
                    "type": "pdf",
                    "url": "http://www.eco.uc3m.es/temp/CreditCrunches.pdf"
                },
                {
                    "type": "pdf",
                    "url": "https://www.chicagofed.org/~/media/others/events/2011/money-banking-payments-finance/araujo-minetti-pdf.pdf"
                }
            ],
            "abstract": "We investigate the effects of a credit crunch in an economy where firms can operate a mature technology or restructure their activity and adopt a new technology. We show that firms’ collateral and credit relationships ease firms’ access to credit and investment but can also inhibit firms’ restructuring. When this occurs, negative collateral or productivity shocks and the resulting drop in the price of collateral assets squeeze collateral-poor firms out of the credit market but foster the restructuring of collateral-rich firms. We characterize conditions under which such an increase in firms’ restructuring occurs within existing credit relationships or through their breakdown. The analysis reveals that the credit and asset market policies adopted during the recent credit crunch can promote investment but might also slow down a process of Shumpeterian restructuring in the credit market.",
            "year_published": 2019,
            "reference_count": 49,
            "scholarly_citation_count": 1,
            "external_ids": [
                {
                    "type": "magid",
                    "value": "mag1605916543"
                },
                {
                    "type": "doi",
                    "value": "10.1016/j.red.2019.02.001"
                }
            ],
            "start_page": "153",
            "end_page": "179",
            "source": {
                "title": "Review of Economic Dynamics",
                "type": "Journal",
                "publisher": "Elsevier BV",
                "issn": [
                    {
                        "type": "print",
                        "value": "10942025"
                    },
                    {
                        "type": "electronic",
                        "value": "10966099"
                    }
                ],
                "country": "United States",
                "asjc_codes": [
                    "2002"
                ],
                "asjc_subjects": [
                    "Economics and Econometrics"
                ]
            },
            "scholarly_citations": [
                "024-902-290-771-501"
            ],
            "author_count": 4,
            "date_published": "2019-04-01T00:00:00+00:00"
        }
    ],
    "results": 1
}
```

[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
