# Getting To Know You Bingo

A mandatory fun time activity for introducing yourself to people at an event for the purpose of making new friends.

This creates a printable set of bingo cards to hand out at an unconference, meet-up, event, or similar gathering of socially awkward people who need to gamify their interactions with other attendees.

This was built for [BarCamp London XIII](https://thirteen.barcamplondon.org/) and was well tolerated by over 16% of attendees.

## Instructions

* Create a list of questions, one per line, in `questions.txt`
* Install [WeasyPrint](https://pypi.org/project/weasyprint/) using `pip install weasyprint`
* Run `python bingo.py`
* Print the new PDF onto paper and hand out to attendees.

## Caveats

* Please look through the list of questions and remove any which aren't suitable for your event.
   * Add more questions to taste.
* Some attendees will complain that their sheets contain impossible conditions.
   * Encourage them to be creative.
* GDPR violations may occur if all the data is correlated.
   * Please perform a thorough DPIA before proceeding.
* Paper is set to A4 size.
   * If your country has not standardised on ISO 216, please move.

## Support

[![No Maintenance Intended](https://unmaintained.tech/badge.svg)](https://unmaintained.tech/)