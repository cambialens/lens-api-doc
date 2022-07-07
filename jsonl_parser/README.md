# lens-jsonl-parser
 Parse lens scholarly export and convert to csv

This project takes json file, parses into object model and produces csv files as output.

### Test
`python lens_jsonl_parser.py lens-export.jsonl` 

It creates output directory in the working directory. Separate files for author and author affiliation are created along with scholarly works. To join scholarly work with author and affiliation, lens_id and author_sub_id should be used. auther_sub_id is just a serial number for the author of that record.

### __get_authors
takes author's json file to return authors.

### _get_affiliations
returns the affiliation of the individual author. 