import json
import os
import sys
from model import Patent
from patent_parser import PatentParser
from writers import PatentCsvWriter
from datetime import date, datetime

start = datetime.now()
try:
	input_jsonl_file = sys.argv[1]
except IndexError:	 
	raise ValueError('Please provide JSONL file.')

output_csv_file = sys.argv[2] if len(sys.argv) > 2 else 'output.csv'
with open(input_jsonl_file, 'r', encoding='utf-8-sig') as input_file:
	output_location = os.path.join(os.getcwd(), 'output-'+str(date.today()))
	if not os.path.exists(output_location):
		os.makedirs(output_location)

	output_file = '{}/{}'.format(output_location, output_csv_file)
		
	with open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
		print('Starting Patent csv parser for: {}'.format(input_jsonl_file))
		patent_csv_writer = PatentCsvWriter(csv_output)
		patent_parser = PatentParser()
		count = 0
		for row in input_file:
			patent_json = json.loads(row)
			patent = patent_parser.parse(patent_json)
			patent_csv_writer.write(patent)
			count += 1
			if (count % 20_000 == 0):
				print('Processed {} records ...'.format(count))
		print('Successfully parsed {} patents in {} seconds into: \n\t{}'.format(count, (datetime.now() - start).total_seconds(), output_location))
			