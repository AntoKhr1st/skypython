import json


def load_candidates():
    '''возвращает содержимое файла'''
    with open('candidates.json', 'r', encoding='utf-8') as f:
        content = f.read()
        data = json.loads(content)
    return data


def get_all(candidates_list):
    '''распечатывает всех кандидатов из переданного списка'''
    for i in candidates_list:
        print(i)


def get_by_pk(pk):
    '''возвращает кандидата по переданному номеру pk'''
    candidate_pk = {}
    candidates_list = load_candidates()
    for i in candidates_list:
        if i['pk'] == pk:
            candidate_pk = i
    return candidate_pk


def get_by_skill(skill_name):
    '''возвращает список кандидатов с нужным скилом'''
    candidates_list = load_candidates()
    candidates_with_spec_skill = []
    for candidate in candidates_list:
        if skill_name in candidate['skills']:
            candidates_with_spec_skill.append(candidate)
    return candidates_with_spec_skill