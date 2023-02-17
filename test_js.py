
import re

text = '''

SKILLS
Web Development
TECHNOLOGIES
Javascript Python
React JS Django
Node JS Firebase
Express JS


ABOUT

I'm a full stack web developer new in this field. At first | was interested in
building Desktop applications using lava, Mysql). But Gradually | learn this
Now it is my Aim to be a great Web Developer who can build websites with
beautiful front-end and also build back-end.

INSTITUTES

Saylani Mass IT Training
Online Course 
Physical Course 



EDUCATION
2020 Sindh Madrassatul Islam University
to Undergraduate BS (Computer Science)

2020 Sindh Muslim Science Govt. College
Intermediate in Pre-Engineering

'''


final_text = ''


final_text += text
Edu = re.search(r'(EDUCATION|Education:?)[\n+]([\w\W]*)[\n+\w:?]\n+',text)
Skills = re.search(r'(SKILLS|Skills:?)\n+([\s\w]+)(?=\n+[A-Z ]+:?\n+)',text)
Intstitute = re.search(r'(INSTITUTES|Intstitutes:?)\n+([\s\w]+)(?:(?=\n+[A-Z ]+:?\n+))',text)
Dic = {"Education": str(Edu.group(2)), "SKILLS": str(Skills.group(2)), 'INSTITUTE': str(Intstitute.group(2)) } 
print(Dic)