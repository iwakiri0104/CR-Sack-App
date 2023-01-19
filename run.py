import os
import logging
from slack_bolt import App
from slack_bolt import Say
from slack_bolt.adapter.socket_mode import SocketModeHandler
import deepl

SLACK_BOT_TOKEN = "xoxb-4051031086081-4051041571265-qH8YDWZOetmdkG1iBIUIOH1a"
SLACK_APP_TOKEN = "xapp-1-A041H0YHNFK-4077265939473-c1b5f6da64228277f3bfd57e124407adf5913a7a8a662968e374f77cc266ae6e"
DEEPL_API_TOKEN = "d857ebc3-1537-41ac-968f-e280bcb43793"

app = App(token=SLACK_BOT_TOKEN)

translator = deepl.Translator(DEEPL_API_TOKEN)

logging.basicConfig(level=logging.DEBUG)

languages = {
    "jp": "JA",  # Japanese
    "us": "EN-US",  # American
    "gb": "EN-GB",  # British
    "cn": "ZH",  # Chinese
    "de": "DE",  # German
    "fr": "FR",  # French
    "es": "ES",  # Spanish
    "it": "IT",  # Italian
    "flag-pt": "PT-PT",  # Portuguese not Brazilian
    "flag-br": "PT-BR",  # Portuguese Brazilian
    "ru": "RU",  # Russian
    "flag-nl": "NL",  # Dutch
}


@app.middleware
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@app.event("reaction_added")
def show_datepicker(event, say: Say):
    replies = say.client.conversations_replies(channel=event["item"]["channel"], ts=event["item"]["ts"])
    print(f"replies={replies}")
    message = replies["messages"][0]["text"]
    print(f"message={message}")
    reaction = event["reaction"]
    print(f"reaction={reaction}")

    counts = [x["count"] for x in replies["messages"][0]["reactions"] if x["name"] == reaction]
    print(f"counts={counts}")
    if counts and counts[0] > 1:
        return

    target_lang = languages.get(reaction)
    if not target_lang:
        return
    result = translator.translate_text(message, target_lang=target_lang)
    print(result)
    query = ""
    for m in message.split("\n"):
        query += f">{m}\n"
    say(text=f"{query}{result.text}", thread_ts=replies["messages"][0].get("thread_ts"))


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
