from model import Patent

class PatentParser:

    def parse(self, patent_json):
        lens_id = patent_json.get('lens_id')
        jurisdiction = patent_json.get('jurisdiction')
        kind = patent_json.get('kind')
        display_key = self.__get_docnumber(jurisdiction, patent_json.get('doc_number'), kind)
        title = patent_json.get('title')
        abstract = self.__get_object(patent_json, 'abstract')
        abstract_text = abstract[0].get('text') if abstract else ''

        document_type = patent_json.get('publication_type')
        biblio = patent_json.get('biblio') if 'biblio' in patent_json else {}
        # Publication reference
        publication_date = self.__get_string(biblio, 'publication_reference', 'date')
        publication_year = publication_date.split('-')[0]
        # Application reference
        application_jurisdiction = self.__get_string(biblio, 'application_reference', 'jurisdiction')
        application_kind = self.__get_string(biblio, 'application_reference', 'kind')
        application_doc_number = self.__get_string(biblio, 'application_reference', 'doc_number')
        application_number = self.__get_docnumber(application_jurisdiction, application_doc_number, application_kind)
        application_date = self.__get_string(biblio, 'application_reference', 'date')
        # Priority claims
        priority_claims = self.__get_object(biblio, 'priority_claims')
        priority_numbers = self.__get_string(priority_claims, 'claims', 'doc_number')
        earliest_priority_date = self.__get_string(priority_claims, 'earliest_claim', 'date')
        #classification
        cpc_classification = self.__get_string(biblio, 'classifications_cpc', 'classifications', 'symbol')
        us_classification = self.__get_string(biblio, 'classifications_national', 'classifications', 'symbol')
        ipcr_classification = self.__get_string(biblio, 'classifications_ipcr', 'classifications', 'symbol')
        
        title = self.__get_string(biblio, 'invention_title', 'text')
        applicants = self.__get_string(biblio, 'parties', 'applicants', 'extracted_name', 'value')
        inventors = self.__get_string(biblio, 'parties', 'inventors', 'extracted_name', 'value')
        owners = self.__get_string(biblio, 'parties', 'owners_all', 'extracted_name', 'value')
        url = 'https://lens.org/' + lens_id
        npl_resolved_lens_ids = self.__get_string(biblio, 'references_cited', 'citations', 'nplcit', 'lens_id')
        npl_resolved_external_ids = self.__get_string(biblio, 'references_cited', 'citations', 'nplcit', 'external_ids')
        npl_citations = self.__get_string(biblio, 'references_cited', 'citations', 'nplcit', 'text')
        npl_citations_count = self.__get_number(biblio, 'references_cited', 'npl_count')
        npl_resolved_citation_count = self.__get_number(biblio, 'references_cited', 'npl_resolved_count')
        cites_patent_count = self.__get_number(biblio, 'references_cited', 'patent_count')
        cited_by_patent_count = self.__get_number(biblio,'cited_by', 'patent_count')
        extended_family_size = self.__get_number(patent_json, 'families', 'extended_family', 'size')
        simple_family_size = self.__get_number(patent_json, 'families', 'simple_family', 'size')
        legal_status = self.__get_string(patent_json, 'legal_status', 'patent_status')
        claims = self.__get_string(patent_json, 'claims', 'claims', 'claim_text')

        return Patent(lens_id, jurisdiction, kind, display_key, publication_date, publication_year, application_number,
                application_date, priority_numbers, earliest_priority_date, title, abstract_text, applicants, inventors, owners, url,
                document_type, cites_patent_count, cited_by_patent_count, simple_family_size, extended_family_size,cpc_classification, ipcr_classification,
                us_classification, npl_citations_count, npl_resolved_citation_count, npl_resolved_lens_ids, npl_resolved_external_ids, npl_citations,
                legal_status, claims)
                
    def __get_object(self, root, element):
        if root is None:
            return {}
        else:
            return root[element] if element in root else {}
        
    def __get_number(self, root, *args):
        return self.__get_value(root, 0, *args)

    def __get_string(self, root, *args):
        return self.__get_value(root, '', *args)

    def __get_value(self, root, default, *args):
        if root is None:
            return default
        elif isinstance(root, str):
            return root
        elif isinstance(root, int):
            return root
        elif isinstance(root, dict):
            (key, *tail) = args
            v = root[key] if key in root else default
            return self.__get_value(v, default, *tail)
        elif isinstance(root, list):
            return ';'.join(filter(None, map(lambda item: self.__get_value(item, default, *args), root)))
        else:
            return ValueError("Expected root to be dict, found " + str(type(root)))
        
    def __get_docnumber(self, jurisdictions, doc_number, kind):
        new_doc_number = ' '.join([jurisdictions, doc_number, kind])
        return(new_doc_number)
