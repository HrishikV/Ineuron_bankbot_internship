import json
import bot_banking_functtions as bbf


def get_banking_intent(text):
    rule_data_file = './dataset/rules.json'
    with open(rule_data_file, 'r') as f:
        rule_dict = json.load(f)
    for i in rule_dict['intents']:
        for ext in i['examples']:
            if text == ext['text']:
                return i['intent']


def get_output(intent, output="output"):
    rule_data_file = './dataset/rules.json'
    output = str(output)
    with open(rule_data_file, 'r') as f:
        rule_dict = json.load(f)
        for i in rule_dict["outputs"]:
            if i["intent"] == intent:
                return i[output]


def account_balance(cust_id, acctype=None):
    if acctype is None:
        return "enter account type", 0
    elif acctype == "credit":
        balance, due = bbf.return_credit_details(cust_id)
        return get_output("accountbalance") + " " + str(balance) + ", " + str(-due), -1
    elif acctype == "debit":
        balance = bbf.check_balance(cust_id)
        return get_output("accountbalance") + " " + str(balance), -1
    else:
        return "Invalid acc type", 0


def fund_transfer(cust_id, bef_id=None, amount=None):
    if bef_id is None:
        return "enter Beneficiary id", 0
    elif amount is None:
        return "Enter amount", 1
    else:
        return get_output("FundTransfer", bbf.acc_transfer(cust_id, bef_id, amount)), -1


def credit_use(cust_id, amount=None):
    if amount is None:
        return "enter amount", 1
    else:
        transfer = bbf.credit_use(cust_id, amount)
        if transfer is not False:
            return (transfer + " is the new balance " + amount + " has been credited to your account") - 1
        else:
            return "Insufficient credit", -1


def main():
    n = 0
    c = 0
    while 1:
        l = []
        if n == 0:
            print("How may I help you")
            text = input()
            intent = get_banking_intent(text)
        if c == 0:
            print("Enter customer ID and Password")
            cust_id, password = input().split()
            cust_id = int(cust_id)
            print(type(cust_id), type(password))
            check = bbf.check_user(cust_id, password)
            print(check)
        if check:
            c = 1
            while 1:
                if intent == "accountbalance":
                    if not l:
                        output, r = account_balance(cust_id)
                        print(output)
                        l.append(input().lower())
                    else:
                        output, to = account_balance(cust_id, l[0])
                        print(output)
                        if to == -1:
                            break
                elif intent == "register":
                    print(get_output(intent)[0])
                    break
                elif intent == "nonsense":
                    print("Please don't waste your time here")
                    break
                elif intent == "discoTerms":
                    print(get_output(intent)[0])
                    break
                elif intent == "FundTransfer":
                    if len(l) < 1:
                        output, r = fund_transfer(cust_id)
                        print(output)
                        l.append(int(input()))
                    elif len(l) < 2:
                        output, r = fund_transfer(cust_id, l[0])
                        print(output)
                        l.append(int(input()))
                    else:
                        output = fund_transfer(cust_id, l[0], l[1])
                        print(output[0])
                        break
                elif intent == "representative":
                    print(get_output(intent)[0])
                    break
                elif intent == "LostCard":
                    """put in a function to deactivate the card"""
                    print(get_output(intent)[0])
                    break
                elif intent == "Forgotpassword":
                    print(get_output(intent)[0])
                    break
                elif intent == "OK":
                    n = 1
                    print(get_output(intent)[0])
                    break
        else:
            print("Invalid credentials")
        if n != 0:
            break
