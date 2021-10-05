from django.db import models
 
# Create your models here.
class Features(models.Model):
    age = models.CharField("age", max_length=255, blank = True, null = True)
    sex = models.CharField("sex", max_length=255, blank = True, null = True)
    cp   = models.CharField(" chest pain type", max_length=255, blank = True, null = True)
    resting_bp = models.CharField("resting blood pressure", max_length=255, blank = True, null = True)
    serum_cholesterol = models.CharField("serum cholesterol", max_length=255, blank = True, null = True)
    fasting_blood_sugar = models.CharField("fasting blood sugar", max_length=255, blank = True, null = True)
    resting_ecg = models.CharField("resting ecg results ", max_length=255, blank = True, null = True)
    max_heart_rate = models.CharField("max heart rate", max_length=255, blank = True, null = True)
    exercise_induced_angina = models.CharField("exercise induced angina", max_length=255, blank = True, null = True)
    st_depression = models.CharField("st depression", max_length=255, blank = True, null = True)
    st_slope = models.CharField("slope of the peak exercise ST segment", max_length=255, blank = True, null = True)
    number_of_vessels = models.CharField("number of Major vessels ", max_length=255, blank = True, null = True)
    thallium_scan_results = models.CharField("thalassemia", max_length=255, blank = True, null = True)
