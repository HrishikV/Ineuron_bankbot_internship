import wget
urls=["https://github.com/IBM/watson-banking-chatbot/blob/master/data/conversation/workspaces/full_banking.json","https://github.com/IBM/watson-banking-chatbot/blob/master/data/conversation/workspaces/banking_US.json","https://github.com/IBM/watson-banking-chatbot/blob/master/data/conversation/workspaces/banking_IN.json"]
for url in urls:
    wget.download(url)
