from django.core.management import BaseCommand
from testapp_dcod.models import Data_piece
import csv

class Command(BaseCommand):
	help = "Parsing and saving data."

	def handle(self, *args, **options):
		db = Data_piece.objects.all()
		before_counter = 0
		for a in db:
			before_counter += 1
		print(before_counter)
		with open('/home/ubuntu/Antoha_work_28_03_17/infotech-helpdesk/brokkr/testapp_dcod/eFw3Cefj.csv', newline='') as csv_data:
			writer = csv.reader(csv_data, delimiter=',', quotechar='|')
			next(writer)
			counter = 0
			for row in writer:
				# print(row)
				thing = Data_piece.objects.create(region=row[0], country=row[1], number=row[2])
				thing.save
				counter += 1
		print(counter)
		db = Data_piece.objects.all()
		after_counter = 0
		for a in db:
			after_counter += 1
		print(after_counter)
