import re
import pandas as pd
import datetime
from time import mktime

# Safely replace characters from a field
def removeChar(charField, characterToRemove):
    if charField is "":
        return_text = charField
    else:
        return_text = charField.replace(characterToRemove, '')
    return return_text

#  converts epoch date to datetime
def converttime(epoch_date):
    if epoch_date is "":
        return_date = epoch_date
    else:
        return_date = time.strftime("%Y-%m-%d")
    return return_date

# removes html markup
def cleanhtml(raw_html):
    try:
        raw_html = raw_html.replace('\\n','')
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
    except:
        cleantext = ''
    return cleantext

# scrubs markup from a field and returns to a new colulmn
def scrub_markup(dataframe, new_field, html_field):
    dataframe[new_field] = dataframe[html_field].apply(lambda x: cleanhtml(x))
    return
    # example:  scrub_markup(df, 'DISCUSSION_TOPIC_CLEAN', 'DISCUSSION_TOPIC_MESSAGE')

# counts the number of words in a string
def word_count(text):
    try:
        for char in '-.,\n':
            text=text.replace(char,' ')
        text = text.lower()
        word_list = text.split()
        if len(word_list) > 0:
            x = str(len(word_list))
        else:
            x = None
    except:
        x = None
    return x

# counts # of words in a df and returns to a new column "Field"
def count_words(dataframe, new_field, countwordfield):
    dataframe[new_field] = dataframe[countwordfield].apply(lambda x: word_count(x))
    return
    # example:  count_words(df, 'RESPONSE_MESSAGE_WORD_COUNT', 'DISCUSSION_RESPONSE_MESSAGE')


# Other Time Conversions
todays_date = datetime.date.today()
yesterdays_date = (todays_date - datetime.timedelta(1))
unix_yesterdays_date = str(int(mktime(yesterdays_date.timetuple())))
