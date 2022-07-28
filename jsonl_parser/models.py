class Work:
	def __init__(self, lens_id, title, date_published, publication_year,publication_type, source_title, publisher, 
				source_country, authors, magid, doi, coreid, patent_citations,abstract, volume, issue_number,start_page, 
				end_page, fields_of_study, keywords, mesh_terms, external_url,pmid, microsoft_academic_id, pmcid,
				citing_patents_count, references, citing_works_count, is_open_access,open_access_license, open_access_colour):
		self.lens_id = lens_id
		self.title = title
		self.date_published = date_published
		self.publication_year = publication_year
		self.publication_type = publication_type
		self.source_title = source_title
		self.publisher = publisher
		self.source_country = source_country
		self.authors = authors
		self.magid = magid
		self.doi = doi
		self.coreid = coreid
		self.patent_citations = patent_citations
		self.abstract = abstract
		self.volume = volume
		self.issue_number = issue_number
		self.start_page = start_page
		self.end_page = end_page
		self.fields_of_study = fields_of_study
		self.keywords = keywords
		self.mesh_terms = mesh_terms
		self.external_url = external_url
		self.pmid = pmid
		self.microsoft_academic_id = microsoft_academic_id
		self.pmcid = pmcid
		self.citing_patents_count = citing_patents_count
		self.references = references
		self.citing_works_count = citing_works_count
		self.is_open_access = is_open_access
		self.open_access_license = open_access_license
		self.open_access_colour = open_access_colour


class Author:
	def __init__(self, first_name, last_name, initials, magid, affiliations):
		self.first_name = first_name
		self.last_name = last_name
		self.initials = initials
		self.magid = magid
		self.affiliations = affiliations

class Affiliation:
	def __init__(self, name, magid, grid, ror, grid_id, country_code):
		self.name = name
		self.magid = magid
		self.grid = grid
		self.ror = ror
		self.grid_id = grid_id
		self.country_code = country_code

class MeshTerms:
	def __init__(self, mesh_id, mesh_heading, qualifier_id, qualifier_name):
		self.mesh_id = mesh_id
		self.mesh_heading = mesh_heading
		self.qualifier_id = qualifier_id
		self.qualifier_name = qualifier_name