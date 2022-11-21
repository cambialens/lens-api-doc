from models import Work, Author, Affiliation, MeshTerms

class WorkParser:

	def parse(self, work_json):
		source_title = None
		publisher = None
		source_country = None
		issn = None
		magid = None
		doi = None
		pmid = None
		pmcid = None
		external_url = None
		open_access_license = None
		open_access_colour = None
		source_urls = None
		references = None
		lens_id = work_json.get('lens_id')
		title = work_json.get('title')
		date_published = work_json.get('date_published')
		publication_year = work_json.get('publication_year')
		publication_type = work_json.get('publication_type')
		authors = self.__get_authors(work_json['authors']) if 'authors' in work_json else []
		abstract = work_json.get('abstract')
		volume = work_json.get('volume')
		issue_number = work_json.get('issue')
		start_page = work_json.get('start_page')
		end_page = work_json.get('end_page')
		fields_of_study = ','.join(work_json.get('fields_of_study')) if 'fields_of_study' in work_json else ''
		if (work_json.get('keywords') == [None]):
			keywords = None
		else:
			keywords = ','.join(work_json['keywords']) if 'keywords' in work_json else None
		chemicals = self.__get_chemicals(work_json['chemicals'])if 'chemicals' in work_json else None
		funding = self.__get_funding(work_json['funding']) if 'funding' in work_json else None
		mesh_terms = self.__get_meshterms(work_json['mesh_terms']) if 'mesh_terms' in work_json else []
		citing_patents_count = work_json.get('patent_citations_count')
		reference = work_json.get('references')
		if (reference is not None):
			references = ';'.join(map(lambda id: id.get('lens_id'), reference))
		citing_works_count = work_json.get('citing_works_count')
		is_open_access = work_json.get('is_open_access')

		url = work_json.get('source_urls')
		if (url is not None):
			source_urls = ';'.join(map(lambda id: id.get('url'), url))

		source = work_json.get('source')
		if (source is not None):
			source_title = source.get('title', '')
			source_country = source.get('country', '')
			publisher = source.get('publisher', '')
			issns = source.get('issn')
			if(issns is not None):
				issn = ';'.join(map(lambda id: id.get('value'), issns))
		
		external_id = work_json.get('external_ids')
		if (external_id is not None):
			external_url = self.__get_external_url(external_id)
			for id in external_id:
				type = id.get('type')
				value = id['value']
				if type == 'magid':
					magid = value
				elif type == 'doi':
					doi = value
				elif type == 'pmid':
					pmid = value
				elif type == 'pmcid':
					pmcid = value
		
		open_access = work_json.get('open_access')
		if bool(open_access is not None):
			open_access_license = open_access.get('license')
			open_access_colour = open_access.get('colour')

		return Work(lens_id, title, date_published, publication_year, publication_type, source_title, issn, publisher, 
					source_country, authors, magid, doi, abstract, volume, issue_number, start_page, end_page, fields_of_study, 
					keywords, chemicals, funding, mesh_terms, source_urls, external_url, pmid, pmcid,citing_patents_count, 
					references, citing_works_count, is_open_access, open_access_license, open_access_colour)

	def __get_authors(self, authors_json):
		authors = []
		magid = None
		orcidid = None
		for author in authors_json:
			first_name = author.get('first_name')
			last_name = author.get('last_name')
			initials = author.get('initials')
			ids = author.get('ids') 
			if (ids is not None):
				for id in ids:
					if id['type'] == 'magid':
						magid = id['value']
					elif id['type'] == 'orcid':
						orcidid = id['value']
			affiliations = self.__get_affiliations(author['affiliations']) if 'affiliations' in author else []
			authors.append(Author(first_name, last_name, initials, magid, orcidid, affiliations))
		return authors

	def __get_affiliations(self, affiliations_json):
		affiliations = []
		ror = None
		for affiliation in affiliations_json:
			name = affiliation.get('name')
			ids = affiliation['ids'] if 'ids' in affiliation else []
			for id in ids:
				if id['type'] == 'ror':
					ror = id['value']
			grid_id = affiliation.get('grid_id')
			country_code = affiliation.get('country_code')
			affiliations.append(Affiliation(name, ror, grid_id, country_code))
		return affiliations

	def __get_meshterms(self, mesh_terms_json):
		mesh_terms = []
		for mesh_term in mesh_terms_json:
			mesh_id = mesh_term.get('mesh_id')
			mesh_heading = mesh_term.get('mesh_heading')
			qualifier_id = mesh_term.get('qualifier_id')
			qualifier_name = mesh_term.get('qualifier_name')
			mesh_terms.append(MeshTerms(mesh_id, mesh_heading, qualifier_id, qualifier_name))	
		return mesh_terms

	def __get_chemicals(self, chemicals_json):
		chemicals = ''
		for chemical in chemicals_json:
			for key, value in chemical.items():
				if key == 'substance_name':
					chemicals =','.join(value )
		return chemicals

	def __get_funding(self, funding_json):
		fundings = ''
		for funding in funding_json:
			for key, value in funding.items():
				if key == 'org':
					fundings = ','.join(value)
		return fundings

	def __get_external_url(self, external_id):
		external_url = None
		for external_ids in external_id:
			type = external_ids.get('type')
			value = external_ids.get('value')
			if type == 'doi':
				external_url = "http://dx.doi.org/" + value
			if type == 'pmid':
				external_url = "https://www.ncbi.nlm.nih.gov/pubmed/" + value
			if type == 'pmcid':
				external_url = "https://www.ncbi.nlm.nih.gov/pmc/articles/" + value
		return external_url