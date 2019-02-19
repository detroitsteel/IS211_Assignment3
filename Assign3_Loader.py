#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Intakes a URL in a csv file format of web traffic data
and parses the data"""

from __future__ import division
import urllib2
import logging
import argparse
import csv
import re

 
def downloadData(url):
    """downloadData Function - intakes a csv file path and creates
    a csv file, which is then passed to the function processData().
    The function is meant to parse a csv file of web traffic data.
    Args:
        url (string): A url in csv format
    Output: A list. 
    Example:
        d = downloadData('https://s3.amazonaws.com
        /cuny-is211-spring2015/birthdays100.csv')
    """
    url = url
    new_csv_file = 'Webtraffic.csv'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    a_file = csv.reader(response)
    with open(new_csv_file, mode = 'w') as outfile:
        writer = csv.writer(outfile)
        for row in a_file:
            writer.writerow(row)
    outfile.close
    return processData(new_csv_file)


def processData(new_csv_file):
    """processData Function - intakes the name of a csv file which is parsed and
    returns specific details about the csv. 
    Args:
        new_csv_file (string): A string which is the name of a csv file
    Output: A dict 
    Example:
        d = processData('NewCsvFile.csv')
    """
    final = 0.0
    i = 0
    j = 0
    index = 0
    k = 0
    b_brw_lst = []
    b_fnl_lst = []
    a_csv_file = 'PicFilesOnly.csv'
    src_sch = ("[c][h][r][o][m][e]|[s][a][f][a][r][i]|[m][s][i][e]|"
               "[f][i][r][e][f][o][x]")
    b_file = open(a_csv_file, mode = 'w')
    with open(new_csv_file, mode = 'r') as outfile:
        b_writer = csv.writer(b_file)
        for row in outfile:
            j += 1
            b_writer.writerow(row)
            if re.search("[jJgGpP][pPiInN][gGfFgG]", row):
                i += 1
            b_re_sch = re.search(src_sch, row, re.IGNORECASE)#"[CcFfMSs][ihSsa][rIif][oEea][mfr][eoi][\w\W]", row)
            if b_re_sch:
                b_re_sch_match = b_re_sch.group()
                b_brw_lst.append(b_re_sch_match.upper())
            b_set = set(b_brw_lst)
            b_fnl_lst = [[m,b_brw_lst.count(m)] for m in b_set]
            b_top_brw = sorted(b_fnl_lst, key = lambda brw: brw[1], reverse = True)
    outfile.close
    b_file.close
    final = float((i/j)*100)
    print  ('Image requests account for %i %% of all requests.'
            'The most used browser for the given data was %s with %i uses.'
            % (final, b_top_brw[0][0], b_top_brw[0][1]))
    return 

        
def main():
    """Main Function - intakes passed command line URL arg and returns facts
    about the parsed web traffic data. The URL must provide a csv file with
    web traffic data.
    Args:
        url (string): A url in csv format
    Output: Facts about the parsed web traffic data. 
    Example:
        $ python Assign3_Loader.py
        http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv

        'Image requests account for 65 % of all requests.
        The most used browser for the given data was Chrome .'
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help = "URL you'd like to parse", type = str)
    args = parser.parse_args()
    url = args.url
    Log_Filename = 'errors.log'
    logging.basicConfig(filename = Log_Filename, level = logging.ERROR)
    logger1 = logging.getLogger('assingment2')
    try:
        personData = downloadData(url)
        #response = int(raw_input('Enter User ID to lookup. To EXIT enter 0. '))
        #while response > 0:
        #    displayPerson(response, personData)
        #    response = int(raw_input('Enter User ID to lookup. To EXIT enter 0. '))
    except Exception as e:
        logger1.error('Main Error %s' % e)
main()
