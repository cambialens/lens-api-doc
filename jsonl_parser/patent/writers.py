import csv

from typing import List

from model import Patent

class PatentCsvWriter:
	def __init__(self, patent_csv_file):
		patent_headers = ['Lens ID', 'Jurisdiction', 'Kind', 'Display Key', 'Publication Date', 'Publication Year', 
        'Application Number', 'Application Date', 'Priority Numbers', 'Earliest Priority Date', 'Title', 'Abstract',
        'Applicants', 'Inventors', 'Owners', 'URL', 'Document Type', 'Cites Patent Count', 'Cited By Patent Count', 
        'Simple Family Size', 'Extended Family Size', 'CPC Classification', 'IPCR Classification',
        'US Classification', 'NPL Citation Count', 'NPL Resolved Citation Count', 'NPL Resolved Lens IDs',
        'NPL Resolved External IDs', 'NPL Citations', 'Legal Status', 'Claims']

		self.patent_writer = csv.DictWriter(patent_csv_file, fieldnames=patent_headers)

		self.patent_writer.writeheader()
		
	def write(self, patent: Patent):
		self.__write_patent(patent)

	def __write_patent(self, patent: Patent):
		patent_dist = {
						'Lens ID' : patent.lens_id,
                		'Jurisdiction' : patent.jurisdiction,
                		'Kind' : patent.kind,
                		'Display Key' : patent.display_key,
                		'Publication Date' : patent.publication_date,
                		'Publication Year' : patent.publication_year,
                		'Application Number' : patent.application_number,
                		'Application Date' : patent.application_date,
                        'Priority Numbers' : patent.priority_numbers,
                		'Earliest Priority Date': patent.earliest_priority_date,
                		'Title' : patent.title,
                		'Abstract' : patent.abstract,
                		'Applicants' : patent.applicants,
                		'Inventors' : patent.inventors,
                		'Owners' : patent.owners,
						'URL' : patent.url,
                		'Document Type' : patent.document_type,
                		'Cites Patent Count' : patent.cites_patent_count,
						'Cited By Patent Count' : patent.cited_by_patent_count,
                		'Simple Family Size' : patent.simple_family_size,
                		'Extended Family Size' : patent.extended_family_size,
                		'CPC Classification' : patent.cpc_classification,
                		'IPCR Classification' : patent.ipcr_classification,
                		'US Classification' : patent.us_classification,
                		'NPL Citation Count' : patent.npl_citation_count,
                		'NPL Resolved Citation Count' : patent.npl_resolved_citation_count,
                		'NPL Resolved Lens IDs' : patent.npl_resolved_lens_ids,
                		'NPL Resolved External IDs' : patent.npl_resolved_external_ids,
                		'NPL Citations' : patent.npl_citations,
                		'Legal Status' : patent.legal_status,
						'Claims': patent.claims
					}
		self.patent_writer.writerow(patent_dist)
