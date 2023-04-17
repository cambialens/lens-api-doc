# Scholarly JSONL to CSV Parser

This project parses Scholarly jsonl file exported from The Lens into object model defined in `models.py` and produces csv files for works, authors, affiliations and mesh terms. 

## How to use it

`python scholarly_jsonl_parser.py lens-export.jsonl`

After execution of the script, csv files are created in the current working directory inside a new folder named `output-yyyy-mm-dd` in a relational schema. Scholarly work can be joined with its authors and affiliations using `lens_id` and `author_sub_id`. `author_sub_id` is just a serial number for the authors of that record.

## Output Schema

### works.csv

Field | Description | Example
---- | --- | ---
`Lens ID` | Unique Lens Identifier  | `000-032-744-027-385`
`Title` | Title of the scholarly work | `Fidget Spinner`
`Date Published` | Date of publication | `2019-04-04T00:00:00000000+00:00`
`Publication Year` | Year of publication | `2019`
`Publication Type` | Publication Type eg. Journal Article etc | `journal article`
`Source Title` | Name of source publication in which the scholarly work appears | `Doing More with Less`
`ISSNs` | International Standard Serial Number of the source publication | `27754030`
`Publisher` |  | `Springer New York`
`Source Country` | Publisher’s country | `United Kingdom`
`Abstract` | Abstract text | 
`Volume` | Journal volume | `5`
`Issue Number` | The journal issue | `1`
`Start Page` | Start Page in the journal | `33`
`End Page` | End Page in the Journal | `49`
`Fields of Study` | Fields of study determined by Microsoft Academic | `Economy;Tourism`
`Keywords` | Keywords for the scholarly work from PubMed | `policy`
`Chemicals` | Name of the chemical substance | `Anti-HIV Agents`
`Funding` | Funding Organisation | `National Science Foundation`
`Source URLs` | Source Urls |
`External URL` |   |
`PMID` | PubMed identifier associated with the scholarly work | `21838587`
`DOI` | Crossref Digital Identifier associated with the scholarly work | `10.52137/humanis.v6i1.03`
`Microsoft Academic ID` | Microsoft Academic identifier associated with the scholarly work | `3139075244`
`PMCID` | PubMed central identifier associated with the scholarly work | `pmc7901867`
`Citing Patents Count` | Number of patents that cite a scholarly work | `5`
`References` | Lens Id of the scholarly works cited | `007-899-176-416-740`
`Citing Works Count` | Number of scholarly works that cite a given scholarly work | `10`
`Is Open Access` | Flags if the scholarly work has is Open Access | `TRUE`
`Open Access License` | Open Access license type | `cc-by`
`Open Access Colour` | Open Access colour category | `gold`


### authors.csv

Field | Description | Example
---- | --- | ---
`lens_id` | Unique Lens Identifier | `000-032-744-027-385`
`author_sub_id` | Serial number for the author of given scholarly work | `1`
`first_name` | Author’s first name | `David`
`last_name` | Author’s last name | `Smith`
`initials` | Author's Initials | `D`
`magid` | Author’s MAGID | `2779337967`
`orcidid`| Author’s ORCID | `0000-0001-5352-4498`

### author_affiliations.csv

Field | Description | Example
---- | --- | ---
`lens_id` | Unique Lens Identifier | `000-032-744-027-385`
`author_sub_id` | Serial number for the author of given scholarly work | `1`
`name` | author’s affiliated institution and address | `Institut Agama Islam Negeri Lhokseumawe`
`ror` | The institution ROR identifier | `https://ror.org/02teq1165`
`grid_id` | Affiliation grid id | `grid.251313.7`
`country_code` | Alpha-2 country code of the author’s institution | `US`

### mesh_terms.csv

Field | Description | Example
---- | --- | ---
`lens_id` | Unique Lens Identifier | `000-032-744-027-385`
`mesh_id` | Unique MeSH identifiers for  names of the substance | `D010808`
`mesh_heading` | Medical subject headings assigned to PubMed entries | `Physical Examination`
`qualifier_id` | Mesh Term Qualifier ID | `Q000662`
`qualifier_name` | Mesh Term Qualifier Name | `veterinary`