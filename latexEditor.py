import os
import subprocess
import re
import sys


def replace_whole_words_in_section(tex_path, output_path, sections_titles, replacements):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for section_title in sections_titles:
        # Find the section by title
        section_pattern = rf"(\\section\{{{re.escape(section_title)}\}})(.*?)(?=\\section|\\end{{document}}|$)"
        match = re.search(section_pattern, content, re.DOTALL)

        if not match:
            print(f"Section '{section_title}' not found.")
            return

        section_header, section_body = match.groups()

        # Replace only whole words in the section body
        for old, new in replacements.items():
            section_body = re.sub(rf"\b{re.escape(old)}\b", new, section_body)

        # Rebuild the full LaTeX file
        content = content[:match.start()] + section_header + section_body + content[match.end():]

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


# Usage
input_tex_java = "D:/Resumes/ResumeEditor/Resume_Template_Java_3.tex"
input_tex_python = "D:/Resumes/ResumeEditor/Resume_Template_Python_3.tex"
input_tex_devops = "D:/Resumes/ResumeEditor/Resume_Template_devops.tex"
input_tex_devops_py = "D:/Resumes/ResumeEditor/Resume_Template_devops_Py.tex"
output_tex = "D:/Resumes/Resumes/Tailored/Resume_Pradnya_Chaudhari.tex"
OUTPUT_PDF_PATH = "D:/Resumes/Resumes/Tailored/Resume_Pradnya_Chaudhari.pdf"

skill_replacements = {
    # "Angular": "AngularJS",
    # "Java": "Java 11",
    # "Spring Boot": "SpringBoot",
    # "Go": "Golang",
    # "Go": "Go, Shell Scripting",
    # "React": "ReactJS",
    # "PostgreSQL": "Postgres",
    # "HTML": "HTML5",
    # "CSS": "CSS3",
    # "MongoDB": "Mongo",
    "Django, Flask, Node.js": "Microservice Architecture",  # only for java
    # "Node.js": "NodeJS",
    # ", Node.js": "",
    "TDD": "Test-Driven Development",
    # 'Bash': 'Shell Scripting',    # Only for devops
    # "Kubernetes": 'K8s',
    ", Groovy": "",
    # "Oracle": "PL/SQL"
}

work_replacements = {
    # "React": "Angular",
    # "React": "ReactJS",
    # "Angular": "AngularJS",
    # "Java": "Java 11",
    # "Spring Boot": "SpringBoot",
    # "REST": "RESTful"
    # "Go": "Golang",
    # "Kafka": "Apache Kafka"
    # "PostgreSQL": "Postgres",
    # "REST APIs": "RESTful APIs",
    # "CI/CD": "CICD",
    # "HTML": "HTML5",
    # "CSS": "CSS3",
    # "microservice": "micro-service",
    # "microservices": "micro-services",
    # "Microservices": "Micro-services",
    # "Linux": "UNIX",
    # "MongoDB": "Mongo",
    # "full-stack": "full-service stack",
}

section_titles = [
    # "Technical Skills",
    # "Professional Summary",
    "Work Experience",
    "Project Experience"
]

skill_titles = [
    "Technical Skills",
]

num = int(sys.argv[1])
# print(num, " ", type(num))

input_tex = input_tex_java

if num == 1:
    input_tex = input_tex_java
elif num == 2:
    input_tex = input_tex_python
elif num ==3:
    input_tex = input_tex_devops
elif num == 4:
    input_tex = input_tex_devops_py

replace_whole_words_in_section(input_tex, output_tex, section_titles, work_replacements)
replace_whole_words_in_section(output_tex, output_tex, skill_titles, skill_replacements)

# Compile .tex to .pdf using pdflatex (or xelatex)
subprocess.run(
    ["pdflatex", "-output-directory", os.path.dirname(OUTPUT_PDF_PATH), output_tex],
    check=True
)
