from unittest import TestCase
from unittest.mock import patch

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
    def test_should_return_talk_no(self):
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

    def test_should_return_none_to_non_talk_contents(self):
        # トークではないコンテンツやキーノートにはnoがつかない
        non_talk_start_time_list = [
            "2020-08-28T10:00:00",
            "2020-08-28T10:30:00",
            "2020-08-28T12:45:00",
            "2020-08-28T15:20:00",
            "2020-08-28T18:30:00",
            "2020-08-29T10:00:00",
            "2020-08-29T10:30:00",
            "2020-08-29T13:00:00",
            "2020-08-29T15:20:00",
            "2020-08-29T17:15:00",
            "2020-08-29T18:15:00",
        ]
        for start_at in non_talk_start_time_list:
            actual = sut.talk_number(start_at)
            self.assertIsNone(actual)


class SessionCreateTestCase(TestCase):
    def test_should_create_talk(self):
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
        day = 2

        actual = sut.Talk.create(session_data, day)

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

    def test_should_create_non_talk_contentswhen_includes_blank(self):
        # トークではないコンテンツはプロポーザルの項目が当てはまらず、空欄を含む
        session_data = {
            "questionAnswers": [
                {"question": "Elevator Pitch", "answer": None},
                {
                    "question": (
                        "聴衆に求める前提知識 / Prerequisite knowledge for attending"
                    ),
                    "answer": None,
                },
                {"question": "聴衆が持ち帰ることができるもの", "answer": None},
            ],
            "id": "215382",
            "title": "ブランクありテストデータ",
            "description": "ブランクのある\r\nダミープロポーザルです",
            "startsAt": "2020-08-28T15:20:00",
            "endsAt": "2020-08-28T16:00:00",
            "speakers": [{"id": "masked_id_bbb", "name": "Staff"}],
            "categories": [
                {"name": "Session format", "categoryItems": []},
                {"name": "Track", "categoryItems": []},
                {"name": "Level", "categoryItems": []},
                {"name": "Language", "categoryItems": [{"name": "Japanese"}]},
                {
                    "name": "発表資料の言語 / Language of presentation material",
                    "categoryItems": [{"name": "Japanese only"}],
                },
                {"name": "Audience expertise", "categoryItems": []},
            ],
            "roomId": 14495,
            "room": "#pyconjp",
        }
        day = 1

        actual = sut.Talk.create(session_data, day)

        self.assertEqual(
            actual,
            sut.Talk(
                "215382",
                "ブランクありテストデータ",
                "#pyconjp",
                1,
                None,  # noはトークのためのもの
                "ブランクのある\r\nダミープロポーザルです",
                sut.AnswerItems(None, None, None),
                sut.CategoryItems(
                    None, None, None, None, "Japanese", "Japanese only"
                ),
                ["masked_id_bbb"],
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


class InvitedTalkCreateTestCase(TestCase):
    def test_should_create(self):
        session_data = {
            "questionAnswers": [
                {"question": "Elevator Pitch", "answer": "招待講演のエレベーターピッチ"},
                {
                    "question": (
                        "聴衆に求める前提知識 / Prerequisite knowledge for attending"
                    ),
                    "answer": None,
                },
                {"question": "聴衆が持ち帰ることができるもの", "answer": None},
            ],
            "id": "213320",
            "title": "招待講演テストデータ",
            "description": "招待講演の情報を\r\nスタッフが入力しました",
            "startsAt": "2020-08-28T13:45:00",
            "endsAt": "2020-08-28T14:30:00",
            "speakers": [{"id": "masked_id_ddd", "name": "PyCon JP"}],
            "categories": [
                {
                    "name": "Session format",
                    "categoryItems": [{"name": "Talk(45min)"}],
                },
                {
                    "name": "Track",
                    "categoryItems": [
                        {"name": "Data Science / Machine Learning"}
                    ],
                },
                {"name": "Level", "categoryItems": []},
                {"name": "Language", "categoryItems": [{"name": "Japanese"}]},
                {
                    "name": "発表資料の言語 / Language of presentation material",
                    "categoryItems": [{"name": "Japanese only"}],
                },
                {"name": "Audience expertise", "categoryItems": []},
            ],
            "roomId": 14816,
            "room": "#pyconjp_1",
        }
        day = 1

        actual = sut.InvitedTalk.create(session_data, day)

        self.assertIsInstance(actual, sut.Talk)
        self.assertEqual(
            actual,
            sut.InvitedTalk(
                "213320",
                "招待講演テストデータ",
                "#pyconjp_1",
                1,
                2,
                "招待講演の情報を\r\nスタッフが入力しました",
                sut.AnswerItems("招待講演のエレベーターピッチ", None, None),
                sut.CategoryItems(
                    "Invited talk(45min)",
                    None,
                    None,
                    "Data Science / Machine Learning",
                    "Japanese",
                    "Japanese only",
                ),
                ["masked_id_ddd"],
            ),
        )


class CreateStaffEnteredContentsTestCase(TestCase):
    @patch("sessionfetcher.data.Talk.create")
    def test_should_return_talk(self, talk_create):
        session_data = {
            "questionAnswers": [
                {"question": "Elevator Pitch", "answer": None},
                {
                    "question": (
                        "聴衆に求める前提知識 / Prerequisite knowledge for attending"
                    ),
                    "answer": None,
                },
                {"question": "聴衆が持ち帰ることができるもの", "answer": None},
            ],
            "id": "214735",
            "title": "スタッフ作成コンテンツ",
            "description": "スタッフが作成した\r\nキーノート・招待講演以外のコンテンツです",
            "startsAt": "2020-08-29T10:00:00",
            "endsAt": "2020-08-29T10:30:00",
            "speakers": [{"id": "masked_id_ccc", "name": "Staff"}],
            "categories": [
                {"name": "Session format", "categoryItems": []},
                {"name": "Track", "categoryItems": []},
                {"name": "Level", "categoryItems": []},
                {"name": "Language", "categoryItems": [{"name": "Japanese"}]},
                {
                    "name": "発表資料の言語 / Language of presentation material",
                    "categoryItems": [{"name": "Japanese only"}],
                },
                {"name": "Audience expertise", "categoryItems": []},
            ],
            "roomId": 14495,
            "room": "#pyconjp",
        }
        day = 2

        actual = sut.create_staff_entered_contents(session_data, day)

        self.assertEqual(actual, talk_create.return_value)
        talk_create.assert_called_once_with(session_data, day)

    @patch("sessionfetcher.data.InvitedTalk.create")
    def test_should_return_invited_talk(self, invited_talk_create):
        session_data = {
            "questionAnswers": [
                {"question": "Elevator Pitch", "answer": "招待講演のエレベーターピッチ"},
                {
                    "question": (
                        "聴衆に求める前提知識 / Prerequisite knowledge for attending"
                    ),
                    "answer": None,
                },
                {"question": "聴衆が持ち帰ることができるもの", "answer": None},
            ],
            "id": "213316",
            "title": "招待講演テストデータ その2",
            "description": "招待講演の情報を\r\nスタッフが入力しました",
            "startsAt": "2020-08-28T14:50:00",
            "endsAt": "2020-08-28T15:20:00",
            "speakers": [{"id": "masked_id_eee", "name": "PyCon JP"}],
            "categories": [
                {
                    "name": "Session format",
                    "categoryItems": [{"name": "Talk(30min)"}],
                },
                {
                    "name": "Track",
                    "categoryItems": [
                        {"name": "Data Science / Machine Learning"}
                    ],
                },
                {"name": "Level", "categoryItems": []},
                {"name": "Language", "categoryItems": [{"name": "Japanese"}]},
                {
                    "name": "発表資料の言語 / Language of presentation material",
                    "categoryItems": [{"name": "Japanese only"}],
                },
                {"name": "Audience expertise", "categoryItems": []},
            ],
            "roomId": 14816,
            "room": "#pyconjp_1",
        }
        day = 1

        actual = sut.create_staff_entered_contents(session_data, day)

        self.assertEqual(actual, invited_talk_create.return_value)
        invited_talk_create.assert_called_once_with(session_data, day)
