from jsonl_parser.models import Work, Author, Affiliation

class WorkParser:

	def parse(self, work_json):
		lens_id = work_json['lens_id']
		title = work_json['title']
		publication_type = work_json['publication_type']
		authors = self.__get_authors(work_json['authors']) if 'authors' in work_json else []
		external_ids = work_json['external_ids'] if 'external_ids' in work_json else []
		magid = ''
		doi = ''
		coreid = ''
		# Can there be multiple id with same type?
		for external_id in external_ids:
			type = external_id.get('type')
			if type == 'magid':
				magid = external_id['value']
			elif type == 'doi':
				doi = external_id['value']
			elif type == 'coreid':
				coreid = external_id['value']
		patent_citations = work_json['patent_citations'] if 'patent_citations' in work_json else []
		patent_citation_lens_ids = [pc['lens_id'] for pc in patent_citations]
		abstract = work_json['abstract'] if 'abstract' in work_json else ''

		return Work(lens_id, title, publication_type, authors, magid, doi, coreid, patent_citation_lens_ids, abstract)

	def __get_authors(self, authors_json):
		authors = []
		for author in authors_json:
			first_name = author['first_name']
			last_name = author['last_name']
			initials = author['initials']
			ids = author['ids'] if 'ids' in author else []
			magid = ''
			for id in ids:
				if id['type'] == 'magid':
					magid = id['value']
			affiliations = self.__get_affiliations(author['affiliations']) if 'affiliations' in author else []
			authors.append(Author(first_name, last_name, initials, magid, affiliations))
		return authors

	def __get_affiliations(self, affiliations_json):
		affiliations = []
		for affiliation in affiliations_json:
			name = affiliation.get('name')
			magid = affiliation.get('magid')
			grid = affiliation.get('grid')
			ror = affiliation.get('ror')
			grid_id = affiliation.get('grid_id')
			country_code = affiliation.get('country_code')
			affiliations.append(Affiliation(name, magid, grid, ror, grid_id, country_code))
		return affiliations