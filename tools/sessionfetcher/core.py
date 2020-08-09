from sessionfetcher import data, http


def fetch_talks_as_dict(sessions_uri, speakers_uri):
    sessions_response = http.fetch_response(sessions_uri)
    speakers_response = http.fetch_response(speakers_uri)
    speakers_map = create_speakers_map(speakers_response)
    talks = create_talks(sessions_response)
    for talk in talks:
        yield talk_dict_joined_speaker(talk, speakers_map)


def create_speakers_map(response):
    speakers_map = {}
    for speaker_data in response:
        speaker = data.Speaker.create(speaker_data)
        speakers_map[speaker_data["id"]] = speaker
    return speakers_map


def create_talks(response):
    # APIは日ごとにトークのリストを分けるように設定した
    for day, res in enumerate(response, start=1):
        for session in res["sessions"]:
            if session["speakers"][0]["name"] == "PyCon JP":
                # sessionize用にPyCon JPスタッフが登録したデータは集計しない
                continue
            yield data.Talk.create(session, day)


def talk_dict_joined_speaker(talk, speakers_map):
    talk_dict = talk.as_dict()
    speaker_ids = talk_dict.pop("speaker_ids")
    if len(speaker_ids) == 1:
        speaker = speakers_map[speaker_ids[0]]
        talk_dict.update(speaker.as_dict())
        return talk_dict
    # 共同発表の場合
    names, profiles = [], []
    for speaker_id in speaker_ids:
        speaker = speakers_map[speaker_id]
        names.append(speaker.name)
        profiles.append(f"{speaker.name}：\n{speaker.profile}")
    talk_dict["name"] = ", ".join(names)
    talk_dict["profile"] = "\n\n".join(profiles)
    return talk_dict
