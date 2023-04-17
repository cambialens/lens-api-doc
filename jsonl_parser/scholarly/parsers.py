from models import Work, Author, Affiliation, MeshTerms
from datetime import datetime

class WorkParser:

	def parse(self, work_json):
		magid = None
		doi = None
		pmid = None
		pmcid = None
		external_url = None
		lens_id = work_json.get('lens_id')
		title = work_json.get('title')
		date_published = work_json.get('date_published')
		publication_year = work_json.get('year_published')
		publication_type = work_json.get('publication_type')
		authors = self.__get_authors(work_json['authors']) if 'authors' in work_json else []
		abstract = work_json.get('abstract')
		volume = work_json.get('volume')
		issue_number = work_json.get('issue')
		start_page = work_json.get('start_page')
		end_page = work_json.get('end_page')
		fields_of_study = self.__get_value(work_json, 'fields_of_study')
		keywords = self.__get_value(work_json, 'keywords')
		chemicals = self.__get_value(work_json.get('chemicals'), 'substance_name')
		funding = self.__get_value(work_json.get('funding'), 'org')
		mesh_terms = self.__get_meshterms(work_json['mesh_terms']) if 'mesh_terms' in work_json else []
		citing_patents_count = work_json.get('patent_citations_count')
		references = self.__get_value(work_json.get('references'), lens_id)
		citing_works_count = work_json.get('citing_works_count')
		is_open_access = work_json.get('is_open_access')
		source_urls = self.__get_value(work_json, 'source_urls', 'url')
		source = work_json.get('source')
		source_title = self.__get_value(source, 'title')
		source_country = self.__get_value(source, 'country')
		publisher = self.__get_value(source, 'publisher')
		issn = self.__get_value(source, 'issn', 'value')
		open_access_license = self.__get_value(work_json, 'open_access', 'license')
		open_access_colour = self.__get_value(work_json, 'open_access', 'colour')

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
	

	def __get_value(self, root,  *args):
		if root is None:
			return ''
		elif isinstance(root, str):
			return root
		elif isinstance(root, int):
			return root
		elif isinstance(root, dict):
			(key, *tail) =args
			v = root[key] if key in root else ''
			return self.__get_value(v, *tail)
		elif isinstance(root, list):
			return ';'.join(filter(None, map(lambda item: self.__get_value(item, *args), root)))
