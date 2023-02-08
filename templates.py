def user_socials_tmp():
    return r'''<a id="card--social" href="{social_link}" target="_blank">{social_name}</a>'''

def user_qualifications_tmp():
    return r'''<li>✔️ {user_qualification}</li>'''

def user_skills_tmp():
    return r'''<div class="card--skills"><span>{user_skill}</span></div>'''

def user_work_responsibilities_tmp():
    return r'''<li>{user_responisibility}</li>'''

def user_work_history_tmp():
    return r'''
    <div class="card--work-history">
        <strong>{user_work_title}</strong>
        <p>{user_work_timeline}</p>
        <ul>
            {user_work_responsibilities}
        </ul>
    </div>

    <div class="line-break"></div> 
'''

def user_education_specifics_tmp():
    return r'''<li>{edu_specific}</li>'''

def user_education_tmp():
    return r'''
    <div class="card--education-history">
        <strong>{user_edu_title}</strong>
        <p>{user_edu_timeline}</p>
        <ul>
            {user_edu_specifics}
        </ul>
    </div>
'''

def user_languages_tmp():
    return r'''<li>{lang_icon} <strong>{lang_name}</strong>: {lang_desc}</li>'''

def user_accomplishments_tmp():
    return r'''                
    <div class="card--accomplishment">
        <a href={accomplishment_link} target="_blank"><span>🏆 </span>{accomplishment_desc}</a>
    </div>
'''

def user_project_desc_tmp():
    return r'''<p>{project_description_paragraph}</p>'''

def user_projects_tmp():
    return r'''
    <div class="row--projects">
        <h3><a href={user_project_link} target="_blank"><span id="project-emote">{user_project_icon} </span> {user_project_title}</a></h3>
        <div class="project-container">
            <a href={user_project_link} target="_blank" class="project-image-link">
                <img src={user_project_image} class="project-image"></img>
            </a>
            <div class="project-description">
                {user_project_description}
            </div>
        </div>
    </div>

    <div class="line-break"></div>
'''