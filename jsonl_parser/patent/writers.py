import csv

from typing import List

from model import Patent

class PatentCsvWriter:
	def __init__(self, patent_csv_file):
		patent_headers = ['lens_id', 'jurisdiction', 'kind', 'display_key', 'publication_date', 'publication_year', 
        'application_number', 'application_date', 'priority_numbers', 'earliest_priority_date', 'title', 'abstract',
        'applicants', 'inventors', 'owners', 'document_type', 'cites_patent_count',
        'simple_family_size', 'extended_family_size', 'cpc_classification', 'ipcr_classification',
        'us_classification', 'npl_citation_count', 'npl_resolved_citation_count', 'npl_resolved_lens_ids',
        'npl_resolved_external_ids', 'npl_citations', 'legal_status']

		self.patent_writer = csv.DictWriter(patent_csv_file, fieldnames=patent_headers)

		self.patent_writer.writeheader()
		
	def write(self, patent: Patent):
		self.__write_patent(patent)

	def __write_patent(self, patent: Patent):
		patent_dist = {
						'lens_id' : patent.lens_id,
                		'jurisdiction' : patent.jurisdiction,
                		'kind' : patent.kind,
                		'display_key' : patent.display_key,
                		'publication_date' : patent.publication_date,
                		'publication_year' : patent.publication_year,
                		'application_number' : patent.application_number,
                		'application_date' : patent.application_date,
                        'priority_numbers' : patent.priority_numbers,
                		'earliest_priority_date': patent.earliest_priority_date,
                		'title' : patent.title,
                		'abstract' : patent.abstract,
                		'applicants' : patent.applicants,
                		'inventors' : patent.inventors,
                		'owners' : patent.owners,
                		'document_type' : patent.document_type,
                		'cites_patent_count' : patent.cites_patent_count,
                		'simple_family_size' : patent.simple_family_size,
                		'extended_family_size' : patent.extended_family_size,
                		'cpc_classification' : patent.cpc_classification,
                		'ipcr_classification' : patent.ipcr_classification,
                		'us_classification' : patent.us_classification,
                		'npl_citation_count' : patent.npl_citation_count,
                		'npl_resolved_citation_count' : patent.npl_resolved_citation_count,
                		'npl_resolved_lens_ids' : patent.npl_resolved_lens_ids,
                		'npl_resolved_external_ids' : patent.npl_resolved_external_ids,
                		'npl_citations' : patent.npl_citations,
                		'legal_status' : patent.legal_status
					}
		self.patent_writer.writerow(patent_dist)
