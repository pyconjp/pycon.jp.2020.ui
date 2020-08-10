from unittest import TestCase

from sessionfetcher import data as sut


class AnswerItemsCreateTestCase(TestCase):
    def test_should_create(self):
        data_dict = {
            "聴衆に求める前提知識 / Prerequisite knowledge for attending": (
                "前提として、〇〇した経験。\r\nこれがあると理解しやすいでしょう"
            ),
            "Elevator Pitch": "このトークはエレガントに示します",
            "聴衆が持ち帰ることができるもの": "〇〇をPythonで行う方法",
        }

        actual = sut.AnswerItems.create(data_dict)

        self.assertEqual(
            actual,
            sut.AnswerItems(
                "このトークはエレガントに示します",
                "前提として、〇〇した経験。\r\nこれがあると理解しやすいでしょう",
                "〇〇をPythonで行う方法",
            ),
        )


class CategoryItemsCreateTestCase(TestCase):
    def test_should_create(self):
        data_dict = {
            "Track": "Data Science / Machine Learning",
            "Level": "Intermediate",
            "Audience expertise": "0%",
            "Language": "Japanese",
            "発表資料の言語 / Language of presentation material": "Japanese only",
            "Session format": "Talk(45min)",
        }

        actual = sut.CategoryItems.create(data_dict)

        self.assertEqual(
            actual,
            sut.CategoryItems(
                "Talk(45min)",
                "Intermediate",
                "0%",
                "Data Science / Machine Learning",
                "Japanese",
                "Japanese only",
            ),
        )


class talkNumberTestCase(TestCase):
    def test_should_return_no(self):
        expectations = {
            "2020-08-28T11:50:00": 1,
            "2020-08-28T13:45:00": 2,
            "2020-08-28T14:50:00": 3,
            "2020-08-28T16:00:00": 4,
            "2020-08-28T16:50:00": 5,
            "2020-08-28T18:00:00": 6,
            "2020-08-29T11:50:00": 1,
            "2020-08-29T14:00:00": 2,
            "2020-08-29T14:50:00": 3,
            "2020-08-29T16:00:00": 4,
            "2020-08-29T16:30:00": 5,
        }
        for start_at, expected in expectations.items():
            with self.subTest(start_at=start_at, expected=expected):
                actual = sut.talk_number(start_at)
                self.assertEqual(actual, expected)


class SessionCreateTestCase(TestCase):
    def test_should_create(self):
        session_data = {
            "questionAnswers": [
                {"question": "Elevator Pitch", "answer": "エレベーターピッチです"},
                {
                    "question": (
                        "聴衆に求める前提知識 / Prerequisite knowledge for attending"
                    ),
                    "answer": "前提知識です",
                },
                {"question": "聴衆が持ち帰ることができるもの", "answer": "持ち帰ります"},
            ],
            "id": "214734",
            "title": "テストデータプロポーザル",
            "description": "テストデータに使うための\r\nダミープロポーザルです",
            "startsAt": "2020-08-29T14:50:00",
            "endsAt": "2020-08-29T15:20:00",
            "speakers": [{"id": "masked_id_aaa", "name": "Test User"}],
            "categories": [
                {
                    "name": "Session format",
                    "categoryItems": [{"name": "Talk(30min)"}],
                },
                {"name": "Track", "categoryItems": [{"name": "Python core"}]},
                {"name": "Level", "categoryItems": [{"name": "Beginner"}]},
                {"name": "Language", "categoryItems": [{"name": "English"}]},
                {
                    "name": "発表資料の言語 / Language of presentation material",
                    "categoryItems": [{"name": "English only"}],
                },
                {
                    "name": "Audience expertise",
                    "categoryItems": [{"name": "100%"}],
                },
            ],
            "roomId": 14496,
            "room": "#pyconjp_2",
        }

        actual = sut.Talk.create(session_data, 2)

        self.assertEqual(
            actual,
            sut.Talk(
                "214734",
                "テストデータプロポーザル",
                "#pyconjp_2",
                2,
                3,
                "テストデータに使うための\r\nダミープロポーザルです",
                sut.AnswerItems("エレベーターピッチです", "前提知識です", "持ち帰ります"),
                sut.CategoryItems(
                    "Talk(30min)",
                    "Beginner",
                    "100%",
                    "Python core",
                    "English",
                    "English only",
                ),
                ["masked_id_aaa"],
            ),
        )


class SessionAsDictTestCase(TestCase):
    def test_should_return_flat_dict(self):
        talk = sut.Talk(
            "241734",
            "辞書に変換するテストデータ",
            "#pyconjp_1",
            2,
            4,
            "テストデータに使うための\r\nダミープロポーザル",
            sut.AnswerItems("エレベーターピッチ", "前提知識", "持ち帰り"),
            sut.CategoryItems(
                "Talk(15min)",
                "Advanced",
                "0%",
                "Tips of development",
                "Japanese",
                "Japanese only",
            ),
            ["masked_id_bbb"],
        )

        actual = talk.as_dict()

        self.assertEqual(
            actual,
            {
                "id": "241734",
                "title": "辞書に変換するテストデータ",
                "room": "#pyconjp_1",
                "day": 2,
                "no": 4,
                "elevator_pitch": "エレベーターピッチ",
                "prerequisite_knowledge": "前提知識",
                "audience_takeaway": "持ち帰り",
                "talk_format": "Talk(15min)",
                "audience_python_level": "Advanced",
                "audience_expertise": "0%",
                "track": "Tips of development",
                "lang_of_talk": "Japanese",
                "lang_of_slide": "Japanese only",
                "speaker_ids": ["masked_id_bbb"],
                "description": "テストデータに使うための\r\nダミープロポーザル",
            },
        )
