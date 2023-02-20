
#THIS IS A TEST1 FILE
#This should be deleted after testing. 

import openai

final_text = ''
test_string = '''
Im A. Spartan
San Jose, CA 95192 | (408) 555-5555 | imaspartan@gmail.com | linkedin/in/imaspartan

OBJECTIVE: Seeking internship in full-stack development

EDUCATION
B.S., Software Engineering May 20XX
San José State University, San Jose, CA, GPA: 3.8

A.S., Computer Science Jun 20XX
DeAnza College, Cupertino, CA, GPA: 3.7

TECHNICAL SKILLS

Programming: Java, Git, C, Python, PHP, JavaScript, CSS, Swift, Firebase, MySQL
Frameworks: AngularJS, React

OS: Unix/Linux, iOS

Remote: Zoom, Google Meets, Slack, Discord

RELATED EXPERIENCE

Software Developer, Making Software, San Jose, CA Jul 20XX - Present
e Co-created company with two other engineers to make software application

e Manage iOS project and develop software, creating first iOS application to tell stories

e Oversee software application as project manager using Waterfall Agile process models

e Manage web development projects and maintain company machines, virus scans, data backup/retrieval

Math, Physics & Computer Science Tutor, DeAnza College, Cupertino, CA Aug 20XX - Jun 20XX
e Provided private tutoring to students in variety of subjects including Trigonometry, Calculus, Linear Analytics

e Improved students’ performance in math, computer science and physics courses

e Implemented a team oriented tutoring environment using creative ways to help students master concepts

PROJECT EXPERIENCE (More projects available at https://github.com/imaspartan)

EatRight — HackDavis, Virtual Jan 20XX

¢« Followed agile methodology and built a program designed to return the amount of calories in a specific food through       
Amazon Echo, using Python, Node.js, and Amazon AWS

¢« Led team via virtual event platform by assigning tasks and plotting out plan to follow, utilizing scrum approach to       
maximize usage of time

GroceriesNow, San Jose, CA Aug 20XX - Dec 20XX
¢« Developed an iOS application in Swift where users can simplify ordering groceries to their location

« Managed customer accounts using Firebase, along with a customer's order details and location

¢« Created function so users can check location and status of grocery order through Apple Maps

ACTIVITIES & ORGANIZATIONS

Computer History Museum, Won $1000 at Hackathon Camp, iOS Development Jun 20XX - Aug 20XX
Facebook, Attended Hackathon Camp Apr 20XX
Event Coordinator, Software & Computer Engineering Society (SCE) Sept 20XX - Present
Member, SJSU Robotics Team Jan 20XX - Present
Volunteer, FoodRunners Mar 20XX - Dec 20XX

SJSU cnt
'''




final_text += test_string


# Define OpenAI API key 
openai.api_key = "api_key"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = final_text + "Please give me the all the data with respective headings as keys. Only dictionary format"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
print(type(response))
