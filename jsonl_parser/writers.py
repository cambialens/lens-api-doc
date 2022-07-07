#writers
import csv
from typing import List

from models import Affiliation, Author, Work

class WorkCsvWriter:
	def __init__(self, location):
		work_headers = ['lens_id', 'title', 'publication_type', 'magid', 'doi', 'coreid', 'patent_citations', 'abstract']
		author_headers = ['lens_id', 'author_sub_id', 'first_name', 'last_name', 'initials', 'magid']
		affiliation_headers = ['lens_id', 'author_sub_id', 'name', 'magid', 'grid', 'ror', 'grid_id', 'country_code']

		self.work_csv_file = open(location + '/works.csv', 'w', encoding='utf-8')
		self. author_csv_file = open(location + '/authors.csv', 'w', encoding='utf-8')
		self. affiliation_csv_file = open(location + '/author_affiliations.csv', 'w', encoding='utf-8')

		self.work_writer = csv.DictWriter(self.work_csv_file, fieldnames=work_headers)
		self.author_writer = csv.DictWriter(self.author_csv_file, fieldnames=author_headers)
		self.affiliation_csv_writer = csv.DictWriter(self.affiliation_csv_file, fieldnames=affiliation_headers)

		self.work_writer.writeheader()
		self.author_writer.writeheader()
		self.affiliation_csv_writer.writeheader()

	def write(self, work: Work):
		self.__write_work(work)
		self.__write_authors(work.lens_id, work.authors)

	def close(self):
		self.affiliation_csv_file.close()
		self.author_csv_file.close()
		self.work_csv_file.close()

	def __write_work(self, work: Work):
		work_dist = {
						'lens_id': work.lens_id, 
						'title': work.title,
						'publication_type': work.publication_type,
						'magid': work.magid,
						'doi': work.doi,
						'coreid': work.coreid,
						'patent_citations': ';'.join(work.patent_citations),
						'abstract': work.abstract
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