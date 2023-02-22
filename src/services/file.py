import csv
from io import StringIO
from typing import BinaryIO


class FileService:
    @staticmethod
    def upload(file: BinaryIO):
        reader = csv.DictReader((line.decode() for line in file))
        for row in reader:
            print(row)
            
    @staticmethod
    def download():
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=["id", "name", "age"])
        writer.writeheader()
        writer.writerow({"id": 3, "name": "Alina", "age": None})
        output.seek(0)
        return output
