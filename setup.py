from setuptools import setup

setup(
    name='bmi_batch_process',
    url='https://github.com/jagadeesh-r1/code-20210626-jagadeeshreddy',
    author='Jagadeesh Reddy',
    author_email='mail4jagadeeshreddy@gmail.com',
    packages=['BMI'],
    version='0.3',
    license='GNU General Public License v3.0',
    description='This package is used to process BMI (BodyMassIndex) using Height and Weight of person. The input must a iterable of json objects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
