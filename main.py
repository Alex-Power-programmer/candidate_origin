from flask import Flask

import utils

apper = Flask(__name__)
candidates = utils.load_candidates()


@apper.route('/')
def page_index():
    str_candidate = "<pre>"
    for candidate in candidates.values():
        str_candidate += f"{candidate['name']} \n {candidate['position']} \n {candidate['skills']} \n\n"
    str_candidate += "</pre>"
    return str_candidate


@apper.route('/candidates/<int:id>')
def profile(id):
    candidate = candidates[id]
    str_profile = f"<img src={candidate['picture']}></img> <br><br>{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']} <br><br>\n\n"
    return str_profile


@apper.route('/skills/<skill>')
def skills(skill):
    str_candidate = '<pre>'
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(", ")
        candidate_skills = [i.lower() for i in candidate_skills]
        if skill.lower() in candidate_skills:
            str_candidate += f'{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n'
    str_candidate += '</pre>'

    return str_candidate


apper.run()
