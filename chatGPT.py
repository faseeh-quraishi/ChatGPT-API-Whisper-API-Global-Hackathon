def chatGPT():
    import openai

    prompt = {}
    JSON_format = []
    # 
    f =open('GPT-3.5_data.txt','r')
    for line in f:
        line = line.strip('\n').split(':')
        prompt['role'] = line[0]
        prompt['content'] = line[1]
        JSON_format.append(prompt)
        prompt = {}
    for i in JSON_format:
        print('\n',i,'\n')
    openai.api_key = open('OpenAI-API.txt').readline()

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=JSON_format
    )

    response = open('GPT-3.5_data.txt','a+')
    input = '\nuser: '+completion.choices[0].message
    response.write(input)
    # print(completion.choices[0].message)



chatGPT()

