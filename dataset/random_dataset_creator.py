import random as r
import numpy as np
import names
import pandas as pd


def genereate_phone_no():
    ph_no = ""
    ph_no = ph_no + str(r.randint(7, 9))
    for i in range(1, 10):
        ph_no = ph_no + str(r.randint(0, 9))
    return int(ph_no)


gender_classifier = {0: 'male', 1: 'female'}
cust_df = pd.DataFrame()
cust_df['cust_id'] = 1
cust_df['name'] = "laura"
cust_df["phone_number"] = ""
cust_df['password'] = ""
credit_df = pd.DataFrame(np.random.randint(0, 100, size=(1000, 3)), columns=['cust_id', 'credit_balance', 'due'])
debit_df = pd.DataFrame(np.random.randint(0, 100, size=(1000, 2)), columns=['cust_id', 'balance'])
for index, row in credit_df.iterrows():
    cust_df.at[index, 'cust_id'] = index + 1
    credit_df.at[index, 'cust_id'] = index + 1
    debit_df.at[index, 'cust_id'] = index + 1
    cust_df.at[index, 'password'] = "1234"
    cust_df.at[index, 'name'] = names.get_first_name(gender=gender_classifier[r.randint(0, 1)])
    cust_df.at[index, 'phone_number'] = str(genereate_phone_no())
    credit_df.at[index, 'credit_balance'] = r.randint(1000, 100000)
    credit_df.at[index, 'due'] = r.randint(1000, 50000)
    debit_df.at[index, 'balance'] = r.randint(0, 100000)
cust_df.to_csv('./cust_df.csv', header=True)
credit_df.to_csv('./credit_df.csv', header=True)
debit_df.to_csv('./debit_df.csv', header=True)
