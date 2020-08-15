from dataclasses import dataclass, asdict
from typing import List

from sessionfetcher import parser


@dataclass(frozen=True)
class AnswerItems:
    elevator_pitch: str
    prerequisite_knowledge: str
    audience_takeaway: str

    @classmethod
    def create(cls, data_dict):
        elevator_pitch = data_dict["Elevator Pitch"]
        prerequisite_knowledge = data_dict[
            "聴衆に求める前提知識 / Prerequisite knowledge for attending"
        ]
        audience_takeaway = data_dict["聴衆が持ち帰ることができるもの"]
        return cls(elevator_pitch, prerequisite_knowledge, audience_takeaway)

    def as_dict(self):
        return asdict(self)


@dataclass(frozen=True)
class CategoryItems:
    talk_format: str
    audience_python_level: str
    audience_expertise: str
    track: str
    lang_of_talk: str
    lang_of_slide: str

    @classmethod
    def create(cls, data_dict):
        talk_format = data_dict["Session format"]
        audience_python_level = data_dict["Level"]
        audience_expertise = data_dict["Audience expertise"]
        track = data_dict["Track"]
        lang_of_talk = data_dict["Language"]
        lang_of_slide = data_dict[
            "発表資料の言語 / Language of presentation material"
        ]
        return cls(
            talk_format,
            audience_python_level,
            audience_expertise,
            track,
            lang_of_talk,
            lang_of_slide,
        )

    def as_dict(self):
        return asdict(self)


def talk_number(start_at: str) -> int:
    """招待講演・公募トークに、開始時間に対応する番号をつけるヘルパー関数"""
    talk_number_map = {
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
    return talk_number_map.get(start_at)


@dataclass(frozen=True)
class Talk:
    id: str
    title: str
    room: str
    day: int
    no: int
    description: str
    # TODO: YouTubeのURLを後で付ける（roomと対応すると思われる）
    # TODO: presentationのURLを後で付ける
    answer_items: AnswerItems
    category_items: CategoryItems
    speaker_ids: List[str]

    @classmethod
    def create(cls, data_dict, day):
        _id = data_dict["id"]
        title = data_dict["title"]
        room = data_dict["room"]
        no = talk_number(data_dict["startsAt"])
        description = data_dict["description"]
        question_answers_dict = parser.parse_question_answers(
            data_dict["questionAnswers"]
        )
        answer_items = AnswerItems.create(question_answers_dict)
        categories_dict = parser.parse_categories(data_dict["categories"])
        category_items = CategoryItems.create(categories_dict)
        speaker_ids = [speaker["id"] for speaker in data_dict["speakers"]]
        return cls(
            _id,
            title,
            room,
            day,
            no,
            description,
            answer_items,
            category_items,
            speaker_ids,
        )

    def as_dict(self):
        dict_formatted = {
            "id": self.id,
            "title": self.title,
            "room": self.room,
            "day": self.day,
            "no": self.no,
        }
        dict_formatted.update(self.answer_items.as_dict())
        dict_formatted.update(self.category_items.as_dict())
        dict_formatted["speaker_ids"] = self.speaker_ids
        dict_formatted["description"] = self.description
        return dict_formatted


@dataclass(frozen=True)
class Speaker:
    name: str
    profile: str

    @classmethod
    def create(cls, data_dict):
        return cls(data_dict["fullName"], data_dict["bio"])

    def as_dict(self):
        return asdict(self)
