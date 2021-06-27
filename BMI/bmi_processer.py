import json
import bisect
from typing import List
from tqdm import tqdm
from .constants import bmi_scale,bmi_category,catch_exceptions

class BodyMassIndex:
    """
    Class contains functions to calculate,categorise BMI.
    """
    def __init__(self) -> None:
        pass

    @catch_exceptions
    def convert_cm_to_m(self,height : float) -> float:
        """
        This function takes height in CMs and returns heights in meters
        """
        return height/100.0 

    @catch_exceptions
    def calculate_bmi(self,record : json) -> json:
        """
        record : {
                    "Gender":"Male",
                    "HeightCm":171,
                    "WeightKg":96
            }
        
        BMI = Weight / (Height ** 2) (Kgs/m^2)
        """
        height = self.convert_cm_to_m(record.get("HeightCm"))
        weight = record.get("WeightKg")
        BMI = round(weight / (height**2),2)
        
        #bisect_left gives the left most index where the calculated BMI falls on the scale, this index is inturn used to retrieve BMI category.
        #0.01 is deliberatly added while getting index inorder to get correct index on edge cases.
        bmi_info = bmi_category.get(bisect.bisect_left(bmi_scale,(BMI+0.01))-1) 
        
        bmi_info["BMI"] = BMI
        return bmi_info

    @catch_exceptions
    def process_data(self,records : List) -> List:
        """
        records : [
                {
                    "Gender":"Male",
                    "HeightCm":171,
                    "WeightKg":96
                },
                {
                    "Gender":"Male",
                    "HeightCm":161,
                    "WeightKg":85
                },
        ]
        Takes records and processes and returns updated records.
        """
        for i in tqdm(records):
            i.update(self.calculate_bmi(i))
        return records

    @catch_exceptions
    def process_start(self,input_file_path : str ,output_file_path : str):
        """
        input_file_path : input json file path
        output_file_path : path to dump the processed data.
        """
        if input_file_path == None or output_file_path  == None:
            raise Exception("Input file or Output file paths does not exist")
        
        with open(input_file_path,'rb') as input_file:
            input_records = json.load(input_file)

        processed_data = self.process_data(input_records)

        with open(output_file_path,'w') as outfile:
            json.dump(processed_data,outfile,indent=4)

BMI = BodyMassIndex()