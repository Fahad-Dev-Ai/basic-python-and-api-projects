from groq import Groq
client = Groq(api_key = "your key here")
messages=[{"role":"system","content":"you're a bodybuilding coach who helps skinny guys make a lean and big body, also you have to give short advice"}]
while True:
    user = input("you : ")
    messages.append({"role":"user","content":user})
    if user =="exit":
        break
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    messages.append({"role":"assistant","content":response.choices[0].message.content})


    print(response.choices[0].message.content)
