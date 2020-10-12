import json
import codecs
import os
from datetime import datetime
from collections import Counter

def fma():
    userInput = input('Directory of only messages_.json files': ')

    searchInput = str(input('Search for word: ').lower())

    directory = userInput
    dir_list = os.listdir(directory)
    
    name1Count = 0
    name2Count = 0
    word1Count = 0
    word2Count = 0
    pic1Count = 0
    pic2Count = 0
    search1Count = 0
    search2Count = 0
    dateArray = []
    dateCount = []

    for data in dir_list:
        data = open(directory+'/'+data).read()

        name1 = data['participants'][0]['name']
        name2 = data['participants'][1]['name']

        for p in data['messages']:

                timestamp  = datetime.utcfromtimestamp(p['timestamp_ms'] / 1000).strftime('%Y-%m-%d  %H:%M:%S')
                timestamp2 = datetime.utcfromtimestamp(p['timestamp_ms'] / 1000).strftime('%Y-%m-%d')
                dateArray.append(timestamp2)

                nametime = print(p['sender_name'] + ' (' + timestamp + '):')

                # message counter
                if p['sender_name'] == name1:
                    name1Count += 1
                else:
                    name2Count += 1

                # photos message counter
                if 'photos' in p:
                    nametime
                    print('Photo message \n\n')
                    if p['sender_name'] == name1:
                        pic1Count += 1
                    else:
                        pic2Count += 1

                elif 'content' not in p:
                    nametime
                    print('Other media content \n\n')

                else:
                    nametime
                    text = p['content']
                    textLength = len(text.split(' '))
                    print(text + '\n\n')

                    # word counter
                    if p['sender_name'] == name1:
                        word1Count += textLength ## only splits spaces, not linebreaks
                        if searchInput is not False:
                            for i in range(textLength):
                                if searchInput in text.split(' ')[i].lower():
                                    print(i)
                                    search1Count += 1
                    else:
                        word2Count += textLength
                        if searchInput is not False:
                            for i in range(textLength):
                                if searchInput in text.split(' ')[i].lower():
                                    print(i)
                                    search2Count += 1

    dateCount = Counter(dateArray).most_common() # sorted date list with duplicates
    dateArrayNoDup = list(dict.fromkeys(dateArray))  # removes duplicates from date array, still sorted

    totalMessages = name1Count + name2Count
    percentage1 = round((name1Count / totalMessages)  * 100)
    percentage2 = round((name2Count / totalMessages) * 100)
    totalWordcount = word1Count + word2Count
    average1 = round((word1Count / name1Count)*2)/2
    average2 = round((word2Count / name2Count)*2)/2
    picTotal = pic1Count + pic2Count

    firstName1 = name1.split(' ')[0]
    firstName2 = name2.split(' ')[0]

    print('Conversation between ' + name1 + ' and ' + name2 + ':\n')
    print('Message stats:')
    print(firstName1 + ' has sent ' + str(name1Count) + ' (' + str(percentage1) + '%) messages. ' + str(pic1Count) + ' of those messages contains at least one image.')
    print(firstName2 + ' has sent ' + str(name2Count) + ' (' + str(percentage2) + '%) messages. ' + str(pic2Count) + ' of those messages contains at least one image.')

    print(str(totalMessages) + ' total messages sent, with ' + str(picTotal) + ' messages containing at least one image \n')

    print('Word stats:')
    print('Total amount of words for ' + firstName1 + ': ' + str(word1Count) + ' (' + str(average1) + ' words per message on average).')
    print('Total amount of words for ' + firstName2 + ': ' + str(word2Count) + ' (' + str(average2) + ' words per message on average).')
    print(firstName1 + ' has sent "' + searchInput + '" ' + str(search1Count) + ' time(s), ' + firstName2 + ' sent it ' + str(search2Count) + ' time(s)')

    print('Total word count: ' + str(totalWordcount) + '\n')

    print('Date stats:')
    print('Latest message date: ' + str(dateArray[0]) + ', first message date: ' + str(dateArray[-1]) + '. \n' + str(len(dateArrayNoDup)) + ' days between first and last message. \nThat makes ' + str(round(totalMessages / len(dateArrayNoDup))) + ' messages a day on average.')
    print(str(dateCount[0][0]) + ' has been the date with most sent messages, with ' + str(dateCount[0][1]) + ' messages sent.\n\n')
fma()
