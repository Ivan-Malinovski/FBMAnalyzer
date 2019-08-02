# FBMAnalyzer

A primitive Facebook Messenger analyzer. At this time, it only supports 1-1 conversations, and it requires you to download your Messenger archive from Facebook.com in json. The latter is probably never going to be changed, because of Facebook restrictions.

Right now it outputs the following:
* Total amount of sent words and messages per participant
* How many of those messages contain images (I'll upgrade this to total images at some point)
* How many times a certain word has been said, both in total and per participant
* Total word count
* When the first and last message has been sent
* Messages a day on average
* The date with most messages sent

The code is currently very messy, please don't look at it.

Usage (assuming you've downloaded and extracted the Messenger archive):
* Download the exe (once I've made it)
* Run it
* Type in the path to the message_1.json or just drag the json file in the window, press enter
* Type in the word you want to search for (or leave blank), and press enter

TODO:
* Fix current features that don't work properly (Message a day on average)
* Clean up redundant code
* Add stat for conversation starter (first message of the day)
* Add stat for how long it takes participants to reply
