import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


# Set up the Groq client with your API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Replace with your actual API key

# Define a function to generate resume content
def generate_resume_content(role, experience, technologies):
    prompt = f"""
    Create a professional resume section for a {role} with {experience} years of experience specializing in {technologies}. 
    Include a brief professional summary and 3-5 bullet points for key responsibilities or achievements. 
    Keep it concise, professional, and tailored to the role. Also have done 5-6 projects in the past 3 years like -
    Project 1: This is a project in which i have implemented a web application for Management system in PowerApps.
    Project 2: This is a project in which i have implemented an application in which we are processing data, manipulating it for some heirarical orders and with the help of pandas inserting it to database.
    Project 3: This is a project in which i have implemented a web application for calculating growth of a horse based on its feed quantity and quality.
    Project 4: This is a project in which i have implemented a Scrum based implementations for resolving client issues in production or if needed than implement new functionalities as well using fastapi and test cases.
    Project 5: This is a project in which i have implemented a web application clinic and pharmacy management system.
    Project 6: This is a project in which i have implemented some functionalities to integrate the python implementation with desktop applications on client server.
    """
    
    # Call the Groq API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # You can use "llama2-70b-4096" or another available model
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,  # Adjust this for longer or shorter output
        temperature=0.7  # Controls creativity (0.5-1.0 is good for professional tone)
    )
    
    # Extract and return the generated text
    return response.choices[0].message.content

# Example usage
role = "Software Engineer"
experience = 3
technologies = "Python, Django, FastAPI, Django Rest Fraemwork, HTML, GIT, SVN, Microsoft PowerApps, SQL, MYSQL, PostgreSQL and Docker"

resume_content = generate_resume_content(role, experience, technologies)
print("Generated Resume Content:\n")
print(resume_content)