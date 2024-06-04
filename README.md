### Interpretation-blood-test-results
[![CodeQL](https://github.com/Mehranalam/Interpretation-blood-test-results/actions/workflows/codeql.yml/badge.svg)](https://github.com/Mehranalam/Interpretation-blood-test-results/actions/workflows/codeql.yml)


An open source project for the interpretation of blood test results, by receiving information such as WBC and RBC, interprets the test result completely automatically.

This project is just a small step to do a big thing. This project protects the privacy and vital information of the body [blood test] by receiving the information and storing it once in the database and also by encrypting the data in the database.

#### setup


```bash
cd app
pip install -r requirements.txt
```
#### Quick start

```bash
python main.py
python result.py
python information.py
```

- `main.py` core of project and setup input pdf and manage database
- `result.py` This file acts as a bridge between the data classification process and the final interpretation of the blood tests. 
It helps to ensure that the results are based on a solid foundation of data analysis and that any anomalies or errors are identified and 
corrected before the tests are interpreted. By utilizing this file, medical professionals can 
have greater confidence in the accuracy of their blood test results, which can ultimately lead to better patient outcomes.
- `information.py` last step for procces data and push to OpenAI & Google Gemini

Sample output: [result/](/results)

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
