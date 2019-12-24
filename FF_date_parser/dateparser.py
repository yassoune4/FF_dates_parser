"""
##################################################
## Author: Ysalihi (TensorFlow)
## Copyright: Copyright 2019, Fifty_Five_Test
## Version Python: 3.7
## Email: yassinesalihi4@gmail.com
##################################################

#Problem Description:
====================
        -We want a Python program to parse any input text
        and extract every date it contains and count the dates.
        A date has to be precise, including a day, a month and a year.

#Usage:
======
    python dateparser.py

    You can change the String content (string_test) inside the code.
"""

import re 
from datetime import datetime

# implement the regex and format date of (yyyy-MM-dd|MM-dd-yyyy|MM-dd-yy|d-MMM-yyyy)
minus_format = ('%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y', '%d-%b-%Y')
minus_regex = '[\d]{4}-[\d]{1,2}-[\d]{1,2}|[\d]{1,2}-[\d]{1,2}-[\d]{2,4}|[\d]{1,2}-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|' \
                'Aug|Sep|Oct|Nov|Dec)-[\d]{4}'
# implement the regex and format date of (MM/dd/yy|MM/dd/yyyy|d/MMM/yyyy|dd/MMM/yy)
slash_format = ('%m/%d/%y', '%m/%d/%Y', '%d/%b/%Y', '%d/%b/%y')
slash_regex = '[\d]{1,2}/[\d]{1,2}/[\d]{2,4}|[\d]{1,2}/(?:Jan|Feb|Mar|Apr|May|' \
                'Jun|Jul|Aug|Sep|Oct|Nov|Dec)/[\d]{2,4}'
# implement the regex and format date of (MMM.dd.yyyy | yyyyMMdd)
point_format = ('%b.%d.%Y',)
point_regex = '(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).[\d]{1,2}.[\d]{4}'
# implement the regex and format date of (MMMM d, yyyy|MMM d, yyyy|dd MMMM yyyy|dd MMM yyyy)
comma_space_format = ('%B %d, %Y', '%b %d, %Y', '%d %B %Y', '%d %b %Y')
comma_space_regex = '[ADFJMNOS]\w* [\d]{1,2}, [\d]{4}|[\d]{1,2} [ADFJMNOS]\w* [\d]{4}'
# concatenate all date formats
dates_formats = minus_format + slash_format + point_format + comma_space_format
# concatenate all regex formats using the logical OR
dates_regex = minus_regex + '|' + slash_regex + '|' + point_regex + '|' + comma_space_regex
# the string for test
string_test = 'Marvin Lee Minsky at the Mathematics Genealogy Project; 20 May 2014\nMarvin Lee Minsky at the AI ' \
              'Genealogy Project. {reprint 18 September 2011)\n"Personal page for Marvin Minsky". web.media.mit.edu. ' \
              'Retrieved 23 June 2016.\nAdmin (January 27, 2016). "Official Alcor Statement Concerning Marvin Minsky".' \
              '\nAlcor Life Extension Foundation. Retrieved 2016-04-07.\n"IEEE Computer Society Magazine Honors ' \
              'Artificial Intelligence Leaders".\nDigitalJournal.com. August 24, 2011. Retrieved September 18,' \
              ' 2011.\nPress release source: PRWeb (Vocus).\n"Dan David prize 2014 winners". May 15, 2014.' \
              ' Retrieved May 20, 2014.'


def parsing_date(text):
    """ Function that takes a string(text) and checks that it writes
        in a valid format and return a date object.
        Whene this function find an invalid format of date
        so nothing happens (pass).
    """
    for fmt in dates_formats:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass


def count_frequency(my_list):
    """  this function takes a list of date objects and
        groups them into a dictionary.

    for exemple :
    input :
        my_list =
                [datetime.datetime(2014, 5, 20, 0, 0),
                datetime.datetime(2011, 9, 18, 0, 0),
                datetime.datetime(2016, 6, 23, 0, 0)]
    after sorting the list :
        my_list =
                [datetime.datetime(2011, 9, 18, 0, 0),
                datetime.datetime(2014, 5, 20, 0, 0),
                datetime.datetime(2016, 6, 23, 0, 0)]
    output :
        frep =
            {2011: {9: {18: 1}}, 2014: {5: {20: 1}},
            2016: {6: {23: 1}}}

        -The frep dictionary contains years as keys
        and each key contains a dictionary of months
        and each month contains a dictionary of days
        and each day contains a value which means
        the occurrence of a date.
    """
    # sort the list
    my_list.sort()
    freq = {}
    for e in my_list:
        if e.year not in freq.keys():
            freq[e.year] = {}
            freq[e.year][e.month] = {}
            freq[e.year][e.month][e.day] = 1
        elif e.month not in freq[e.year].keys():
            freq[e.year][e.month] = {}
            freq[e.year][e.month][e.day] = 1
        elif e.day not in freq[e.year][e.month].keys():
            freq[e.year][e.month][e.day] = 1
        else:
            freq[e.year][e.month][e.day] += 1
    return freq


def print_dates(my_dict):
    """ This function takes a dictionary and display it in this format.
        yyyy:
                -mm
                        -dd (occurrence of date)
        exemple :
        input : {2011: {9: {18: 1}}, 2014: {5: {20: 1}}, 2016: {6: {23: 1}}}
        output : 2011:
                            -09
                                    -18 (1)
                2014:
                            -05
                                    -20 (1)
                2016:
                            -06
                                    -23 (1)
    """
    for e in my_dict.keys():
        print(e, ':')
        for f in my_dict[e].keys():
            # print the integer with 2 digits, left padding it with zeros
            print('\t-', '%02d' % f)
            for g in my_dict[e][f].keys():
                print('\t\t-', '%02d' % g, ' (', my_dict[e][f][g], ')')


if __name__ == "__main__":
    """finds all the matches in string_test based in dates_regex,
    and returns them as a list of strings."""
    list = re.findall(dates_regex, string_test)
    # list that will contain all date objects
    Dates_List = []
    for i in list:
        # append each valid date format as a date object
        Dates_List.append(parsing_date(i))
    # print all dates after counting their frequency
    print_dates(count_frequency(Dates_List))
