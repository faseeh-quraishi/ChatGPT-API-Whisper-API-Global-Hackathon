import openai

prompt = {}
all_prompts = []
f =open('GPT-3.5_data.txt','r')
for line in f:
    line = line.strip('\n').split(':')
    prompt[line[0]] = line[1]
    all_prompts.append(prompt)
    prompt = {}
print('\n',all_prompts,'\n')