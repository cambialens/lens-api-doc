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
            "patent_citations": [
                {
                    "lens_id": "025-968-418-263-556"
                }
            ],
            "patent_citations_count": 1,
            "lens_id": "016-246-580-034-670",
            "created": "2018-05-12T12:35:22.055000+00:00",
            "open_access": {
                "license": "cc-by-nc-sa",
                "colour": "hybrid"
            },
            "publication_type": "journal article",
            "publication_supplementary_type": [
                "clinical trial, phase iii",
                "multicenter study",
                "randomized controlled trial",
                "research support, n.i.h., extramural"
            ],
            "authors": [
                {
                    "first_name": "S.",
                    "last_name": "Engebretson",
                    "initials": "S",
                    "affiliations": [
                        {
                            "name": "aNew York University, College of Dentistry, New York, New York 10010, United States",
                            "grid": {
                                "id": "grid.21100.32",
                                "addresses": [
                                    {
                                        "country_code": "CA"
                                    }
                                ]
                            },
                            "institution": "York University"
                        }
                    ]
                },
                {
                    "first_name": "Marie C.",
                    "last_name": "Gelato",
                    "initials": "MC",
                    "affiliations": [
                        {
                            "name": "bStony Brook Medicine, Stony Brook, New York 11794, United States",
                            "grid": {
                                "id": "grid.36425.36",
                                "addresses": [
                                    {
                                        "country_code": "US"
                                    }
                                ]
                            },
                            "institution": "Stony Brook University"
                        }
                    ]
                },
                {
                    "first_name": "Leslie",
                    "last_name": "Hyman",
                    "initials": "L",
                    "affiliations": [
                        {
                            "name": "bStony Brook Medicine, Stony Brook, New York 11794, United States",
                            "grid": {
                                "id": "grid.36425.36",
                                "addresses": [
                                    {
                                        "country_code": "US"
                                    }
                                ]
                            },
                            "institution": "Stony Brook University"
                        }
                    ]
                },
                {
                    "first_name": "Bryan S.",
                    "last_name": "Michalowicz",
                    "initials": "BS",
                    "affiliations": [
                        {
                            "institution": "cUniversity of Minnesota, School of Dentistry, Minneapolis, Minnesota 55455, United States"
                        }
                    ]
                },
                {
                    "first_name": "Elinor",
                    "last_name": "Schoenfeld",
                    "initials": "E",
                    "affiliations": [
                        {
                            "name": "bStony Brook Medicine, Stony Brook, New York 11794, United States",
                            "grid": {
                                "id": "grid.36425.36",
                                "addresses": [
                                    {
                                        "country_code": "US"
                                    }
                                ]
                            },
                            "institution": "Stony Brook University"
                        }
                    ]
                }
            ],
            "title": "Design features of the Diabetes and Periodontal Therapy Trial (DPTT): A multicenter randomized single-masked clinical trial testing the effect of nonsurgical periodontal therapy on glycosylated hemoglobin (HbA1c) levels in subjects with type 2 diabetes and chronic periodontitis ☆☆",
            "volume": "36",
            "issue": "2",
            "languages": [
                "en"
            ],
            "references": [
                {
                    "lens_id": "000-902-678-418-666"
                },
                {
                    "lens_id": "009-477-839-313-148"
                },
                {
                    "lens_id": "009-666-259-811-864"
                },
                {
                    "lens_id": "010-191-520-208-428"
                },
                {
                    "lens_id": "010-950-058-400-675"
                },
                {
                    "lens_id": "012-982-306-980-242"
                },
                {
                    "lens_id": "013-265-576-671-217"
                },
                {
                    "lens_id": "014-287-574-456-744"
                },
                {
                    "lens_id": "015-129-896-126-919"
                },
                {
                    "lens_id": "016-945-336-786-312"
                },
                {
                    "lens_id": "019-057-352-639-973"
                },
                {
                    "lens_id": "019-384-628-907-990"
                },
                {
                    "lens_id": "020-346-139-119-115"
                },
                {
                    "lens_id": "022-506-837-457-704"
                },
                {
                    "lens_id": "025-826-220-021-523"
                },
                {
                    "lens_id": "025-826-423-380-649"
                },
                {
                    "lens_id": "032-149-436-621-702"
                },
                {
                    "lens_id": "032-255-849-587-599"
                },
                {
                    "lens_id": "032-968-019-888-86X"
                },
                {
                    "lens_id": "034-494-676-639-653"
                },
                {
                    "lens_id": "035-069-835-132-673"
                },
                {
                    "lens_id": "035-254-547-454-998"
                },
                {
                    "lens_id": "035-391-010-028-826"
                },
                {
                    "lens_id": "036-613-302-127-532"
                },
                {
                    "lens_id": "039-120-288-830-996"
                },
                {
                    "lens_id": "039-812-193-186-154"
                },
                {
                    "lens_id": "045-391-408-939-534"
                },
                {
                    "lens_id": "045-579-901-866-185"
                },
                {
                    "lens_id": "047-021-495-077-374"
                },
                {
                    "lens_id": "047-426-047-421-683"
                },
                {
                    "lens_id": "053-788-592-360-316"
                },
                {
                    "lens_id": "057-541-052-735-43X"
                },
                {
                    "lens_id": "064-203-426-129-672"
                },
                {
                    "lens_id": "064-364-121-353-339"
                },
                {
                    "lens_id": "066-005-342-898-218"
                },
                {
                    "lens_id": "067-585-773-724-13X"
                },
                {
                    "lens_id": "072-191-146-155-862"
                },
                {
                    "lens_id": "072-822-443-374-189"
                },
                {
                    "lens_id": "077-466-318-602-799"
                },
                {
                    "lens_id": "079-019-130-486-78X"
                },
                {
                    "lens_id": "082-444-465-200-590"
                },
                {
                    "lens_id": "085-670-698-198-828"
                },
                {
                    "lens_id": "087-880-348-023-057"
                },
                {
                    "lens_id": "097-827-472-332-949"
                },
                {
                    "lens_id": "099-608-242-925-709"
                },
                {
                    "lens_id": "105-575-000-819-839"
                },
                {
                    "lens_id": "107-854-826-094-226"
                },
                {
                    "lens_id": "135-663-758-084-002"
                },
                {
                    "lens_id": "152-697-260-272-147"
                },
                {
                    "lens_id": "153-559-208-836-807"
                },
                {
                    "lens_id": "155-740-379-756-202"
                },
                {
                    "lens_id": "168-887-895-981-383"
                },
                {
                    "lens_id": "168-977-715-566-705"
                },
                {
                    "lens_id": "169-526-631-599-773"
                },
                {
                    "lens_id": "177-200-440-164-742"
                },
                {
                    "lens_id": "191-839-173-722-782"
                },
                {
                    "lens_id": "198-731-392-080-45X"
                }
            ],
            "keywords": [
                "Diabetes mellitus",
                "Glycosylated hemoglobin",
                "HbA1c",
                "Periodontal disease",
                "Periodontitis",
                "Type 2"
            ],
            "mesh_terms": [
                {
                    "mesh_heading": "Blood Glucose",
                    "qualifier_name": "analysis",
                    "mesh_id": "D001786",
                    "qualifier_id": "Q000032"
                },
                {
                    "mesh_heading": "Clinical Protocols",
                    "mesh_id": "D002985"
                },
                {
                    "mesh_heading": "Diabetes Mellitus, Type 2",
                    "qualifier_name": "blood",
                    "mesh_id": "D003924",
                    "qualifier_id": "Q000097"
                },
                {
                    "mesh_heading": "Glycated Hemoglobin A",
                    "qualifier_name": "analysis",
                    "mesh_id": "D006442",
                    "qualifier_id": "Q000032"
                },
                {
                    "mesh_heading": "Humans",
                    "mesh_id": "D006801"
                },
                {
                    "mesh_heading": "Mouthwashes",
                    "qualifier_name": "therapeutic use",
                    "mesh_id": "D009067",
                    "qualifier_id": "Q000627"
                },
                {
                    "mesh_heading": "Periodontitis",
                    "qualifier_name": "blood",
                    "mesh_id": "D010518",
                    "qualifier_id": "Q000097"
                },
                {
                    "mesh_heading": "Severity of Illness Index",
                    "mesh_id": "D012720"
                },
                {
                    "mesh_heading": "Single-Blind Method",
                    "mesh_id": "D016037"
                }
            ],
            "chemicals": [
                {
                    "substance_name": "Blood Glucose",
                    "registry_number": "0",
                    "mesh_id": "D001786"
                },
                {
                    "substance_name": "Glycated Hemoglobin A",
                    "registry_number": "0",
                    "mesh_id": "D006442"
                },
                {
                    "substance_name": "Mouthwashes",
                    "registry_number": "0",
                    "mesh_id": "D009067"
                },
                {
                    "substance_name": "hemoglobin A1c protein, human",
                    "registry_number": "0",
                    "mesh_id": "C517652"
                }
            ],
            "clinical_trials": [
                {
                    "id": "nct00997178",
                    "registry": "10.18810/clinical-trials-gov"
                }
            ],
            "fields_of_study": [
                "Internal medicine",
                "Randomized controlled trial",
                "Physical therapy",
                "Dentistry",
                "Randomization",
                "Type 2 diabetes",
                "Chronic periodontitis",
                "Scaling and root planing",
                "Periodontitis",
                "Type 2 Diabetes Mellitus",
                "Clinical trial",
                "Medicine"
            ],
            "funding": [
                {
                    "org": "NIDCR NIH HHS",
                    "funding_id": "U01 DE018886",
                    "country": "United States"
                },
                {
                    "org": "NIDCR NIH HHS",
                    "funding_id": "U01 DE018902",
                    "country": "United States"
                },
                {
                    "org": "NIDCR NIH HHS",
                    "funding_id": "UO1 DE018902",
                    "country": "United States"
                }
            ],
            "source_urls": [
                {
                    "url": "http://www.sciencedirect.com/science/article/pii/S1551714413001614"
                },
                {
                    "type": "unknown",
                    "url": "http://europepmc.org/abstract/MED/24080100"
                },
                {
                    "type": "unknown",
                    "url": "http://www.contemporaryclinicaltrials.com/article/S1551-7144(13)00161-4/abstract"
                },
                {
                    "type": "html",
                    "url": "http://europepmc.org/articles/PMC3885354"
                },
                {
                    "type": "html",
                    "url": "https://nyuscholars.nyu.edu/en/publications/design-features-of-the-diabetes-and-periodontal-therapy-trial-dpt"
                },
                {
                    "type": "html",
                    "url": "https://www.ncbi.nlm.nih.gov/pubmed/24080100"
                },
                {
                    "type": "html",
                    "url": "https://www.sciencedirect.com/science/article/pii/S1551714413001614"
                },
                {
                    "type": "pdf",
                    "url": "http://www.preserveyourteeth.com/forms/publications/Design_Features_DPTT_b_25.pdf"
                },
                {
                    "type": "core_fulltext",
                    "url": "https://core.ac.uk/download/pdf/82325678.pdf"
                }
            ],
            "abstract": "Abstract Background Evidence suggests that periodontitis is associated with prevalent and incident type 2 diabetes mellitus (T2DM), raising the question of whether periodontitis treatment may improve glycemic control in patients with T2DM. Meta-analyses of mostly small clinical trials suggest that periodontitis treatment results in a modest reduction in glycosylated hemoglobin (Hb) A1c. Purpose The purpose of the Diabetes and Periodontal Therapy Trial (DPTT) was to determine if periodontal treatment reduces HbA1c in patients with T2DM and periodontitis. Methods DPTT was a phase-III, single-masked, multi-center, randomized trial with a planned enrollment of 600 participants. Participants were randomly assigned to receive periodontal treatment immediately (Treatment Group) or after 6 months (Control Group). HbA1c values and clinical periodontal measures were determined at baseline and 3 and 6 months following randomization. Medication usage and dosing were assessed at each visit. Periodontal treatment consisted of scaling and root planing for a minimum of two 90-minute sessions, plus the use of an antibacterial mouth rinse for at least 32 days afterwards. The primary outcome was change in HbA1c from baseline to 6 months and the trial was powered to detect a between-group difference of 0.6%. Secondary outcomes included changes in periodontal clinical measures, fasting plasma glucose, the Homeostasis Model Assessment (HOMA2) and the need for rescue diabetes or periodontal therapy. Conclusion Dental and medical researchers collaborated to recruit, treat and monitor participants with two chronic diseases to determine if treatment of one condition affects the status of the other.",
            "year_published": 2013,
            "references_count": 57,
            "scholarly_citations_count": 23,
            "external_ids": [
                {
                    "type": "magid",
                    "value": "mag2032032163"
                },
                {
                    "type": "pmid",
                    "value": "24080100"
                },
                {
                    "type": "doi",
                    "value": "10.1016/j.cct.2013.09.010"
                }
            ],
            "start_page": "515",
            "end_page": "526",
            "source": {
                "title": "Contemporary Clinical Trials",
                "type": "Journal",
                "publisher": "Elsevier Inc.",
                "issn": [
                    {
                        "type": "electronic",
                        "value": "15592030"
                    },
                    {
                        "type": "print",
                        "value": "15517144"
                    }
                ],
                "country": "Netherlands",
                "asjc_codes": [
                    "2736",
                    "2700"
                ],
                "asjc_subjects": [
                    "General Medicine",
                    "Pharmacology (medical)"
                ]
            },
            "scholarly_citations": [
                "002-766-214-233-849",
                "003-159-551-789-532",
                "004-611-380-582-565",
                "007-078-510-225-686",
                "020-395-484-049-382",
                "024-934-953-127-749",
                "029-284-280-417-783",
                "031-296-216-724-498",
                "040-793-824-470-544",
                "045-364-961-943-105",
                "047-845-909-326-820",
                "048-165-048-329-129",
                "051-532-781-808-480",
                "056-524-694-788-620",
                "059-524-110-174-668",
                "061-191-783-691-933",
                "074-794-978-605-69X",
                "077-837-872-838-547",
                "078-397-628-071-620",
                "082-627-563-150-664",
                "082-926-428-633-92X",
                "099-584-695-769-442",
                "194-018-966-210-702"
            ],
            "author_count": 5,
            "date_published": "2013-09-27T00:00:00+00:00"
        }
    ],
    "results": 1
}
```

[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>
