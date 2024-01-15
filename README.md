### Interpretation-blood-test-results
[![CodeQL](https://github.com/Mehranalam/Interpretation-blood-test-results/actions/workflows/codeql.yml/badge.svg)](https://github.com/Mehranalam/Interpretation-blood-test-results/actions/workflows/codeql.yml)


An open source project for the interpretation of blood test results, by receiving information such as WBC and RBC, interprets the test result completely automatically.

<img src="/assets/INTRO.jpg"/>


This project is just a small step to do a big thing. This project protects the privacy and vital information of the body [blood test] by receiving the information and storing it once in the database and also by encrypting the data in the database.

The data is classified in an orderly manner and after receiving the information, it will deliver the interpretation and output in the form of a .pdf file after a few minutes.

```python
RAW_DATA = get_data_from_user("../assets/input/complete-blood-count-CBC.pdf")
find_usable_data(RAW_DATA ,"RBC")
```

- [https://geekymedics.com/fbc-interpretation/](https://geekymedics.com/fbc-interpretation/)
- [assets/input/complete-blood-count-CBC.pdf](https://github.com/Mehranalam/Interpretation-blood-test-results/blob/main/assets/input/complete-blood-count-CBC.pdf)


#### Dataset of Blood test sample [Drlogy Healthcare organization]

- [Blood Report Format: CBC, Hb, ESR, RBC, WBC, Blood Smear ](https://drlogy.com/blog/blood-report-format)