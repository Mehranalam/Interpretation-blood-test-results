import result


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
print(result.READ_DATA())
def GET_TARGET_DATA(index_of):
    for init in result.READ_DATA():
        SPLITED = init.split(",")
        SPLITED_BY_KEY = int(SPLITED[0].split("-")[0])
        if SPLITED_BY_KEY == index_of:
            FINAL_DATA = SPLITED[1].replace(" " ,"")
            return FINAL_DATA.replace(")" ,"")


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
print(Lymphocytes_COUNT)

def RESULTـOFـWHITEـBLOODـCELLS():
    # goood
    TODO

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
