import json


def get_banking_intent(text):
    rule_data_file = './dataset/rules.json'
    with open(rule_data_file, 'r') as f:
        rule_dict = json.load(f)
    for i in rule_dict['intents']:
        for ext in i['examples']:
            if text == ext['text']:
                return i['intent']


def get_output(text):
    rule_data_file = './dataset/rules.json'
    with open(rule_data_file, 'r') as f:
        rule_dict = json.load(f)
