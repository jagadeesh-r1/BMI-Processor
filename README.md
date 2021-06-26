# code-20210626-jagadeeshreddy

# Body Mass Index Batch Processor


[![made-with-python](https://img.shields.io/badge/v0.0.2%20-bmi_processor-1f425f.svg)](https://pypi.org/project/bmi-batch-process/)

This Package is used to calculate BMI and Categorise the BMI in 5 Classes.
## Tech

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
 
 Example:
   ```python3
   processed_results = obj.process_start('input_file.json', 'output_path.json')   
   ```

## License

GNU v3
