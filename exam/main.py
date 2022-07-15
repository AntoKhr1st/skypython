from flask import Flask

from exam.util import load_candidates, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = load_candidates()
    result = ''
    for can in candidates:
        result += f'<pre> {can["name"]} \n {can["position"]} \n {can["skills"]} \n</pre>'

    return result


@app.route('/candidates/<int:uid>/')
def candidate_pk_page(uid):
    can = get_by_pk(uid)
    url = can['picture']
    return f"<img src='{url}'><pre>{can['name']}\n{can['position']}\n{can['skills']}</pre>"


@app.route('/skills/<skill>/')
def candidate_skill_page(skill):
    candidates_list = get_by_skill(skill)
    result = ''
    for can in candidates_list:
        result += f'<pre> {can["name"]} \n {can["position"]} \n {can["skills"]} \n</pre>'
    return result


app.run()
