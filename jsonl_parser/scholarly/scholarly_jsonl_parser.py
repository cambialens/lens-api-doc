import json
import os
import sys
from models import Work, Author
from parsers import WorkParser
from writers import WorkCsvWriter
from datetime import date, datetime

start = datetime.now()
json_file = sys.argv[1]
with open(json_file, 'r', encoding='utf-8-sig') as input_file:
	output_location = os.path.join(os.getcwd(), 'output-'+ str(date.today()))
	if not os.path.exists(output_location):
		os.makedirs(output_location)
	work_csv_writer = WorkCsvWriter(output_location)

	try:
		print('Starting csv parser for: {}'.format(json_file))
		work_parser = WorkParser()
		count = 0
		for row in input_file:
			work_json = json.loads(row)
			work = work_parser.parse(work_json)
			work_csv_writer.write(work)
			count += 1
			if (count % 20_000 == 0):
				print('Processed {} records ...'.format(count))
		print('Successfully parsed {} scholarly works in {} seconds into: \n\t{}'.format(count, (datetime.now() - start).total_seconds(), output_location))

	finally:
		work_csv_writer.close()