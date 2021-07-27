import re
import string

text = """
ACHTUNG!Warnsignal
Es geht eine neue SMS Spam Welle um. Der Text geht in dieser Richtung.
'1 Neue Spnachnachricht(en) empfadgen: [bösartiger Link]'Ñ¦
#Spam
@TheMorpheusTuts Hallo Welt
https://twitter.com/TheMorpheusTuts/status/1416103913355366400 Hallo Welt
Zu erkennen         am schlechten Deutsch, aber sowas sollte generell nicht per SMS kommen, ohne, dass ihr wisst von wem.
"""


def clean(text, *, allow_none=False, duplicate_whitespace=False, remove_linebreaks_with='\n', to_ascii=True, allow_mentions=True, allow_urls=True, allow_digits=True, allow_punctuation=True):
    if text is None:
        if allow_none:
            return None
        return ''

    text = str(text)

    if not allow_mentions:
        text = re.sub("@\S+", "", text)
    if not allow_urls:
        text = re.sub("https?:\/\/\S*", "", text)
    if not allow_digits:
        text = re.sub("\d+", "", text)
    if not allow_punctuation:
        for c in string.punctuation:
            text = text.replace(c, "")

    text = re.sub('\n', remove_linebreaks_with, text)

    if not duplicate_whitespace:
        text = re.sub(' +', ' ', text).strip()

    if to_ascii:
        text = text.encode('ascii', 'ignore').decode()

    return text


print(clean(text, allow_digits=False, allow_punctuation=False, duplicate_whitespace=False, remove_linebreaks_with='\n', allow_mentions=False, allow_urls=False))
