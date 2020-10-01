## Lens Patent API - `Beta`

### Table of Contents
- [Endpoints](#endpoints)
- [Request Structure](#request-structure)
- [Request Fields](#request-fields)
- [Response Fields](#response-fields)
- [Examples](#examples)
- [Sample](#sample-data)

### Endpoints

 - Getting individual patent by Lens Id `GET` `/patent/{lens_id}`
 - Query Using GET Request `GET` `/patent/search?query=...&token={api-token}`
 - Search Using POST Request `POST` `/patent/search`
 
### Request Structure

 The request payload should comply with following `json` schema for POST request.
 
 Fields | Description |  Required
 ------- | ------| -------
 **[query](https://docs.api.lens.org/request.html#supported-query-types)** | Valid json search request | true
 **[sort](https://docs.api.lens.org/request.html#sorting)** | Use available fields to sort results by ascending/descending order. | false
 **[include](https://docs.api.lens.org/request.html#projection)** | Only get specific fields from API response. By default all fields are selected. | false
 **[exclude](https://docs.api.lens.org/request.html#projection)** | Get all fields except undesired ones in search result. | false
 **[size](https://docs.api.lens.org/request.html#pagination)** | Integer value to specify number of items per page | false
 **[from](https://docs.api.lens.org/request.html#pagination)** | Integer value, defines the offset from the first result | false
 **[scroll_id](https://docs.api.lens.org/request.html#pagination)** | Pagination parameter | false (true for next scroll requests)
 **[scroll](https://docs.api.lens.org/request.html#pagination)** | Lifespan of Scroll scroll context in minute (e.g. 1m) | false (true for scroll context)
 
### Request Fields
 Field | Type | Description
 -------- | --------- | -------
 **lens_id** | String | Unique lens identifier e.g. `100-004-910-081-14X`
 **abstract** | String | Patent document abstract
 **applicant.address** | String |  
 **applicant.app_type** | String | 
 **applicant.name** | String |
 **applicant.residence** | String |
 **application_reference.appl_type** | String |
 **application_reference.country** | String |
 **application_reference.date** | Date | `yyyy-MM-dd`
 **application_reference.doc_number** | String |
 **application_reference.kind** | String | 
 **claim** | String | The claims full text
 **classifications_cpc.action_date** | Date | `yyyy-MM-dd`
 **classifications_cpc.classification_data_source** | String | 
 **classifications_cpc.classification_status** | String |
 **classifications_cpc.classification_symbol_position** | String |
 **classifications_cpc.classification_value** | String |
 **classifications_cpc.first_symbol** | String |
 **classifications_cpc.generating_office** | String |
 **classifications_cpc.later_symbol** | String |
 **classifications_cpc.sequence** | String |
 **classifications_cpc.source** | String |
 **classifications_cpc.symbol** | String |
 **classifications_cpc.version_indicator** | String |
 **classifications_ipc.edition** | String |
 **classifications_ipc.later_symbol** | String |
 **classifications_ipc.main_symbol** | String |
 **classifications_ipc.source** | String |
 **classifications_ipc.symbol** | String |
 **classifications_ipc.text** | String |
 **classifications_ipcr.action_date** | Date | `yyyy-MM-dd`
 **classifications_ipcr.classification_data_source** | String |
 **classifications_ipcr.classification_status** | String |
 **classifications_ipcr.classification_symbol_position** | String |
 **classifications_ipcr.classification_value** | String |
 **classifications_ipcr.first_symbol** | String |
 **classifications_ipcr.generating_office** | String |
 **classifications_ipcr.later_symbol** | String |
 **classifications_ipcr.sequence** | String |
 **classifications_ipcr.source** | String |
 **classifications_ipcr.symbol** | String |
 **classifications_ipcr.version_indicator** | String |
 **classifications_national.first_symbol** | String |
 **classifications_national.later_symbol** | String |
 **classifications_national.source** | String |
 **classifications_national.symbol** | String |
 **classifications_national.symbol_position** | String |
 **country** | String |
 **date_published** | Date | `yyyy-MM-dd`
 **description** | String |
 **doc_key** | String |
 **doc_number** | String |
 **has_abstract** | Boolean |
 **has_claim** | Boolean |
 **has_description** | Boolean |
 **has_title** | Boolean |
 **inventor.address** | String |
 **inventor.name** | String |
 **inventor.nationality** | String |
 **inventor.residence** | String |
 **inventor.sequence** | String |
 **kind** | String |
 **language** | String |
 **legal_status.anticipated_term_date** | Date | `yyy-MM-dd`
 **legal_status.application_expiry_date** | Date | `yyy-MM-dd`
 **legal_status.discontinued_date** | Date | `yyy-MM-dd`
 **legal_status.grant_date** | Date | `yyy-MM-dd`
 **legal_status.granted** | Boolean | 
 **legal_status.has_disclaimer** | Boolean | 
 **legal_status.ipr_type** | String | 
 **legal_status.patent_status** | String | 
 **legal_status.prosecution_stage** | String | 
 **legal_status.publication_count** | String | 
 **npl_citation_count** | Integer | 
 **patent_citation_count** | Integer |
 **priority_claim.country** | String |
 **priority_claim.date** | Date | `yyy-MM-dd`
 **priority_claim.doc_number** | String |
 **priority_claim.kind** | String |
 **pub_key** | String |
 **publication_type** | String |
 **reference_cited.npl_citation.category** | String |
 **reference_cited.npl_citation.cited_date** | Date |
 **reference_cited.npl_citation.cited_phase** | String |
 **reference_cited.npl_citation.name** | String |
 **reference_cited.npl_citation.npl_type** | String |
 **reference_cited.npl_citation.num** | String |
 **reference_cited.npl_citation.sequence** | String |
 **reference_cited.npl_citation.srep_office** | String |
 **reference_cited.npl_citation.text** | String |
 **reference_cited.npl_citation.us_category** | String |
 **reference_cited.npl_citation.xp_number** | String |
 **reference_cited.patent_citation.category** | String |
 **reference_cited.patent_citation.cited_date** | Date | `yyy-MM-dd`
 **reference_cited.patent_citation.cited_phase** | String |
 **reference_cited.patent_citation.document_id.country** | String |
 **reference_cited.patent_citation.document_id.date** | Date | `yyy-MM-dd`
 **reference_cited.patent_citation.document_id.doc_number** | String |
 **reference_cited.patent_citation.document_id.kind** | String |
 **reference_cited.patent_citation.document_id.name** | String |
 **reference_cited.patent_citation.name** | String |
 **reference_cited.patent_citation.num** | String |
 **reference_cited.patent_citation.pub_key** | String |
 **reference_cited.patent_citation.sequence** | String |
 **reference_cited.patent_citation.srep_office** | String |
 **reference_cited.patent_citation.us_category** | String |
 **title** | String |
 **year_published** | Integer |
 
### Response Fields
Field | Type | Description
-------- | --------- | -------
**lens_id** | String |
**country** | String |
**doc_number** | String |
**kind** | String |
**date_publ** | Date |
**doc_key** | String |
**biblio** | String |
**kind** | String |
**biblio** | [Bibliographic Data](#bibliographic-data) |
**sequence_listing** | [PatentSequenceListing](#patent-sequence-listing) |
**abstract** | [Abstract](#abstract)
**claims** | List[[Claims](#claims)]
**description** | [Description](#description)
**publication_type** | String | [Document Type](#document-type)
**legal_status** | [Legal Status Information](#legal-status-information)

##### Bibliographic Data
Field | Type | Description
-------- | --------- | -------
**publication_reference** | [Publication Reference](#publication-reference) |
**application_reference** | [Application Reference](#application-reference) |
**priority_claims** | [Priority Claims](#priority-claims) |
**invention_title** | List[[Invention Title](#invention-title)] |
**lang** | String |
**parties** | [Parties](#parties) |
**assignees** | [Assignees](#assignees) |
**examiners** | [Examiners](#examiners) |
**classifications_ipc** | [Classification Ipc](#classification-ipc) |
**classifications_ipcr** | List[[Classification Ipcr](#classification-ipcr)] |
**classifications_cpc** | [Classifications Cpc](#classifications-cpc) |
**classifications_national** | [Classifications National](#classifications-national) |
**references_cited** | [References Cited](#references-cited) |
**npl_citations** | [Patent Npl Citations](#patent-npl-citations) |
**designation_of_states** | [Designation Of States](#designation-of-states) |
**pct_or_regional_filing_data** | [Pct Or Regional Filing Data](#pct-or-regional-filing-data) |
**pct_or_regional_publishing_data** | [Pct Or Regional Publishing Data](#pct-or-regional-publishing-data)
**us_term_of_grant** | [UsTermOfGrant](#us-term-of-grant)

##### Publication Reference
Field | Type | Description
-------- | --------- | -------
**country** | String |
**doc_number** | String |
**kind** | String |
**date** | Date |
**name.value** | String |
**name.name_type** | String | [ `legal`, `natural` ]
**lang** | String |

##### Application Reference
Field | Type | Description
-------- | --------- | -------
**country** | String |
**doc_number** | String |
**kind** | String |
**date** | Date |
**name.value** | String |
**name.name_type** | String | [ `legal`, `natural` ]
**lang** | String |
**appl_type** | String |
**is_representative** | Boolean |

##### Priority Claims
Field | Type | Description
-------- | --------- | -------
**priority_claim** | List[[Priority Claim]](#priority-claim) |
**source** | [Source](#source) | 

##### Priority Claim
Field | Type | Description
-------- | --------- | -------
**country** | [Country](#country) |
**doc_number** | String |
**kind** | String |
**date** | Date |
**office_of_filing** | [Region And Country](#region-and-country) |
**priority_doc_requested** | Boolean | 
**priority_doc_attached** | Boolean |
**sequence** | Integer |
**source** | [Source](#source) | 

##### Claims
-------- | --------- | -------
**claim** | List[Claim](#claim) |
**id** | String |
**lang** | String |
**claim_type** | String |
**status** | String |
**docPage** | List[[Doc Page](#doc-page)] |

##### Claim
-------- | --------- | -------
**id** | String |
**num** | String |
**claim_type** | String |
**claim_text** | List[String]
**claim_references** | List[[Claim Ref](#claim-ref)] | 

##### Claim Ref
-------- | --------- | -------
**value** | String |
**idref** | List[String] |

##### Doc Page
-------- | --------- | -------
**id** | String |
**file** | String |
**wi** | String |
**he** | String |
**type** | String |
**alt** | String |
**pp** | String |
**ppf** | String |
**ppl** | String |
**ocr** | String |
**color** | String |
**orientation** | String |

##### Description
-------- | --------- | -------
**text** | String |
**lang** | String |
**source** | [Source](#source) | 

##### Designation Of States
Field | Type | Description
-------- | --------- | -------
**designation_pct** | [Designation Pct](#designation-pct)
**precautionary_designation_statement** | String
**exclusion_from_designation** | 
**source** | [Source](#source) |

##### Invention Title
Field | Type | Description
-------- | --------- | -------
**text** | String |
**lang** | String |
**source** | [Source](#source) |

##### Parties
Field | Type | Description
-------- | --------- | -------
**applicants** | List[[Applicant](#applicant)] | 
**inventors** | List[[Inventor](#inventor)] |
**deceased_inventors** | List[[Inventor](#inventor)] |
**correspondence_addresses** | List[[Correspondence Address](#correspondence-address)] |
**customer_number** | String |
**agents** | List[[Agent](#agent)] |

##### Applicant
Field | Type | Description
-------- | --------- | -------
**applicant_name** |  [NameGroup](#name-group) |
**address_books** |  List[[Address Book](#address-book)] |
**nationality** | [Country](#country) |
**residence** |  [Country](#country) |
**us_rights** | [US Rights](#us-rights) |
**designated_states** | [Designated States](#designated-states) |
**designated_states_as_inventor** | [Designated States](#designated-states) |
**sequence** | Integer |
**app_type** | [Applicant Type](#applicant-type) |
**designation** | String |  `all`, `all_except_us`,`us_only`,`as_indicated`
**data_format** | String | `DOCDB`, `DOCDBA`, `ORIGINAL`, `EPODOC`, `BNS`
**source** | [Source](#source) |

##### Inventor
Field | Type | Description
-------- | --------- | -------
**inventor_name** |  [NameGroup](#name-group) |
**address_books** |  List[[Address Book](#address-book)] |
**nationality** | [Country](#country) |
**residence** |  [Country](#country) |
**designated_states** | [US Rights](#us-rights) |
**designation** | String |  `all`, `all_except_us`,`us_only`,`as_indicated`
**sequence** | Integer |
**data_format** | String | `DOCDB`, `DOCDBA`, `ORIGINAL`, `EPODOC`, `BNS`
**source** | [Source](#source) |

##### Agent
Field | Type | Description
-------- | --------- | -------
**agent_name** |  [NameGroup](#name-group) |
**address_books** |  List[[Address Book](#address-book)] |
**sequence** | Integer |
**rep_type** | String | `agent`, `attorney`, `common_representative`
**data_format** | String | `DOCDB`, `DOCDBA`, `ORIGINAL`, `EPODOC`, `BNS`
**source** | [Source](#source) |

##### Assignees
Field | Type | Description
-------- | --------- | -------
**assignee** | List[[NameAndAddress](#name-and-address)] |
**source** | [Source](#source) |

##### Examiners
Field | Type | Description
-------- | --------- | -------
**primary_examiner** | [Examiner](#examiner) |
**assistant_examiner** | [Examiner](#examiner) |
**authorized_officer** | [AuthorizedOfficer](#authorized-officer) |
**source** | [Source](#source) |

##### Classification Ipc
Field | Type | Description
-------- | --------- | -------
**edition** | String | 
**main_classification** | String |
**further_classification** | List[[FurtherClassification](#further-classification)] |
**unlinked_indexing_codes** | List[String] |
**linked_indexing_code_groups** | List[[LinkedIndexingCodeGroup](#linked-indexing-code-group)] |
**additional_infos** | List[String] |
**text** | String |
**source** | [Source](#source) |

##### Classification Ipcr
Field | Type | Description
-------- | --------- | -------
**classification_level** | String | `C`, `A`, `S`
**section** | String | 
**clazz** | [Ipc Class](#ipc-class) |
**subclass** | String |
**main_group** | String |
**subgroup** | String |
**symbol** | String |
**version_indicator** | Date |
**symbol_position** | String | `F` - First, `L` - Later
**classification_value** | String | `I` - Invention, `A` - Additional
**action_date** | Date
**classification_status** | String | `B` - Original, `R` - Reclassified
**classification_data_source** | String | `H` - Human, `M` - Machine, `G` - Generated, `C`
**generating_office** | [Country](#country)
**sequence** | Integer |

##### Classifications Cpc
Field | Type | Description
-------- | --------- | -------
**classification_or_combination_set** |  List[[Classification CPC](#classification-cpc)] OR List[[Combination Set](#combination-set)]
**source** | [Source](#source) |

##### Classification CPC
Field | Type | Description
-------- | --------- | -------
**section** | String | 
**clazz** | [Ipc Class](#ipc-class) |
**subclass** | String |
**main_group** | String |
**subgroup** | String |
**symbol** | String |
**version_indicator** | Date |
**symbol_position** | String | `F` - First, `L` - Later
**classification_value** | String | `I` - Invention, `A` - Additional
**action_date** | Date |
**classification_status** | String | `B` - Original, `R` - Reclassified
**classification_data_source** | String | `H` - Human, `M` - Machine, `G` - Generated, `C`
**generating_office** | [Country](#country) |
**sequence** | Integer |

##### Combination Set
Field | Type | Description
-------- | --------- | -------
**group_number** | Integer |
**combination_rank** | List[[Combination Rank](#combination-rank)] |
**sequence** | Integer |

##### Combination Rank
Field | Type | Description
-------- | --------- | -------
**rank_number** | Integer |
**classification_cpc** | [Classification CPC](#classification-cpc) |

##### Classifications National
Field | Type | Description
-------- | --------- | -------
**country** | [Country](#country) | 
**classifications** | List[[Classification National](#classification-national)] |
**source** | [Source](#source) |

#### Classification National
Field | Type | Description
-------- | --------- | -------
**symbol** | String |
**position** | String | `F` - First, `L` - Later

##### Further Classification
Field | Type | Description
-------- | --------- | -------
**content** | String |
**sequence** | Integer |

##### Ipc Class
Field | Type | Description
-------- | --------- | -------
**class_type** | String |
**value** | Integer |

##### References Cited
Field | Type | Description
-------- | --------- | -------
**text** | String |
**citation** | List[[Citation](#citation)]
**date_search_completed** | Date |
**place_of_search** | [Country](#country) |
**search_report_publication** | List[[Document ID](#document-id)] |
**searcher** | [Name And Address](#name-and-address) |
**source** | [Source](#source) |

##### Citation
Field | Type | Description
-------- | --------- | -------
**sequence** | Integer | 
**patcit** | [Patent Citation](#patent-citation) | 
**nplcit** | [NPL Citation](#npl-citation) | 
**corresponding_docs** | List[[Corresponding Docs](#corresponding-docs)] | 
**rel_passages** | List[[Rel Passage](#rel-passage)] |

##### Document ID
Field | Type | Description
-------- | --------- | -------
**country** | [Country](#country) |
**doc_number** | String |
**kind** | String |
**date** | Date |
**lang** | String |
**name.value** | String |
**name.name_type** | String | [ `legal`, `natural` ]

##### Patent Citation
Field | Type | Description
-------- | --------- | -------
**text** | String |
**file** | String |
**url** | String |
**rel_passages** | List[[Rel Passage](#rel-passage)] |
**document_id** | [Document ID](#document-id) |
**doc_number** | String |
**doc_number_type**| String | `EP_UNKNOWN`, `APPLICATION_NUMBER`, `PUBLICATION_NUMBER`

##### Patent Sequence Listing
Field | Type | Description
-------- | --------- | -------
**seq_list_key** | String |
**sequence_types** | List[String] | `P`, `NA`, `DNA`, `RNA`, `AA`
**length_buckets** | List[String] | `NT_1`, `NT_2`, `NT_3`, `NT_4`, `AA_1`, `AA_2`, `AA_3`
**tax_ids** | List[Integer] | 
**doc_locations** | List[String] |
**data_sources** | List[String] | 
**count** | Integer | 
**source** | [Source](#source) |

##### Patent Npl Citations
Field | Type | Description
-------- | --------- | -------
**citation_ids** | List[String] |
**npl_record_lens_ids** | List[String] |
**npl_lens_ids** | List[String] |
**source** | [Source](#source) |

##### Designation PCT
Field | Type | Description
-------- | --------- | -------
**regional** | List[[Regional](#regional)]
**national** | [National](#national)

##### Pct Or Regional Filing Data
Field | Type | Description
-------- | --------- | -------
**document_id** | List[[Document Id](#document-id)] |
**us_371c124_date** | Date |
**us_371c12_date** | Date |

##### Pct Or Regional Publishing Data
Field | Type | Description
-------- | --------- | -------
**document_id** | [Document Id](#document-id) |
**gazette_reference** | [Gazette Reference](#gazette-reference) |

##### Gazette Reference
Field | Type | Description
-------- | --------- | -------
**gazette_num** | String | 
**date** | Date | 
**text** | String | 
**id** | Date | 
**country** | String | 
**lang** | String | 

##### US Term Of Grant
Field | Type | Description
-------- | --------- | -------
**texts** | List[String] | 
**length_of_grants** | List[String] | 
**lapse_of_patents** | List[[Lapse Of Patent](#lapse-of-patent)] | 
**prior_disclosure_affidavit_fields** | List[String] | 
**disclaimers** | List[[Us Disclaimer](#us-disclaimer)] |
**us_term_extensions** | List[String] | 

##### Lapse Of Patent
Field | Type | Description
-------- | --------- | -------
**document_id** | [DocumentId](#document-id) | 
**text** | String | 

##### Us Disclaimer
Field | Type | Description
-------- | --------- | -------
**date** | Date | 
**text** | String | 

##### Regional
Field | Type | Description
-------- | --------- | -------
**region** | String | Country code
*country_and_protection_requests* | List[[Country And Protection Requests](#country-and-protection-requests)]

##### National
Field | Type | Description
-------- | --------- | -------

##### Country And Protection Requests
Field | Type | Description
-------- | --------- | -------
**country* | String
**protection_requests** | List[[Protection Request](#protection-request)]

##### Protection Request
Field | Type | Description
-------- | --------- | -------
**kind_of_protection** | String
**document_id** | [Document ID](#document-id)
**subset** | String

##### NPL Citation
Field | Type | Description
-------- | --------- | -------
**article** | [Article](#article)
**book** | [Book](#book)
**online** | [Online](#online)
**othercit** | String | Other citations
**lang** | String
**file** | String
**medium** | String
**url** | String
**rel_passages** | List[[Rel Passage](#rel-passage)]

##### Corresponding Docs
Field | Type | Description
-------- | --------- | -------
**patcit** | List[[Patent Citation](#patent-citation)]
**nplcit** | List[[NPL Citation](#npl-citation)]
**rel_passages** | List[[Rel Passage](#rel-passage)]

##### Rel Passage
Field | Type | Description
-------- | --------- | -------
**text** | String |
**passage** | List[String] |
**categories_and_relevant_claims** | List[[Categories And Relevant Claims](#categories-and-relevant-claims)] |

##### Article
Field | Type | Description
-------- | --------- | -------
**text** | String
**atl** | String
**abstract_no** | String
**location** | [Location](#location)
**clazz** | List[[IpcClass](#ipc-class)]
**keyword** | List[String]
**cpyrt** | String
**art_id** | String
**ref_no** | List[[RefNo](#ref-no)]
**author** | List[[Author](#author)]
**subname** | List[[SubName](#subname)]
**serial** | [Serial](#serial)
**book** | [Book](#book)

##### Ref No
-------- | --------- | -------
**id** | String
**value** | String

##### Author
-------- | --------- | -------
**id** | String
**address_book** | [Address Book](#address-book)

##### SubName
-------- | --------- | -------
**sub_name_type** | String
**name** | String
**address_book** | [Address Book](#address-book)

##### Location
Field | Type | Description
-------- | --------- | -------
**text** | String
**serpart** | String
**sersect** | String
**chapter** | String
**pp** | String
**column** | String
**para** | String
**line** | String

##### Serial
Field | Type | Description
-------- | --------- | -------
**serial_title** | String
**alt_title** | String
**sub_names** | List[[SubName](#subname)]
**issue** | String
**imprint** | [Imprint](#imprint)
**pub_date** | [NplPubDate](#Npl-pubDate)
**description** | String
**notes** | String
**issn** | String
**isbn** | String
**pub_id** | String
**vid** | String
**issue_no** | String
**cpyrt** | String

##### Imprint
Field | Type | Description
-------- | --------- | -------
**text** | String
**address** | [Address](#address)
**name.value** | String |
**name.name_type** | String | [ `legal`, `natural` ]
**pubdate** | [NplPubDate](#Npl-pubDate)

##### Npl PubDate
Field | Type | Description
-------- | --------- | -------
**time** | String
**start_date** | Date
**start_date** | Date

##### Book
Field | Type | Description
-------- | --------- | -------
**text** | String
**author** | List[[Author](#author)]
**sub_name** | List[[SubName](#subname)]
**book_title** | List[String]
**subtitle** | String
**edition** | String
**imprint** | List[[Imprint](#imprint)]
**description** | String
**conference** | [Conference](#conference)
**series** | [Series](#series)
**abstract_no** | String
**location** | List[[Location](#location)]
**isbn** | List[String]
**issn** | String
**doi** | String
**issue_no** | String
**pub_id** | String
**volume_id** | String
**book_no** | String
**notes** | String
**clazz** | List[[Ipc Class](#ipc-class)]
**keyword** | List[String]
**copyright** | String
**ref_no** | List[[RefNo](#ref-no)]

##### Series
Field | Type | Description
-------- | --------- | -------
**text** | String
**mst** | String
**msn** | String
**issn** | String

###### Conference
Field | Type | Description
-------- | --------- | -------
**text** | String
**conf_title** | String
**conf_date** | [NplPubDate](#npl-pubDate)
**conf_place** | List[[Address](#address)]
**conf_sponsor** | List[[Address Book](#address-book)]
**conf_no** | String

##### Online
Field | Type | Description
-------- | --------- | -------
**text** | String
**online_title** | List[String]
**host_title** | String
**edition** | String
**history** | [History](#history)
**series** | [Series](#series)
**host_no** | String
**location** | [Location](#location)
**series** | [Series](#series)
**notes** | String
**avail** | String
**clazz** | List[[IPC Class](#ipc-class)]
**keyword** | List[String]
**cpyrt** | String
**issn** | String
**isbn** | String
**date_cit** | Date
**search_term** | List[String]
**search_date** | Date
**ref_no** | List[[RefNo](#ref-no)]

##### History
Field | Type | Description
-------- | --------- | -------
**text** | String |
**received** | Date | 
**accepted** | Date |
**revised** | Date |
**misc** | String |

##### Categories And Relevant Claims
Field | Type | Description
-------- | --------- | -------
**category** | List[[CitationCategory](#citation-category)] |
**claims** | List[String]

##### Linked Indexing Code Group
Field | Type | Description
-------- | --------- | -------
**main_linked_indexing_code** | String
**sub_linked_indexing_code** | List[String]

##### Citation Category
`X`: Particularly relevant if taken alone.
`I`: Particularly relevant if taken alone - prejudicing inventive step.
`Y`: Particularly relevant if combined with another document of the same category .
`A`: Defining the state of the art and not prejudicing novelty or inventive step.
`O`: Non-written disclosure.
`P`: Intermediate document.
`T`: Theory or principle underlying the invention.,
`E`: Earlier patent application, but published after the filing date of the application searched (potentially conflicting patent documents).
`D`: Document cited in the application.
`L`: Document cited for other reasons.
`AMPERSAND`: Document member of the same patent family
`R`: Referring to a patent application or a utility model filed on the same day that relates to the same invention

##### Name Group
Field | Type | Description
-------- | --------- | -------
**first_name** | String |
**last_name** | String |
**middle_name** | String |
**prefix** | String |
**suffix** | String |
**synonyms** | List[String] |
**name.value** | String |
**name.name_type** | String | [ `legal`, `natural` ]
**org_name** | String |
**department** | String |
**role** | String |
**iid** | String |
**registered_number** | String |

##### Examiner
Field | Type | Description
-------- | --------- | -------
**electronic_signature** | [ElectronicSignature](#electronic-signature)
**first_name** | String |
**last_name** | String |
**middle_name** | String |
**prefix** | String |
**suffix** | String |
**synonyms** | List[String] |
**name.value** | String |
**name.name_type** | String | [ `legal`, `natural` ]
**org_name** | String |
**department** | String |
**role** | String |
**iid** | String |
**registered_number** | String |

##### Document Type
`ABSTRACT`, `AMENDED_PATENT`, `DESIGN_RIGHT`, `GRANTED_PATENT`, `LIMITED_PATENT`, `PATENT_APPLICATION`, 
`PLANT_PATENT`, `SEARCH_REPORT`, `STATUTORY_INVENTION_REGISTRATION`, `SPC`, `UNKNOWN`

##### Address Book
Field | Type | Description
-------- | --------- | -------
**lang** | String |
**address** | [Address](#address) |
**email** | List[[Email](#email)] |
**phone** | List[String] |
**fax** | List[String] |
**url** | List[String] |
**ead** | List[String] |
**dtext** | String |
**text** | String |

##### Address
Field | Type | Description
-------- | --------- | -------
**address1** | String |
**address2** | String |
**address3** | String |
**address4** | String |
**address5** | String |
**mail_code** | String |
**po_box** | String |
**room** | String |
**address_floor** | String |
**building** | String |
**street** | String |
**city** | String |
**county** | String |
**state** | String |
**post_code** | String |
**country** | String |
**text** | String

##### Correspondence Address
Field | Type | Description
-------- | --------- | -------
**customer_number** | String |
**address_books** | List[[Address Book](#address-book)] |
**source** | [Source](#source) |

##### US Rights
Field | Type | Description
-------- | --------- | -------
**value** | String |
**to_dead_inventor** | String |
**kind** | String |

##### Country
Country code `US`, `EP`, `WO` etc.

##### Designated States
Field | Type | Description
-------- | --------- | -------
**country_without_region** | List[String] |
**region_and_country** | List[[Region And Country](#region-and-country)] |

##### Applicant Type
`applicant`, `applicant-inventor`

##### Region And Country
Field | Type | Description
-------- | --------- | -------
**region** | String |
**countries** | List[String] |

##### Name And Address
Field | Type | Description
-------- | --------- | -------
**name** | [NameGroup](#name-group) |
**address_book** | [Address Book](#address-book) |

##### Authorized Officer
Field | Type | Description
-------- | --------- | -------
**phone** | String |
**fax** | String |
**email** | String |
**electronic_signature** | [ElectronicSignature](#electronic-signature)

##### Source
`USPTO_FULLTEXT`, `USPTO_ASSIGNMENT`, `EPO_FULLTEXT`, `WIPO_FULLTEXT`, `IP_AUSTRALIA_FULLTEXT`, `DOCDB`, `DOCDB_NATIONAL_OFFICE`, `DOCDB_TRANSCRIPT`, `DOCDB_TRANSLATION`, `DOCDB_EPO`, `DOCDB_PAJ`, `INPADOC`, `LENS`, `UNKNOWN`

##### Email
Field | Type | Description
-------- | --------- | -------
**value** | String |
**email_purpose** | String |

##### Electronic Signature
Field | Type | Description
-------- | --------- | -------
**date** | String |
**place_signed** | String |
**basic_signature** | String |
**enhanced_signature** | Boolean

##### Basic Signature
Field | Type | Description
-------- | --------- | -------
**fax_image** | String
**text_string** | String
**click_wrap** | Boolean

##### Abstract
Field | Type | Description
-------- | --------- | -------
**text** | String
**lang** | String
**source** | [Source](#source) |
**data_format** | String | `DOCDB`, `DOCDBA`, `ORIGINAL`, `EPODOC`, `BNS`

##### Legal Status Information
Field | Type | Description
-------- | --------- | -------
**family_id** | String | INPADOC Family ID
**ipr_type** | String | `PATENT_FOR_INVENTION`, `UTILITY_MODEL`
**granted** | Boolean | Is granted patent
**grant_date** | Date | Grant Date
**application_expiry_date** | Date | Application expiry date because of withdrawn or abandonment
**discontinued_date** | Date | Unnatural death of Patent (lapse, withdrawn, abandoned). It can be revived within certain time frame
**anticipated_term_date** | Date | Calculated Term date based on natural term date plus additional extension
**has_disclaimer** | Boolean | Is US patent subjected to a terminal disclaimer
**calculation_log** | List[String] | Steps used to calculate the term date
**patent_status** | String | PENDING, DISCONTINUED, PATENTED, ACTIVE, INACTIVE, EXPIRED
**prosecution_stage** | String | Most recent stage of application `FILING`,`EXAMINATION`,`PRE_GRANT_CHALLENGE`,`GRANT,POST_GRANT_CHALLENGE`,`INACTIVE`,`TERMINATION`
**party_events** | List[[Party Event](#party-event)] | Assignment events history
**publication_count** | Integer

##### Party Event
Field | Type | Description
-------- | --------- | -------
**assignee** | List[[NameAndAddress](#name-and-address)] | Patent assignee/owner information
**assignor** | List[[NameAndAddress](#name-and-address)] | Patent assignor
**recorded_date** | Date | Date recorded of the event by jurisdictional patent office
**execution_date** | Date | Actual effective date of the assignment
**conveyance_type** | String | Type of assignment `ASSIGNMENT`, `CHANGE_OF_NAME`, `CORRECTION`, `GOVERNMENT_INTEREST_AGREEMENT`, `MERGER`, `RELEASE`, `SECURITY_AGREEMENT`, `OTHER`
**text** | String | Conveyance text recorded from jurisdictional patent office
**party_type** | String | `OWNER`, `REPRESENTATIVE`, `INVENTOR`, `LICENSEE`, `OPPONENT`, `OTHER`
**sequence** | String | 

### Examples
##### Get US Granted Applications after 2018
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match" : {
                        "legal_status.granted": true
                    }
                },
                {
                    "term" : {
                        "publication_type": "PATENT_APPLICATION"
                    }
                },
                {
                    "term" : {
                        "country": "US"
                    }
                },
                {
                    "range": {
                        "year_published": {
                            "gte": 2018
                        }
                    }
                }
            ]
        }
    }
}
```

##### US Patent Expiring between 2020-10-10 - 2020-10-20
```json
{
    "query": {
        "bool": {
            "must": [
                {
                    "match" : {
                        "legal_status.granted": true
                    }
                },
                {
                    "term" : {
                        "country": "US"
                    }
                },
                {
                    "range": {
                        "legal_status.anticipated_term_date": {
                            "gte": "2020-10-10",
                            "lte": "2020-10-20"
                        }
                    }
                }
            ]
        }
    }
}
```


### Sample Data
```json
{
    "total": 1,
    "data": [
        {
            "lens_id": "119-951-128-551-362",
            "country": "BR",
            "doc_number": "0000001",
            "kind": "A",
            "date_publ": "2001-08-14",
            "biblio": {
                "publication_reference": {
                    "country": "BR",
                    "doc_number": "0000001",
                    "kind": "A",
                    "date": "2001-08-14"
                },
                "application_reference": {
                    "country": "BR",
                    "doc_number": "0000001",
                    "kind": "A",
                    "date": "2000-01-03",
                    "is_representative": false
                },
                "priority_claims": {
                    "priority_claim": [
                        {
                            "country": "BR",
                            "doc_number": "0000001",
                            "kind": "A",
                            "date": "2000-01-03",
                            "sequence": 1,
                            "source": "DOCDB"
                        }
                    ]
                },
                "invention_title": [
                    {
                        "text": "Proteção para garrafões de água mineral.",
                        "lang": "pt",
                        "source": "DOCDB"
                    }
                ],
                "parties": {
                    "applicants": [
                        {
                            "applicant_name": {
                                "last_name": "RAMOS CARLOS A S DE CASTRO"
                            },
                            "residence": "BR",
                            "app_type": "APPLICANT",
                            "sequence": 1
                        },
                        {
                            "applicant_name": {
                                "last_name": "CARLOS ALBERTO SOARES DE CASTRO RAMOS"
                            },
                            "app_type": "APPLICANT",
                            "sequence": 1
                        }
                    ],
                    "inventors": [
                        {
                            "inventor_name": {
                                "last_name": "RAMOS CARLOS ALBERTO SOARES DE"
                            },
                            "sequence": 1
                        },
                        {
                            "inventor_name": {
                                "last_name": "CARLOS ALBERTO SOARES DE CASTRO RAMOS"
                            },
                            "sequence": 1
                        }
                    ],
                    "source": "DOCDB"
                },
                "classifications_ipc": {
                    "edition": "7",
                    "main_classification": "B65D23/02",
                    "source": "DOCDB"
                },
                "classifications_ipcr": {
                    "classification_ipcr": [
                        {
                            "section": "B",
                            "clazz": {
                                "value": "65"
                            },
                            "subclass": "D",
                            "main_group": "23",
                            "subgroup": "02",
                            "symbol": "B65D23/02",
                            "version_indicator": "2006-01-01",
                            "classification_level": "A",
                            "classification_value": "I",
                            "action_date": "2005-11-10",
                            "classification_status": "R",
                            "classification_data_source": "M",
                            "generating_office": "EP",
                            "sequence": 1
                        }
                    ],
                    "source": "DOCDB"
                }
            },
            "abstract": [
                {
                    "text": "''PROTEçãO PARA GARRAFõES DE áGUA MINERAL'' Trata-se de uma proteção, feita em Latex resistente para garrafões de água mineral, compreende por ser um produto com formato afunilado, com abertura dos dois lados e tendo um anel de Latex em cada abertura, de maneira que se ajuste perfeitamente no garrafão de água mineral impedindo assim que a água entre em contato com a superfície do garrafão contaminada por bactérias, fungos, urina de animais, etc.",
                    "lang": "pt",
                    "source": "DOCDB_NATIONAL_OFFICE"
                }
            ],
            "document_type": "PATENT_APPLICATION",
            "legal_status": {
                "family_id": 3943293,
                "ipr_type": "patent for invention",
                "granted": false,
                "application_expiry_date": "2004-10-05",
                "calculation_log": [
                    "Application Filing Date: 2000-01-03",
                    "DEFINITIVE DISMISSAL ACC. ARTICLE 33 OF IPL - EXTENSION OF TIME LIMIT FOR REQUEST OF EXAMINATION EXPIRED"
                ],
                "patent_status": "DISCONTINUED",
                "prosecution_stage": "INACTIVE",
                "publication_count": 1
            }
        }
    ],
    "results": 1
}
```