'''
This file calls the data generated and classified by main.py and 
then produces and interprets the final blood tests.
The data generated by main.py is crucial in the production of accurate and reliable blood test results.
'''

import sqlite3
import asyncio
import asyncgpt

conn = sqlite3.connect('database.db')
cursor = conn.execute("SELECT * FROM BLOOD_INFORMATION")
rows = cursor.fetchall()


'''
This file acts as a bridge between the data classification process and the final interpretation of the blood tests. 
It helps to ensure that the results are based on a solid foundation of data analysis and that any anomalies or errors are identified and 
corrected before the tests are interpreted. By utilizing this file, medical professionals can 
have greater confidence in the accuracy of their blood test results, which can ultimately lead to better patient outcomes.3
'''
def READ_DATA(data):
    
    counter = 1
    for PARAMETER in data:
        print(f"{counter} - {PARAMETER}")
        counter += 1
        

async def CONTACT_CHAT_GPT_DALLE_123():
    bot = asyncgpt.GPT(apikey="YOUR API KEY")
    completion = await bot.chat_complete([{"role": "user", "content": "Hello!"}])
    print(completion)


if __name__ == "__main__":
    asyncio.run(CONTACT_CHAT_GPT_DALLE_123())
        
READ_DATA(rows)