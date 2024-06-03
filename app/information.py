import result
from openai import OpenAI

client = OpenAI(api_key='open_ai_key')
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)( '"


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

WBC_COUNT = GET_TARGET_DATA(2) 
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
"""

print(Neutrophils_COUNT)


def RESULTـOFـWHITEـBLOODـCELLS():
    # This function examines the data received from counting the number of white blood cells 
    # and their subsets in order to compare and match with the general and healthy samples and 
    # declares diseases caused by outliers in the WBC count.
    TODO
    

def call_chatgpt(prompt):
    response = client.chat.completions.create(model="gpt-4",  # You can use "gpt-3.5-turbo" if you're on that model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150)
    return response.choices[0].message.content

prompt = "How do I integrate ChatGPT into my Python application? to md file."
response = call_chatgpt(prompt)
print(response)
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