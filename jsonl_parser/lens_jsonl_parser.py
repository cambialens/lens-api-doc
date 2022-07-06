import json
import os
import sys
from jsonl_parser.models import Work, Author
from jsonl_parser.parsers import WorkParser
from jsonl_parser.writers import WorkCsvWriter

json_file = sys.argv[1]
with open(json_file, 'r', encoding='utf-8-sig') as input_file:
	output_location = os.path.join(os.getcwd(), 'output')
	if not os.path.exists(output_location):
		os.makedirs(output_location)
	work_csv_writer = WorkCsvWriter(output_location)

	try:
		work_parser = WorkParser()
		for row in input_file:
			work_json = json.loads(row)
			work = work_parser.parse(work_json)
			work_csv_writer.write(work)
	finally:
		work_csv_writer.close()