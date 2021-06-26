# import bisect
import time
import logging

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            return_value = func(*args, **kwargs)
            end_time = time.time()
            # logger = logging.getLogger(func.__name__)
            # logger.warning("Function {} took {} seconds to complete\n".format(func.__name__,end_time-start_time))

            return return_value
        except Exception as e:
            logger = logging.getLogger(func.__name__)
            # print((args),"***************")
            logger.error("Error in {} :".format(func.__name__) + str(e),exc_info=False)

            return e
    return wrapper

bmi_scale =  [0,18.4,  18.5,24.9,  25,29.9,  30,34.9,  35,39.9,  40,10000]

bmi_category = {
    0:{
        "BmiCategory":"Under Weight",
        "HealthRisk":"Malnutrition Risk"
    },
    2:{
        "BmiCategory":"Normal Weight",
        "HealthRisk":"Low Risk"
    },
    4:{
        "BmiCategory":"Over Weight",
        "HealthRisk":"Enhanced Risk"
    },
    6:{
        "BmiCategory":"Moderately Obese",
        "HealthRisk":"Medium Risk"
    },
    8:{
        "BmiCategory":"Severely Obese",
        "HealthRisk":"High Risk"
    },
    10:{
        "BmiCategory":"Very Severely Obese",
        "HealthRisk":"Very High Risk"
    }
}


# print(bisect.bisect_left(bmi_scale,16)-1)
# print(bisect.bisect_left(bmi_scale,20.01)-1)
# print(bisect.bisect_left(bmi_scale,24.8)-1)
# print(bisect.bisect_left(bmi_scale,28)-1)
# print(bisect.bisect_left(bmi_scale,30.01)-1)
# print(bisect.bisect_left(bmi_scale,32)-1)
# print(bisect.bisect_left(bmi_scale,38)-1)
# print(bisect.bisect_left(bmi_scale,40.01)-1)
# print(bisect.bisect_left(bmi_scale,700)-1)
# print(bisect.bisect_right(bmi_scale,35))