### Interpretation-blood-test-results
[![CodeQL](https://github.com/Mehranalam/Interpretation-blood-test-results/actions/workflows/codeql.yml/badge.svg)](https://github.com/Mehranalam/Interpretation-blood-test-results/actions/workflows/codeql.yml)


An open source project for the interpretation of blood test results, by receiving information such as WBC and RBC, interprets the test result completely automatically.

This project is just a small step to do a big thing. This project protects the privacy and vital information of the body [blood test] by receiving the information and storing it once in the database and also by encrypting the data in the database.

The data is classified in an orderly manner and after receiving the information, it will deliver the interpretation and output in the form of a .pdf file after a few minutes.

The main aim of this project is to make the interpretation of blood test results more accessible and convenient for patients. The traditional method of interpreting blood test results requires patients to visit a physician, who then analyzes the results and explains them to the patient. This process can be time-consuming, expensive, and may not be feasible for patients who live in remote areas.

With the help of this open source project, patients can receive the results of their blood tests and interpret them from the comfort of their own homes. This project is not only convenient, but it also ensures the privacy of the patient's information, which is crucial when it comes to sensitive medical data.

Moreover, the project is designed to be flexible and customizable, allowing different medical institutions to tailor it to their specific needs. This means that hospitals, clinics, and other medical facilities can use this open source project to improve their own blood test interpretation processes.

In conclusion, this project is a game-changer in the medical industry, making the interpretation of blood test results more accessible, convenient, and secure for patients. It is a small step towards a bigger goal of revolutionizing the healthcare industry and improving the lives of patients.

```python
# Blood factors needed to interpret laboratory data 
# data dynamic geting from PDF file.

QUERY_B = [
    "Hemoglobin",
    "WBC count",
    "RBC count",
    "Platelet Count",
    "PCV",
    "MCV",
    "MCH",
    "MCHC",
    "RDW",
    "Neutrophils",
    "Lymphocytes",
    "Monocytes",
    "Eosinophils",
    "Basophils"
]
```

- [https://geekymedics.com/fbc-interpretation/](https://geekymedics.com/fbc-interpretation/)
- [CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf](https://github.com/Mehranalam/Interpretation-blood-test-results/blob/main/assets/input/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf)


#### Dataset of Blood test sample [Drlogy Healthcare organization]

- [Blood Report Format: CBC, Hb, ESR, RBC, WBC, Blood Smear ](https://drlogy.com/blog/blood-report-format)
