import json
from tqdm import tqdm

def count_overweight(file_name):
    with open(file_name,'rb') as input_file:
        records = json.load(input_file)
    counter = 0
    for i in tqdm(records):
        if i.get("BmiCategory") == "Over Weight":
            counter += 1
    print("No of overweight people in records is :",counter)
    