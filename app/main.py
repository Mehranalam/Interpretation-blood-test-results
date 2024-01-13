import sqlite3
from tabulate import tabulate

DATA_PROPERTI = {}

def store_data(data):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    ''' DATA_QUERY '''
    cur.execute("DATA_QUERY")

    '''
    This function collects the test data 
    by receiving detailed information and stores it in the database [ SQlite ]

    ''' 

def get_data_from_user(data_input):
    NON_PRECCES = input("Please Enter All of data with SPACE: [Such as WBC RBC HCT .etc]")
    DATA_LIST = NON_PRECCES.split(" ")

    DATA_PROPERTI["WBC"] = DATA_LIST[0]
    DATA_PROPERTI["RBC"] = DATA_LIST[1]
    DATA_PROPERTI["HCT"] = DATA_LIST[2]
    DATA_PROPERTI["MCV"] = DATA_LIST[3]
    DATA_PROPERTI["MCH"] = DATA_LIST[4]

    print(tabulate([
                        ['WBC', DATA_PROPERTI.get('WBC')],
                        ['RBC', DATA_PROPERTI.get('RBC')],
                        ['HCT', DATA_PROPERTI.get('HCT')],
                        ['MCV', DATA_PROPERTI.get('MCV')],
                        ['MCH', DATA_PROPERTI.get('MCH')]
                        
                    ], headers=['Data', 'Value'], tablefmt='orgtbl'))


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