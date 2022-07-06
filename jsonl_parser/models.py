from email.utils import make_msgid

class Work:
	def __init__(self, lens_id, title, publication_type, authors, magid, doi, coreid, patent_citations, abstract):
		self.lens_id = lens_id
		self.title = title
		self.publication_type = publication_type
		self.authors = authors
		self.magid = magid
		self.doi = doi
		self.coreid = coreid
		self.patent_citations = patent_citations
		self.abstract = abstract

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
		