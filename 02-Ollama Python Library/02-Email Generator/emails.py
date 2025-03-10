import ollama
import os

input='./data/internship.txt'
output='./data/emails.txt'

model="llama3.2"

if not os.path.exists(input):
    print(f"the file {input} not existing ")
    exit(1)

with open(input,'r') as f:
    items=f.read().strip()

print(items)

prom =f"""
You are a specialized email writer that helps people find internships and write the emails needed for each position and company .

here you will find the list containing the company and the field of the internship needed this way
    company : field
    {items}
    What you will do:
1-You will write for each company an email to say that you are proficient in the field associated to the company .
2-You will give some tools that are used in the field and say that You master it in the email  so that the email can be sent directly .
3- You will give  all the emails separated by *****NEXT EMAIL ********.
4- Your Name is Yosra Hindaoui
5- the emails will be sent directly so don't let any space where i should change something
""" 
res=ollama.generate(model=model, prompt=prom)
generated_text=res.get("response","")
print(generated_text)

with open(output,'w') as f:
    f.write(generated_text.strip())
