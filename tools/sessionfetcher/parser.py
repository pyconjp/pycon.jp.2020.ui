from typing import List, Dict


def parse_question_answers(answers_data: List[Dict]) -> Dict[str, str]:
    return {answer["question"]: answer["answer"] for answer in answers_data}


def parse_categories(categories_data: List[Dict]) -> Dict[str, str]:
    category_info = {}
    for category in categories_data:
        name = category["name"]
        # いずれもsingle choiceなのでインデックス0を指定する
        value = category["categoryItems"][0]["name"]
        category_info[name] = value
    return category_info
