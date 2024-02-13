class Patent:
	def __init__(self, lens_id, jurisdiction, kind, display_key, publication_date, publication_year, application_number,
                application_date, priority_numbers, earliest_priority_date, title, abstract, applicants, inventors, owners, url,
                document_type, cites_patent_count, cited_by_patent_count, simple_family_size, extended_family_size, cpc_classification, 
                ipcr_classification, us_classification, npl_citation_count,npl_resolved_citation_count, npl_resolved_lens_ids,
                npl_resolved_external_ids, npl_citations, legal_status, claims):
                self.lens_id = lens_id
                self.jurisdiction = jurisdiction
                self.kind = kind
                self.display_key = display_key
                self.publication_date = publication_date
                self.publication_year = publication_year
                self.application_number = application_number
                self.application_date = application_date
                self.priority_numbers = priority_numbers
                self.earliest_priority_date = earliest_priority_date
                self.title = title
                self.abstract = abstract
                self.applicants = applicants
                self.inventors = inventors
                self.owners = owners
                self.url = url
                self.document_type = document_type
                self.cites_patent_count = cites_patent_count
                self.cited_by_patent_count = cited_by_patent_count
                self.simple_family_size = simple_family_size
                self.extended_family_size = extended_family_size
                self.cpc_classification = cpc_classification
                self.ipcr_classification = ipcr_classification
                self.us_classification = us_classification
                self.npl_citation_count = npl_citation_count
                self.npl_resolved_citation_count = npl_resolved_citation_count
                self.npl_resolved_lens_ids = npl_resolved_lens_ids
                self.npl_resolved_external_ids = npl_resolved_external_ids
                self.npl_citations = npl_citations
                self.legal_status = legal_status
                self.claims = claims
