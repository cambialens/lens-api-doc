import csv
from typing import List

from models import Affiliation, Author, Work, MeshTerms

class WorkCsvWriter:
	def __init__(self, location):
		work_headers = ['Lens ID', 'Title', 'Date Published', 'Publication Year', 'Publication Type', 'Source Title', 'ISSNs', 'Publisher',
						'Source Country', 'Abstract', 'Volume', 'Issue Number', 'Start Page','End Page', 'Fields of Study', 'Keywords',
						'Chemicals', 'Funding', 'Source URLs', 'External URL', 'PMID', 'DOI', 'Microsoft Academic ID', 'PMCID', 
						'Citing Patents Count', 'References', 'Citing Works Count','Is Open Access', 'Open Access License', 'Open Access Colour']

		author_headers = ['lens_id', 'author_sub_id', 'first_name', 'last_name', 'initials', 'magid', 'orcidid']
		affiliation_headers = ['lens_id', 'author_sub_id', 'name', 'ror', 'grid_id', 'country_code']
		mesh_term_headers = ['lens_id', 'mesh_id', 'mesh_heading', 'qualifier_id', 'qualifier_name']

		self.work_csv_file = open(location + '/works.csv', 'w', newline='', encoding='utf-8')
		self. author_csv_file = open(location + '/authors.csv', 'w', newline='', encoding='utf-8')
		self. affiliation_csv_file = open(location + '/author_affiliations.csv', 'w', newline='', encoding='utf-8')
		self. meshterm_csv_file = open(location + '/mesh_terms.csv', 'w', newline='', encoding='utf-8')

		self.work_writer = csv.DictWriter(self.work_csv_file, fieldnames=work_headers)
		self.author_writer = csv.DictWriter(self.author_csv_file, fieldnames=author_headers)
		self.affiliation_csv_writer = csv.DictWriter(self.affiliation_csv_file, fieldnames=affiliation_headers)
		self.meshterm_csv_writer = csv.DictWriter(self.meshterm_csv_file, fieldnames=mesh_term_headers)


		self.work_writer.writeheader()
		self.author_writer.writeheader()
		self.affiliation_csv_writer.writeheader()
		self.meshterm_csv_writer.writeheader()

	def write(self, work: Work):
		self.__write_work(work)
		self.__write_authors(work.lens_id, work.authors)
		self.__write_meshterms(work.lens_id, work.mesh_terms)

	def close(self):
		self.affiliation_csv_file.close()
		self.author_csv_file.close()
		self.meshterm_csv_file.close()
		self.work_csv_file.close()

	def __write_work(self, work: Work):
		work_dist = {
						'Lens ID': work.lens_id, 
						'Title': work.title,
						'Date Published': work.date_published,
						'Publication Year':work.publication_year,
						'Publication Type': work.publication_type,
						'Source Title': work.source_title,
						'ISSNs': work.issn,
						'Publisher': work.publisher,
						'Source Country': work.source_country,
						'Microsoft Academic ID': work.magid,
						'DOI': work.doi,
						'Abstract': work.abstract,
						'Volume': work.volume,
						'Issue Number': work.issue_number, 
						'Start Page': work.start_page,
						'End Page': work.end_page,
						'Fields of Study': work.fields_of_study,
						'Keywords': work.keywords,
						'Chemicals': work.chemicals,
						'Funding': work.funding,
						'Source URLs': work.source_urls,
						'External URL': work.external_url,
						'PMID': work.pmid,
						'PMCID': work.pmcid,
						'Citing Patents Count': work.citing_patents_count,
						'References': work.references,
						'Citing Works Count': work.citing_works_count,
						'Is Open Access': work.is_open_access,
						'Open Access License': work.open_access_license,
						'Open Access Colour': work.open_access_colour
					}
		self.work_writer.writerow(work_dist)

	def __write_authors(self, lens_id, authors: List[Author]):
		author_sub_id = 1
		for author in authors:
			authors_dist = {
								'lens_id': lens_id, 
								'author_sub_id': author_sub_id, 
								'first_name': author.first_name, 
								'last_name': author.last_name, 
								'initials': author.initials, 
								'magid': author.magid,
								'orcidid': author.orcidid
							}
			self.author_writer.writerow(authors_dist)
			self.__write_affiliaions(lens_id, author_sub_id, author.affiliations)
			author_sub_id += 1

	def __write_affiliaions(self, lens_id, author_sub_id, affiliations: List[Affiliation]):
		for affiliation in affiliations:
			affiliations_dist = {
									'lens_id': lens_id, 
									'author_sub_id': author_sub_id, 
									'name': affiliation.name, 
									'ror': affiliation.ror, 
									'grid_id':affiliation.grid_id, 
									'country_code': affiliation.country_code
								}
			self.affiliation_csv_writer.writerow(affiliations_dist)

	def __write_meshterms(self, lens_id, mesh_terms: List[MeshTerms]):
		for meshterm in mesh_terms:
			mesh_term_dist = {
								'lens_id': lens_id,
								'mesh_id': meshterm.mesh_id,
								'mesh_heading': meshterm.mesh_heading,
								'qualifier_id': meshterm.qualifier_id,
								'qualifier_name': meshterm.qualifier_name
							}
			self.meshterm_csv_writer.writerow(mesh_term_dist)

