#writers
import csv
from typing import List

from models import Affiliation, Author, Work, MeshTerms

class WorkCsvWriter:
	def __init__(self, location):
		work_headers = ['lens_id', 'title', 'date_published', 'publication_year', 'publication_type', 'source_title',
						'publisher', 'source_country', 'magid', 'doi', 'coreid','patent_citations','abstract','volume',
						'issue_number', 'start_page', 'end_page', 'fields_of_study', 'keywords', 'source_urls','external_url',
						'pmid', 'microsoft_academic_id', 'pmcid','citing_patents_count','references','citing_works_count', 
						'is_open_access','open_access_license', 'open_access_colour']
		author_headers = ['lens_id', 'author_sub_id', 'first_name', 'last_name', 'initials', 'magid']
		affiliation_headers = ['lens_id', 'author_sub_id', 'name', 'magid', 'grid', 'ror', 'grid_id', 'country_code']
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
						'lens_id': work.lens_id, 
						'title': work.title,
						'date_published': work.date_published,
						'publication_year':work.publication_year,
						'publication_type': work.publication_type,
						'source_title': work.source_title,
						'publisher': work.publisher,
						'source_country': work.source_country,
						'magid': work.magid,
						'doi': work.doi,
						'coreid': work.coreid,
						'patent_citations': ';'.join(work.patent_citations),
						'abstract': work.abstract,
						'volume': work.volume,
						'issue_number': work.issue_number, 
						'start_page': work.start_page,
						'end_page': work.end_page,
						'fields_of_study': work.fields_of_study,
						'keywords': work.keywords,
						'external_url': work.external_url,
						'pmid': work.pmid,
						'microsoft_academic_id': work.microsoft_academic_id,
						'pmcid': work.pmcid,
						'citing_patents_count': work.citing_patents_count,
						'references': work.references,
						'citing_works_count': work.citing_works_count,
						'is_open_access': work.is_open_access,
						'open_access_license': work.open_access_license,
						'open_access_colour': work.open_access_colour
					}
		self.work_writer.writerow(work_dist)

	def __write_authors(self, lens_id, authors: List[Author]):
		author_sub_id = 1
		for author in authors:
			self.__write_affiliaions(lens_id, author_sub_id, author.affiliations)
			authors_dist = {
								'lens_id': lens_id, 
								'author_sub_id': author_sub_id, 
								'first_name': author.first_name, 
								'last_name': author.last_name, 
								'initials': author.initials, 
								'magid': author.magid
							}
			self.author_writer.writerow(authors_dist)
			author_sub_id += 1

	def __write_affiliaions(self, lens_id, author_sub_id, affiliations: List[Affiliation]):
		for affiliation in affiliations:
			affiliations_dist = {
									'lens_id': lens_id, 
									'author_sub_id': author_sub_id, 
									'name': affiliation.name, 
									'magid': affiliation.magid, 
									'grid': affiliation.grid, 
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