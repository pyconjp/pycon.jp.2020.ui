from unittest import TestCase
from unittest.mock import MagicMock, patch

from sessionfetcher import core as sut


class FetchTalksAsDictTestCase(TestCase):
    @patch("sessionfetcher.core.http.fetch_response")
    def test_should_return_talks(self, fetch_response):
        sessions_uri, speakers_uri = MagicMock(spec=str), MagicMock(spec=str)

        fetch_response.side_effect = [
            [
                {
                    "sessions": [
                        {
                            "questionAnswers": [
                                {
                                    "question": "Elevator Pitch",
                                    "answer": "招待講演のエレベーターピッチ",
                                },
                                {
                                    "question": (
                                        "聴衆に求める前提知識 / Prerequisite knowledge "
                                        "for attending"
                                    ),
                                    "answer": None,
                                },
                                {
                                    "question": "聴衆が持ち帰ることができるもの",
                                    "answer": None,
                                },
                            ],
                            "id": "213320",
                            "title": "招待講演テストデータ",
                            "description": (
                                "〇〇氏による招待講演です\r\nhttp://example.com/blog\r\n"
                                "-----\r\n〇〇氏のプロフィール。\r\nプロフィールが続きます"
                            ),
                            "startsAt": "2020-08-28T13:45:00",
                            "endsAt": "2020-08-28T14:30:00",
                            "speakers": [
                                {"id": "masked_id_ddd", "name": "PyCon JP"}
                            ],
                            "categories": [
                                {
                                    "name": "Session format",
                                    "categoryItems": [{"name": "Talk(45min)"}],
                                },
                                {
                                    "name": "Track",
                                    "categoryItems": [
                                        {
                                            "name": (
                                                "Data Science / "
                                                "Machine Learning"
                                            )
                                        }
                                    ],
                                },
                                {"name": "Level", "categoryItems": []},
                                {
                                    "name": "Language",
                                    "categoryItems": [{"name": "Japanese"}],
                                },
                                {
                                    "name": (
                                        "発表資料の言語 / Language of presentation "
                                        "material"
                                    ),
                                    "categoryItems": [
                                        {"name": "Japanese only"}
                                    ],
                                },
                                {
                                    "name": "Audience expertise",
                                    "categoryItems": [],
                                },
                            ],
                            "roomId": 14816,
                            "room": "#pyconjp_1",
                        },
                    ]
                },
                {
                    "sessions": [
                        {
                            "questionAnswers": [
                                {"question": "Elevator Pitch", "answer": None},
                                {
                                    "question": (
                                        "聴衆に求める前提知識 / Prerequisite knowledge "
                                        "for attending"
                                    ),
                                    "answer": None,
                                },
                                {
                                    "question": "聴衆が持ち帰ることができるもの",
                                    "answer": None,
                                },
                            ],
                            "id": "214735",
                            "title": "スタッフ作成コンテンツ",
                            "description": "スタッフが作成した\r\nキーノート・招待講演以外のコンテンツです",
                            "startsAt": "2020-08-29T10:00:00",
                            "endsAt": "2020-08-29T10:30:00",
                            "speakers": [
                                {"id": "masked_id_ccc", "name": "PyCon JP"}
                            ],
                            "categories": [
                                {
                                    "name": "Session format",
                                    "categoryItems": [],
                                },
                                {"name": "Track", "categoryItems": []},
                                {"name": "Level", "categoryItems": []},
                                {
                                    "name": "Language",
                                    "categoryItems": [{"name": "Japanese"}],
                                },
                                {
                                    "name": (
                                        "発表資料の言語 / Language of presentation "
                                        "material"
                                    ),
                                    "categoryItems": [{"name": "Both"}],
                                },
                                {
                                    "name": "Audience expertise",
                                    "categoryItems": [],
                                },
                            ],
                            "roomId": 14495,
                            "room": "#pyconjp",
                        },
                        {
                            "questionAnswers": [
                                {
                                    "question": "Elevator Pitch",
                                    "answer": "エレベーターピッチです",
                                },
                                {
                                    "question": (
                                        "聴衆に求める前提知識 / Prerequisite knowledge "
                                        "for attending"
                                    ),
                                    "answer": "前提知識です",
                                },
                                {
                                    "question": "聴衆が持ち帰ることができるもの",
                                    "answer": "持ち帰ります",
                                },
                            ],
                            "id": "214734",
                            "title": "テストデータプロポーザル",
                            "description": "テストデータに使うための\r\nダミープロポーザルです",
                            "startsAt": "2020-08-29T14:50:00",
                            "endsAt": "2020-08-29T15:20:00",
                            "speakers": [
                                {"id": "masked_id_aaa", "name": "てすとでい太"}
                            ],
                            "categories": [
                                {
                                    "name": "Session format",
                                    "categoryItems": [{"name": "Talk(30min)"}],
                                },
                                {
                                    "name": "Track",
                                    "categoryItems": [{"name": "Python core"}],
                                },
                                {
                                    "name": "Level",
                                    "categoryItems": [{"name": "Beginner"}],
                                },
                                {
                                    "name": "Language",
                                    "categoryItems": [{"name": "Japanese"}],
                                },
                                {
                                    "name": (
                                        "発表資料の言語 / Language of presentation "
                                        "material"
                                    ),
                                    "categoryItems": [
                                        {"name": "Japanese only"}
                                    ],
                                },
                                {
                                    "name": "Audience expertise",
                                    "categoryItems": [{"name": "100%"}],
                                },
                            ],
                            "roomId": 14496,
                            "room": "#pyconjp_2",
                        },
                    ]
                },
            ],
            [
                {
                    "id": "masked_id_aaa",
                    "fullName": "てすとでい太",
                    "bio": "てすとでい太はテストデータに頻繁に登壇しています。",
                }
            ],
        ]

        generator = sut.fetch_talks_as_dict(sessions_uri, speakers_uri)
        actual = list(generator)

        self.assertEqual(
            actual,
            [
                {
                    "id": "213320",
                    "title": "招待講演テストデータ",
                    "room": "#pyconjp_1",
                    "day": 1,
                    "no": 2,
                    "elevator_pitch": "招待講演のエレベーターピッチ",
                    "prerequisite_knowledge": None,
                    "audience_takeaway": None,
                    "talk_format": "Invited talk(45min)",
                    "audience_python_level": None,
                    "audience_expertise": None,
                    "track": "Data Science / Machine Learning",
                    "lang_of_talk": "Japanese",
                    "lang_of_slide": "Japanese only",
                    "description": "〇〇氏による招待講演です\r\nhttp://example.com/blog",
                    "name": "打田智子",
                    "profile": "〇〇氏のプロフィール。\r\nプロフィールが続きます",
                },
                {
                    "id": "214735",
                    "title": "スタッフ作成コンテンツ",
                    "room": "#pyconjp",
                    "day": 2,
                    "no": None,
                    "elevator_pitch": None,
                    "prerequisite_knowledge": None,
                    "audience_takeaway": None,
                    "talk_format": None,
                    "audience_python_level": None,
                    "audience_expertise": None,
                    "track": None,
                    "lang_of_talk": "Japanese",
                    "lang_of_slide": "Both",
                    "description": "スタッフが作成した\r\nキーノート・招待講演以外のコンテンツです",
                },
                {
                    "id": "214734",
                    "title": "テストデータプロポーザル",
                    "room": "#pyconjp_2",
                    "day": 2,
                    "no": 3,
                    "elevator_pitch": "エレベーターピッチです",
                    "prerequisite_knowledge": "前提知識です",
                    "audience_takeaway": "持ち帰ります",
                    "talk_format": "Talk(30min)",
                    "audience_python_level": "Beginner",
                    "audience_expertise": "100%",
                    "track": "Python core",
                    "lang_of_talk": "Japanese",
                    "lang_of_slide": "Japanese only",
                    "description": "テストデータに使うための\r\nダミープロポーザルです",
                    "name": "てすとでい太",
                    "profile": "てすとでい太はテストデータに頻繁に登壇しています。",
                },
            ],
        )
