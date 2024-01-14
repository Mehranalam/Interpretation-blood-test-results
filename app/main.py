from tabulate import tabulate
from PyPDF2 import PdfReader
import sqlite3

DATA_PROPERTI = {}

def store_data(data):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    ''' DATA_QUERY '''
    cur.execute(
        "DATA_QUERY"
        )

    '''
        This function collects the test data 
        by receiving detailed information and stores it in the database [ SQlite ]

    ''' 

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
    

def find_usable_data(final_get_data, query):
    
    REQUESTED_INFORMATION = ""
    
    '''
    
    By sending requested requests, the data will be divided in better details 
    and placed more easily in the database.
    
    '''
    RAW = final_get_data.find(query)
    INIT = 0
    while INIT < len(final_get_data):        
        if final_get_data[RAW+INIT] == "\n":
            break
        
        REQUESTED_INFORMATION = REQUESTED_INFORMATION + final_get_data[RAW+INIT]

        INIT += 1
        
        
    
    print(REQUESTED_INFORMATION)


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
above 2 functions, the data is processed by 
the Bing-DALL_E engine and analyzed with a good prompt, 
and the result is generated and processed as a .pdf file.

'''


RAW_DATA = get_data_from_user("../assets/input/complete-blood-count-CBC.pdf")
find_usable_data(RAW_DATA ,"RBC")