from models import Work, Author, Affiliation, MeshTerms

class WorkParser:

	def parse(self, work_json):
		lens_id = work_json.get('lens_id')
		title = work_json.get('title')
		date_published = work_json.get('date_published')
		publication_year = work_json.get('publication_year')
		publication_type = work_json.get('publication_type')
		source_title = ''
		publisher = ''
		source_country = ''
		source = work_json['source'] if 'source' in work_json else []
		if bool(source):
			for key, value in source.items():
				if key == 'title':
					source_title = value
				elif key == 'publisher':
					publisher = value
				elif key == 'country':
					source_country = value
		authors = self.__get_authors(work_json['authors']) if 'authors' in work_json else []
		external_ids = work_json['external_ids'] if 'external_ids' in work_json else []
		magid = ''
		doi = ''
		coreid = ''
		pmid = ''
		pmcid = ''
		# Can there be multiple id with same type?
		for external_id in external_ids:
			type = external_id.get('type')
			if type == 'magid':
				magid = external_id['value']
			elif type == 'doi':
				doi = external_id['value']
			elif type == 'pmid':
				pmid = external_id['value']
			elif type == 'coreid':
				coreid = external_id['value']
			elif type == 'pmcid':
				pmcid = external_id['value']
		patent_citations = work_json['patent_citations'] if 'patent_citations' in work_json else []
		patent_citation_lens_ids = [pc['lens_id'] for pc in patent_citations]
		abstract = work_json.get('abstract')
		volume = work_json.get('volume')
		issue_number = work_json.get('issue')
		start_page = work_json.get('start_page')
		end_page = work_json.get('end_page')
		fields_of_study = ','.join(work_json.get('fields_of_study')) if 'fields_of_study' in work_json else ''
		keywords = ','.join(work_json.get('keywords')) if 'keywords' in work_json else ''
		mesh_terms = self.__get_meshterms(work_json['mesh_terms']) if 'mesh_terms' in work_json else []
		external_url = work_json.get('external_url')
		citing_patents_count = work_json.get('patent_citations_count')
		references = self.__get_reference(work_json['references']) if 'references' in work_json else ''
		citing_works_count = work_json.get('citing_works_count')
		is_open_access = work_json.get('is_open_access')
		open_access = work_json['open_access'] if 'open_access' in work_json else []
		open_access_license=''
		open_access_colour=''
		if bool(open_access):
			for key, value in open_access.items():
				if key == 'license':
					open_access_license = value
				elif key == 'colour':
					open_access_colour = value

		return Work(lens_id, title, date_published, publication_year, publication_type, source_title, publisher,
					source_country, authors, magid, doi, coreid, patent_citation_lens_ids, abstract,volume,issue_number,
					start_page, end_page, fields_of_study, keywords,mesh_terms, external_url,pmid, pmcid,
					citing_patents_count, references,citing_works_count,is_open_access,open_access_license, 
					open_access_colour)

	def __get_authors(self, authors_json):
		authors = []
		for author in authors_json:
			first_name = author.get('first_name')
			last_name = author.get('last_name')
			initials = author.get('initials')
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
			ids = affiliation['ids'] if 'ids' in affiliation else []
			ror = ''
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

	def __get_reference(self, reference_json):
		references=''
		for  refer in reference_json:
			references += (refer.get('lens_id')) + ','
		return references

