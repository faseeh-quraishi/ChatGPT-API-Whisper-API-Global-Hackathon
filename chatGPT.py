import openai

prompt = {}
messages = []
# 
f =open('GPT-3.5_data.txt','r')
for line in f:
    line = line.strip('\n').split(':')
    prompt[line[0]] = line[1]
    messages.append(prompt)
    prompt = {}
for i in messages:
    print('\n',i,'\n')