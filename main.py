import json
from templates import *


def to_json():
    data = {
        "web_title": "Antonios-Stefanos Tormpantonis",
        "user_pic_link": "./assets/images/profile_pic.jpg",
        "user_name": "Antonios-Stefanos Tormpantonis",
        "user_bio": "BSc Physics, interested in Data Science and Programming, as well as automation of repeatable tasks, mainly through Python. Recently, I have explored machine learning and neural networks. If you have an employment offer, please contact me at the following e-mail address.",
        "user_email": "antonistorb@yahoo.com",

        "user_socials": [
            ("https://www.linkedin.com/in/antonis-tormp/", "LinkedIn"),
            ("https://github.com/AntonisTorb", "GitHub"),
            ("./assets/CV_generic.pdf", "PDF Resume")
        ],

        "user_qualifications": [
            "2 Years experience in data driven environments.",
            "1.5 Years Purchase to Pay experience.",
            "1.5 Years experience with U.S. Tax requirements, related forms and withholding tax.",
            "Intermediate knowledge of Python, Basics of HTML, CSS, JS and SQL." 
        ],

        "user_skills": [
            "Logical Thinking",
            "Problem Solving",
            "Creativity",
            "Responsibility",
            "Languages",
            "Attention to Detail",
            "Teamwork",
            "Multitasking",
            "Data Analysis",
            "Computer Skills"
        ],

        "user_work_history": [
            {
                "user_work_title": "P2P Associate, Vendor Master Data | Eli Lilly",
                "user_work_timeline": "05/2019 - 10/2020",
                "user_work_responsibilities": [
                    "Main point of contact for the Vendor Master Data sub-process for North America.",
                    "Vendor data maintenance for North America and EMEA.",
                    "Ensuring vendor data remained accurate and compliant with region specific and company regulations.",
                    "Handling of vendor account specific requests through a queue system.",
                    "2nd Tier of escalation for the Vendor Master Data sub-process.",
                    "Testing and quality control on new tools, processes, as well as updates to existing ones.",
                    "Documetation correction and updates as required.",
                    "Compliance reporting and auditing on regular intervals.",
                    "Report generation with specific information when requested.",
                    "Puerto Rican merchant certificate and withholding exemption document validation and handling.",
                    "Employee expense accounts maintenance in SAP.",
                    "Bank data maintenance in SAP.",
                    "Validation and compliance control for Customer Master Data sub-process.",
                    "Troubleshooting payment returns/rejections, and implementing solutions to related issues.",
                    "Knowledge transfer and training new team members and affiliates, including recorded presentations."

                ]
            },

            {
                "user_work_title": "Office Administration | Greek Military Mandatory Service",
                "user_work_timeline": "01/2018 - 10/2018",
                "user_work_responsibilities": [
                    "Protocol number assignment to Military Documents.",
                    "Missing documents recovery by following Protocol.",
                    "Incoming and outgoing Military Mail handling.",
                    "Special handling of top secret and confidential documents.",
                    "Military service duty schedule planning.",
                    "Issuing of Military documents as required (medical referrals, leave of absence documents, military personnel transportation tickets, draft documents).",
                    "Daily report generation on the status of the unit and its members.",
                    "Personnel database management (Microsoft Access environment).",
                    "Military document archiving.",
                    "Communications (electronic mail and phone calls)."
                ]
            },

            {
                "user_work_title": "High School level Physics and Mathematics private lessons | Self",
                "user_work_timeline": "09/2012 - 06/2013",
                "user_work_responsibilities": ["Knowledge transfer in preparation for the national university entry exams."]
            }

        ],

        "user_education": [
            {
                "user_edu_title": "BSc, Physics (8 Semesters, 249 ECTS) | Aristotle University of Thessaloniki",
                "user_edu_timeline": "09/2010 - 07/2017",
                "user_edu_specifics": [
                    "Graduation grade of 7.23/10.",
                    "Knowledge acquisition in advanced Mathematics, Data Analysis and multiple fields of Physics.",
                    "Main field in Nuclear Physics and Elementary Particles.",
                    "Exceptional performance in laboratory courses."
                ]
            }
        ],

        "user_languages": [
            ("🇬🇷", "Greek", "Native. High everyday usage, high confidence."),
            ("🇬🇧", "English", "IELTS General Training (01/2019), Overall Score: 8/9 (C1 level). High everyday usage, high confidence."),
            ("🇩🇪", "German", "Zertifikat B2 (05/2009), Overall Score: 80.5/100. Very low circumstantial usage, low confidence.")
        ],

        "user_accomplishments": [
            ("./assets/images/eeom.jpeg", "Received the Employee of the Month award for October 2019 during my employment with Eli Lilly."),
            ("./assets/images/army.jpg", "Received 14 additional days of honorary leave awarded for my contributions during my military service.")
        ],

        "user_projects": [
            {
                "user_project_title": "This website",
                "user_project_icon": "🌐",
                "user_project_link": "https://github.com/AntonisTorb/AntonisTorb.github.io",
                "user_project_image": "./assets/images/website.jpg",
                "user_project_description": [
                    "A small scale static website acting as a digital resume, where I can showcase all the relevant information for my proffessional career.",
                    "I started with a template by following a tutorial, and slowly added features by researching the relevant HTML, CSS and JS code.",
                    "Please also check out the <a href='https://github.com/AntonisTorb/website-generator' target='_blank'>Python Website Generator script</a> that I am using to update the content of this website."

                ]
            },

            {
                "user_project_title": "Simple Neural Network",
                "user_project_icon": "🤖",
                "user_project_link": "https://github.com/AntonisTorb/Simple-Neural-Network",
                "user_project_image": "./assets/images/snn.jpg",
                "user_project_description": [
                    "My first attempt at understanding neural networks, I created my own, simple version of one with Python, as well as some example applications.",
                    "I started by following a tutorial written in JavaScript, which I refactored on the go to Python. I then enhanced it by allowing the user to modify the number of hidden layers, as well as train the model in mini-batches.",
                    "Still a work in progress, as I intend to optimise it further, as well as create an optical character recognition (OCR) application around it."
                ]
            },

            {
                "user_project_title": "EnMasse Email",
                "user_project_icon": "📫",
                "user_project_link": "https://github.com/AntonisTorb/EnMasse-email",
                "user_project_image": "./assets/images/enmasse.jpg",
                "user_project_description": [
                    "An application written in Python that is capable of sending multiple e-mails automatically with a high degree of customization.",
                    "The user provides a template with placeholder text, as well as a file containing the data to replace said placeholders.",
                    "Inspiration for this project was my previous job with Eli Lilly, where I had to contact several vendors for the same issue, but could not automate it at the time."
                ]
            },

            {
                "user_project_title": "DummPy",
                "user_project_icon": "🗔",
                "user_project_link": "https://github.com/AntonisTorb/dummPy",
                "user_project_image": "./assets/images/dummpy.jpg",
                "user_project_description": [
                    "An application written in Python that can produce dummy data of several different types.",
                    "The user can provide samples of data that will be used by the application to produce different combinations as specified. The user can then save the data to an excel or .csv file.",
                    "This was my first application in Python, and I created it so I can use the data generated as practice for future data analysis projects."
                ]
            },

            {
                "user_project_title": "DisInfected",
                "user_project_icon": "🕹️",
                "user_project_link": "https://github.com/AntonisTorb/DisInfected",
                "user_project_image": "./assets/images/disinfected.jpg",
                "user_project_description": [
                    "A small and simple top down videogame written in JavaScript and displayed on HTML canvas.",
                    "My first project with programming languages, after following a tutorial on making videogames, between graduating University and the beginning my military service.",
                    "You can find a playable demo <a href='https://antonistorb.github.io/DisInfected/' target='_blank'>here</a>."

                ]
            }
        ]

    }

    with open("webcontent.json", "w") as json_file:
        json.dump(data, json_file)


def json_load():
    with open("webcontent.json", "r") as json_file:
        return json.load(json_file)


def generate_html():
    data = json_load()

    web_title = data["web_title"]
    user_pic_link = data["user_pic_link"]
    user_name = data["user_name"]
    user_bio = data["user_bio"]
    user_email = data["user_email"]

    user_socials = ""
    for social_link, social_name in data["user_socials"]:
        social = user_socials_tmp().format(social_link=social_link, social_name=social_name)
        user_socials = f"{user_socials}\n{social}"

    user_qualifications = ""
    for user_qualification in data["user_qualifications"]:
        qualification = user_qualifications_tmp().format(user_qualification=user_qualification)
        user_qualifications = f"{user_qualifications}\n{qualification}"

    user_skills = ""
    for user_skill in data["user_skills"]:
        skill = user_skills_tmp().format(user_skill=user_skill)
        user_skills = f"{user_skills}\n{skill}"

    user_work_history = ""
    for position in data["user_work_history"]:
        user_work_title = position["user_work_title"]
        user_work_timeline = position["user_work_timeline"]
        user_work_responsibilities_list = position["user_work_responsibilities"]
        user_work_responsibilities = ""
        for user_responisibility in user_work_responsibilities_list:
            responsibility = user_work_responsibilities_tmp().format(user_responisibility=user_responisibility)
            user_work_responsibilities = f"{user_work_responsibilities}\n{responsibility}"
        work_history= user_work_history_tmp().format(
            user_work_title=user_work_title,
            user_work_timeline=user_work_timeline,
            user_work_responsibilities=user_work_responsibilities
        )
        user_work_history = f"{user_work_history}\n{work_history}"

    user_education = ""
    for education in data["user_education"]:
        user_edu_title = education["user_edu_title"]
        user_edu_timeline = education["user_edu_timeline"]
        user_edu_specifics_list = education["user_edu_specifics"]
        user_edu_specifics = ""
        for edu_specific in user_edu_specifics_list:
            specific = user_education_specifics_tmp().format(edu_specific=edu_specific)
            user_edu_specifics = f"{user_edu_specifics}\n{specific}"
        education = user_education_tmp().format(
            user_edu_title=user_edu_title,
            user_edu_timeline=user_edu_timeline,
            user_edu_specifics=user_edu_specifics
        )
        user_education = f"{user_education}\n{education}"
    
    user_languages = ""
    for lang_icon, lang_name, lang_desc in data["user_languages"]:
        language = user_languages_tmp().format(lang_icon=lang_icon, lang_name=lang_name, lang_desc=lang_desc)
        user_languages = f"{user_languages}\n{language}"

    user_accomplishments = ""
    for accomplishment_link, accomplishment_desc in data["user_accomplishments"]:
        accomplishment = user_accomplishments_tmp().format(accomplishment_link=accomplishment_link, 
                                                           accomplishment_desc=accomplishment_desc)
        user_accomplishments = f"{user_accomplishments}\n{accomplishment}"

    user_projects = ""
    for user_project in data["user_projects"]:
        user_project_title = user_project["user_project_title"]
        user_project_icon = user_project["user_project_icon"]
        user_project_link = user_project["user_project_link"]
        user_project_image = user_project["user_project_image"]
        user_project_description_list = user_project["user_project_description"]
        user_project_description = ""
        for project_description_paragraph in user_project_description_list:
            description_paragraph = user_project_desc_tmp().format(
                project_description_paragraph=project_description_paragraph)
            user_project_description = f"{user_project_description}\n{description_paragraph}"
        project = user_projects_tmp().format(
            user_project_title=user_project_title,
            user_project_icon=user_project_icon,
            user_project_link=user_project_link,
            user_project_image=user_project_image,
            user_project_description=user_project_description
        )
        user_projects = f"{user_projects}\n{project}"


    with open("template.html", "r", encoding="utf8") as file:
        template = file.read().format(
            web_title=web_title,
            user_pic_link=user_pic_link,
            user_name=user_name,
            user_bio=user_bio,
            user_email=user_email,
            user_socials=user_socials,
            user_qualifications=user_qualifications,
            user_skills=user_skills,
            user_work_history=user_work_history,
            user_education=user_education,
            user_languages=user_languages,
            user_accomplishments=user_accomplishments,
            user_projects=user_projects
        )
    with open("index.html", "w", encoding="utf8") as website:
        website.write(template)


if __name__ == "__main__":
    #to_json()
    generate_html()