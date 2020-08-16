from unittest import TestCase

from sessionfetcher import parser as sut


class ParseQuestionAnswersTestCase(TestCase):
    def test_should_parse_into_dict(self):
        data = [
            {
                "id": 21746,
                "question": "Elevator Pitch",
                "questionType": "Long_Text",
                "answer": "人を惹きつけるエレベータピッチ。",
                "sort": 0,
                "answerExtra": None,
            },
            {
                "id": 21756,
                "question": (
                    "聴衆に求める前提知識 / Prerequisite knowledge for attending"
                ),
                "questionType": "Long_Text",
                "answer": "といった前提知識があると理解しやすいと思います。",
                "sort": 5,
                "answerExtra": None,
            },
            {
                "id": 22090,
                "question": "聴衆が持ち帰ることができるもの",
                "questionType": "Long_Text",
                "answer": "・あるパッケージについての知識\r\n・別のパッケージをうまく使う方法",
                "sort": 6,
                "answerExtra": None,
            },
        ]

        actual = sut.parse_question_answers(data)

        self.assertEqual(
            actual,
            {
                "Elevator Pitch": "人を惹きつけるエレベータピッチ。",
                "聴衆に求める前提知識 / Prerequisite knowledge for attending": (
                    "といった前提知識があると理解しやすいと思います。"
                ),
                "聴衆が持ち帰ることができるもの": "・あるパッケージについての知識\r\n・別のパッケージをうまく使う方法",
            },
        )

    def test_should_parse_when_includes_none(self):
        data = [
            {
                "id": 21746,
                "question": "Elevator Pitch",
                "questionType": "Long_Text",
                "answer": None,
                "sort": 0,
                "answerExtra": None,
            },
            {
                "id": 21756,
                "question": (
                    "聴衆に求める前提知識 / Prerequisite knowledge for attending"
                ),
                "questionType": "Long_Text",
                "answer": None,
                "sort": 5,
                "answerExtra": None,
            },
            {
                "id": 22090,
                "question": "聴衆が持ち帰ることができるもの",
                "questionType": "Long_Text",
                "answer": None,
                "sort": 6,
                "answerExtra": None,
            },
        ]

        actual = sut.parse_question_answers(data)

        self.assertEqual(
            actual,
            {
                "Elevator Pitch": None,
                "聴衆に求める前提知識 / Prerequisite knowledge for attending": None,
                "聴衆が持ち帰ることができるもの": None,
            },
        )


class ParseCategoriesTestCase(TestCase):
    def test_should_parse_into_dict(self):
        data = [
            {
                "id": 21742,
                "name": "Session format",
                "categoryItems": [{"id": 49048, "name": "Talk(30min)"}],
                "sort": 1,
            },
            {
                "id": 21743,
                "name": "Track",
                "categoryItems": [
                    {
                        "id": 50366,
                        "name": (
                            "Anything else basically which doesn’t fall into "
                            "the types of topics above"
                        ),
                    }
                ],
                "sort": 2,
            },
            {
                "id": 21744,
                "name": "Level",
                "categoryItems": [{"id": 50340, "name": "Expert"}],
                "sort": 3,
            },
            {
                "id": 21745,
                "name": "Language",
                "categoryItems": [{"id": 49057, "name": "Japanese"}],
                "sort": 8,
            },
            {
                "id": 21752,
                "name": "発表資料の言語 / Language of presentation material",
                "categoryItems": [{"id": 49087, "name": "Both"}],
                "sort": 9,
            },
            {
                "id": 22089,
                "name": "Audience expertise",
                "categoryItems": [{"id": 50343, "name": "100%"}],
                "sort": 4,
            },
        ]

        actual = sut.parse_categories(data)

        self.assertEqual(
            actual,
            {
                "Session format": "Talk(30min)",
                "Track": (
                    "Anything else basically which doesn’t fall into the "
                    "types of topics above"
                ),
                "Level": "Expert",
                "Language": "Japanese",
                "発表資料の言語 / Language of presentation material": "Both",
                "Audience expertise": "100%",
            },
        )

    def test_should_parse_when_includes_empty_items(self):
        data = [
            {
                "id": 21742,
                "name": "Session format",
                "categoryItems": [],
                "sort": 1,
            },
            {"id": 21743, "name": "Track", "categoryItems": [], "sort": 2},
            {"id": 21744, "name": "Level", "categoryItems": [], "sort": 3},
            {
                "id": 21745,
                "name": "Language",
                "categoryItems": [{"id": 49057, "name": "English"}],
                "sort": 8,
            },
            {
                "id": 21752,
                "name": "発表資料の言語 / Language of presentation material",
                "categoryItems": [{"id": 49087, "name": "English only"}],
                "sort": 9,
            },
            {
                "id": 22089,
                "name": "Audience expertise",
                "categoryItems": [],
                "sort": 4,
            },
        ]

        actual = sut.parse_categories(data)

        self.assertEqual(
            actual,
            {
                "Session format": None,
                "Track": None,
                "Level": None,
                "Language": "English",
                "発表資料の言語 / Language of presentation material": "English only",
                "Audience expertise": None,
            },
        )
