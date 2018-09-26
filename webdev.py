

developers_db = [
  {"name": "Batman", "id": "6fc379de-59ba-4dfa-acd7-6f07595bf4d9"},
  {"name": "Robin",  "id": "8916ee4f-72bc-407a-b6ce-abd2d28f7429"},
  {"name": "Eggman", "id": "6423a567-fd64-4f4d-8923-39facda87597"},
  {"name": "Walrus", "id": "4fa52aa9-6374-4349-9091-9814d4c85be0"}
]


def get_developer(limit=100):
    return developers_db[0:limit]


def put_developer(body):
    global developers_db
    for dev in developers_db:
        if dev["id"] == body["id"]:
            dev.update(body)
            break
    else:
        developers_db += [body]
    return body
