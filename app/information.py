import result
from openai import OpenAI
import yaml
import google.generativeai as genai
import os

CONFIG_YML = {}
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)( '"

def APPEND_DATA(DATA ,HANDLE):
    with open(DATA, "a") as myfile:
        myfile.write(f"{HANDLE}")

def WRITE_DATA(DATA ,HANDLE):
    f = open(DATA, "w")
    f.write(f"{HANDLE}")
    f.close()

def CONFIG(CONFIG_YML):
    with open("../config.yml") as stream:
        try:
            CONFIG_YML = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(f"parse data from config.yml have error {exc}")
    
    return CONFIG_YML

''' Sample-output-data
Key -   DATA

1   -   ('Hemoglobin', ' (Hb) 12.5Low 13.0 - 17.0 g/dL')
2   -   ('WBC count', ' 90004000-11000cumm')
3   -   ('RBC count', ' 5.2 4.5 - 5.5 mill/cumm')
4   -   ('Platelet Count', '150000Borderline150000 - 410000cumm ')
5   -   ('PCV', ') 57.5High 40 - 50 %')
6   -   ('MCV', ') 87.75 83 - 101fL')
7   -   ('MCH', '27.2 27 - 32 pg')
8   -   ('MCHC', '32.8 32.5 - 34.5g/dL ')
9   -   ('RDW', '13.6 11.6 - 14.0 %')
10  -   ('Neutrophils', ' 60 50 - 62% ')
11  -   ('Lymphocytes', '31 20 - 40%')
12  -   ('Monocytes', '7 00 - 10%')
13  -   ('Eosinophils', ' 1 00 - 06%')
14  -   ('Basophils', '1 00 - 02%')

'''
def GET_TARGET_DATA(index_of):
    valueOfFinal = []
    keys = ""
    for init in result.READ_DATA():
        if int(init.split("|")[0]) == index_of:
            valueOfFinal = init.split(",")[1].split("----")
            for DATA in init.split(",")[1].split("----"):
                for ALPHA in DATA:
                    for NEW_A in alphabet:
                        if ALPHA == NEW_A:
                            keys = keys + ALPHA

                keys = keys + "-"        

    for init in keys.split("-"):
        if init in valueOfFinal:
            valueOfFinal.remove(init)


    return valueOfFinal[0]

"""
The reference range is a set of laboratory values in which 95% of the healthy population is located, 
and these normal figures are determined by collecting a large number of data from laboratory tests.
Blood test results may change with age, gender, race, pregnancy, diet, use of prescription or herbal 
medications, and stress. Reference or normal values often depend on the method of analysis, 
the device and the method of performing the blood test. Also, factors such as inaccuracy, 
lack of standardization, lack of use of authentic kits or materials also affect the test results. 
If the reference population used to generate normal values is small, the values may be inaccurate.
"""

''' this part of core - app.py check of white blood cells (WBC) [
    Neutrophils_COUNT
    Lymphocytes_COUNT
    Monocytes_COUNT
    Eosinophils_COUNT
    Basophils_COUNT
]

'''
# White blood cells - *WBC*
# This part of the program is dedicated to the calculation and 
# interpretation of blood results based 
# on the white blood cell count

Hemoglobin = GET_TARGET_DATA(1)
WBC_COUNT = GET_TARGET_DATA(2) 
RBC_COUNT = GET_TARGET_DATA(3)
Platelet_Count = GET_TARGET_DATA(4)
PCV = GET_TARGET_DATA(5)
MCV = GET_TARGET_DATA(6)
MCH = GET_TARGET_DATA(7)
MCHC = GET_TARGET_DATA(8)
RDW = GET_TARGET_DATA(9)
Neutrophils_COUNT = GET_TARGET_DATA(10)
Lymphocytes_COUNT = GET_TARGET_DATA(11)
Monocytes_COUNT = GET_TARGET_DATA(12)
Eosinophils_COUNT = GET_TARGET_DATA(13)
Basophils_COUNT = GET_TARGET_DATA(14)

"""
White blood cells, also known as leukocytes, are the main component of the body's immune system. 
A high white blood cell count can indicate an infection, while a low count can be due to various autoimmune 
diseases or immunosuppressive conditions, including HIV/AIDS and lupus. Healthy blood contains a certain 
percentage of white blood cells, which varies between people or at different ages.
The normal range of white blood cell counts in a healthy adult is between 4,000 and 11,000 WBCs per microliter (μl or mcL) 
or cubic millimeter of blood. Although this value may be different in men and women and healthy children and young people.

I recently took a blood test and got the following information from the test:

WBC_COUNT = 34 cmmu
Neutrophils_COUNT = 56
Lymphocytes_COUNT = 66
Monocytes_COUNT = 21
Eosinophils_COUNT = 44
Basophils_COUNT = 67

I want you to completely interpret my blood test according to the above information in an accurate and professional manner with a low error rate and tell me how exactly my physical condition is according to the above information and how good I am in terms of blood, such as the number of white blood cells And I am healthy red.

"""

def RESULTـOFـWHITEـBLOODـCELLS(KEY, prompt):
    # This function examines the data received from counting the number of white blood cells 
    # and their subsets in order to compare and match with the general and healthy samples and 
    # declares diseases caused by outliers in the WBC count.
    genai.configure(api_key=f"{KEY}")
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(prompt)
    english_content = response.text

    WRITE_DATA(
        CONFIG(CONFIG_YML).get("results").get("en"),
        english_content
    )
    

prompt = f"""I would like you to give me a small interpretation of my blood test according to this information, what will this information say about my physical health and what is the state of my body that I will bring to my doctor later:

'Hemoglobin', '(Hb) {Hemoglobin}'
'WBC count', '{WBC_COUNT} cumm'
'RBC count', '{RBC_COUNT} mill/cumm'
'Platelet Count', '{Platelet_Count} cumm'
'PCV', '{PCV} %'
'MCV', '{MCV} fL'
'MCH', '{MCH} pg'
'MCHC', '{MCHC} g/dL'
'RDW', '{RDW} %
'Neutrophils', '{Neutrophils_COUNT} %'
'Lymphocytes', '{Lymphocytes_COUNT} %'
'Monocytes', '{Monocytes_COUNT} %
'Eosinophils', '{Eosinophils_COUNT} %'
'Basophils', '{Basophils_COUNT} %

Please write a complete and detailed summary that has full details and your answer must be in Markdown format.
"""

RESULTـOFـWHITEـBLOODـCELLS(
    CONFIG(CONFIG_YML).get("gemini").get("key"),
    prompt
)

APPEND_DATA(
    CONFIG(CONFIG_YML).get("results").get("en"),
    f"""\n\n\n### information:\n\n- Patientــ name : {
        CONFIG(CONFIG_YML).get("patientــName")
    }\n- Age : {
        CONFIG(CONFIG_YML).get("age")
    }\n- Job : {
        CONFIG(CONFIG_YML).get("job")
    }
    """
)

'''

healthy person: between 4,000 and 11,000 WBCs per microliter (μl or mcL)

- Man: between 5000 and 10000
- Women: between 4500 and 11000

Neutrophils: 40 to 60% of the total
Lymphocytes: 20 to 40%
Monocytes: 2 to 8 percent
Eosinophils: 1 to 4%
Basophils: 0.5 to 1%

'''