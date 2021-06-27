# code-20210626-jagadeeshreddy

# Body Mass Index Batch Processor


[![made-with-python](https://img.shields.io/badge/v0.3%20-bmi_processor-1f425f.svg)](https://pypi.org/project/bmi-batch-process/)

This Package is used to calculate BMI and categorise the BMI in to 6 classes (i.e, Under Weight,Normal Weight,Over Weight,Moderately Obese,Severely Obese,Very Severely Obese) along with their health risks.

## Development

Python

- Written code to take input as json file and dump results in to a new json file
- Using Pytest for checking the functionality of methods for every update
- Using Github Actions to publish the package.


## Installation

```
pip install bmi-batch-process
```

## Usage 
 - import BodyMassIndex package
    ```python3
    from BMI.bmi_processer import BodyMassIndex
    ```
 - Create an object for the class
    ```python3
    obj  = BodyMassIndex()
    ```
 - Input file example
   ```python3
   # the input must be an iterable of json objects
   [
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
      ...
   ]
   ```
 Example:
   ```python3
   processed_results = obj.process_start('input_file.json', 'output_path.json')   
   ```
## Task 2

Counting No of OverWeight people can be done by the following

- import count_overweight function
    ```python3
    from BMI.count_overweight import count_overweight
    ```
- give the processed records file as input
    ```python3
    count_overweight('path of processed records')
    #prints the no of over weight people
    ```

## License

GNU v3
