from unittest import TestCase
from unittest.mock import patch

import main


@patch("main.constants")
class AddStreamingUrlTestCase(TestCase):
    def setUp(self):
        self.youtube_live_url_map = {
            (1, "#pyconjp_4"): "https://youtu.be/test1",
            (1, "#pyconjp_2"): "https://youtu.be/test2",
        }
        self.not_streamed_id_set = set(["214733"])

    def test_should_add_url(self, constants):
        constants.YOUTUBE_LIVE_URL_MAP = self.youtube_live_url_map
        constants.NOT_STREAMED_ID_SET = self.not_streamed_id_set

        talk = {
            "id": "214734",
            "title": "テストデータのタイトル",
            "room": "#pyconjp_4",
            "day": 1,
            "no": 4,
            "elevator_pitch": "テストデータのエレベータピッチです",
            "prerequisite_knowledge": "テストデータへの前提知識",
            "audience_takeaway": "テストデータで持ち帰ることができるもの",
            "talk_format": "Talk(45min)",
            "audience_python_level": "Intermediate",
            "audience_expertise": "0%",
            "track": "Data Science / Machine Learning",
            "lang_of_talk": "Japanese",
            "lang_of_slide": "Japanese only",
            "description": "テストデータの詳細です",
            "name": "てすとでい太",
            "profile": "てすとでい太のプロフィールです",
        }

        main.add_streaming_url(talk)

        self.assertEqual(
            talk,
            {
                "id": "214734",
                "title": "テストデータのタイトル",
                "room": "#pyconjp_4",
                "day": 1,
                "no": 4,
                "elevator_pitch": "テストデータのエレベータピッチです",
                "prerequisite_knowledge": "テストデータへの前提知識",
                "audience_takeaway": "テストデータで持ち帰ることができるもの",
                "talk_format": "Talk(45min)",
                "audience_python_level": "Intermediate",
                "audience_expertise": "0%",
                "track": "Data Science / Machine Learning",
                "lang_of_talk": "Japanese",
                "lang_of_slide": "Japanese only",
                "description": "テストデータの詳細です",
                "name": "てすとでい太",
                "profile": "てすとでい太のプロフィールです",
                "youtube_url": "https://youtu.be/test1",
            },
        )

    def test_should_add_same_url_when_same_day_same_room(self, constants):
        constants.YOUTUBE_LIVE_URL_MAP = self.youtube_live_url_map
        constants.NOT_STREAMED_ID_SET = self.not_streamed_id_set
        # ここから下のテストメソッドでは、判定に必要な項目に絞って辞書を用意
        talk0 = {"id": "214732", "day": 1, "room": "#pyconjp_2"}
        talk1 = {"id": "214735", "day": 1, "room": "#pyconjp_2"}

        for talk in [talk0, talk1]:
            main.add_streaming_url(talk)

        self.assertEqual(talk0["youtube_url"], talk1["youtube_url"])

    def test_should_add_different_url_when_same_day_different_room(
        self, constants
    ):
        constants.YOUTUBE_LIVE_URL_MAP = self.youtube_live_url_map
        constants.NOT_STREAMED_ID_SET = self.not_streamed_id_set

        talk0 = {"id": "214732", "day": 1, "room": "#pyconjp_2"}
        talk1 = {"id": "214734", "day": 1, "room": "#pyconjp_4"}

        for talk in [talk0, talk1]:
            main.add_streaming_url(talk)

        self.assertNotEqual(talk0["youtube_url"], talk1["youtube_url"])

    def test_should_add_empty_url_to_not_streamed_contents(self, constants):
        constants.YOUTUBE_LIVE_URL_MAP = self.youtube_live_url_map
        constants.NOT_STREAMED_ID_SET = self.not_streamed_id_set

        talk = {"id": "214733", "day": 2, "room": "#pyconjp"}

        main.add_streaming_url(talk)

        self.assertEqual(
            talk,
            {"id": "214733", "day": 2, "room": "#pyconjp", "youtube_url": ""},
        )
