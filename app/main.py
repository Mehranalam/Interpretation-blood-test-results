from PyPDF2 import PdfReader
import sqlite3

DATA_PROPERTI = {}

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

def STORE_DATA(RAW_DATA):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    
    
    try:
        cur.execute(
        "CREATE TABLE BLOOD_INFORMATION(Bloodـfactors, data)"
        )
        
        ''' DATA_QUERY '''    
        counter = 0
        for DATA_PROTECT in QUERY_B:
            DATA_PROPERTI[DATA_PROTECT] = FIND_USABLE_DATA(
                RAW_DATA ,
                QUERY_B[counter]
            )
            
            counter += 1

        data = []

        DATA_REPLACE = 0
        while DATA_REPLACE < len(DATA_PROPERTI):
            data.append(
                (QUERY_B[DATA_REPLACE], DATA_PROPERTI[QUERY_B[DATA_REPLACE]])
            )
        
            DATA_REPLACE += 1
        
        cur.executemany(
            "INSERT INTO BLOOD_INFORMATION VALUES(?, ?)"
            ,data
        )
        
    except sqlite3.OperationalError:
        print("ERROR:[ database.db ] file is available\nThere is a problem creating the database.\nYou probably created the database before because the [ database.db ] file is available. Please delete the [ database.db ] or run the [ result.py ] file.")
        
    '''
        This function collects the test data 
        by receiving detailed information and stores it in the database [ SQlite ]

    ''' 
    
    con.commit()  # Remember to commit the transaction after executing INSERT.

def get_data_from_user(data_input):
    
    text = []
    
    '''
        The data is received by pdf files in the assets section 
        and the data is analyzed by the PDFQuery library and 
        stored in a list and the output is published.
        
    '''
    with open(data_input, 'rb') as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()

    
    return text
    

def FIND_USABLE_DATA(final_get_data, query):
    
    REQUESTED_INFORMATION = ""
    
    '''
    
    By sending requested requests, the data will be divided in better details 
    and placed more easily in the database.
    
    '''
    RAW = final_get_data.find(query)
    INIT = 0
    while INIT < len(final_get_data):        
        if final_get_data[RAW + INIT] == "\n":
            break
        
        REQUESTED_INFORMATION = REQUESTED_INFORMATION + final_get_data[RAW+INIT]

        INIT += 1
        
        
    
    REQUESTED_INFORMATION = REQUESTED_INFORMATION.replace("  ", "")
    return REQUESTED_INFORMATION.replace(query, "")


    '''

    This function will display the data in the form of a table 
    by receiving the information under the terminal and regularly deliver the data to the database.

        | Data   |      Value    |

        | WBC    |       34      |
        | RBC    |       43      |
        | HCT    |       23      |
        | MCV    |       12      |
        | MCH    |       45      |

    ''' 

'''

After receiving and correctly classifying the information by the 
above 2+ functions, the data is processed by 
the Bing-DALL_E engine and analyzed with a good prompt, 
and the result is generated and processed as a .pdf file.

'''

RAW_DATA = get_data_from_user(
    "../assets/input/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf"
)

STORE_DATA(RAW_DATA)