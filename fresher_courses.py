import numpy as np
import pandas as pd
import re
import string

# created Python modules
import ocr
import helper


def get_designfresher_courses(roll_number):
    data_map=ocr.get_fresher_DF(roll_number)

    # Correct for div 3
    courses=[
        {
            'course':'Engineering Drawing',
            'code':'CE101',
            'slot':'A',
            'venue':'5G1',
            'instructor': 'CE101',
            'ltpc':' ',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'Mathematics - I',
            'code':'MA101',
            'slot':'B',
            'venue':'5G1',
            'instructor': 'MA101',
            'midsem':' ',
            'endsem':' '
        },
    ]
    if data_map['Division']=='III' or data_map['Division']=='IV':
        for c in courses:
            c['slot']=c['slot']+'1'
    if data_map['Division']=='II' or data_map['Division']=='IV':
        for c in courses:
            c['venue']='5G2'
    tutorial=[
        {
            'course':'MA 101 Tutorial',
            'code':'MA101',
            'slot':'b',
            'venue':data_map['Location'],
            'instructor':'',
            'ltpc':' ',
            'midsem':' ',
            'endsem':' '
        },
    ]
    lab=[
        {
            'course':'Engineering Drawing Lab',
            'code':'CE110',
            'slot':'AL' if data_map['Division'] in ['III','IV'] else 'ML',
            'instructor':'CE110',
            'venue':'Engineering Drawing (Practical): 1203 and 1204, Academic Complex (AC)',
            'ltpc':' ',
            'midsem':' ',
            'endsem':' '
        },
    ]

    for i in range(len(courses)):
        courses[i]['midsem'] = helper.get_midsem_time(courses[i]['slot'])
        courses[i]['endsem'] = helper.get_endsem_time(courses[i]['slot'])   
 
    return {
        'roll_number':roll_number,
        'courses':courses+tutorial+lab
    }

def get_fresher_courses(roll_number):
    data_map=ocr.get_fresher_DF(roll_number)
    print("apple")
    # Correct for div 3
    courses=[
        {
            'course':'Engineering Drawing',
            'code':'CE101',
            'slot':'A',
            'venue':'5G1',
            'instructor': 'CE101',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'Mathematics - I',
            'code':'MA101',
            'slot':'B',
            'venue':'5G1',
            'instructor': 'MA101',
            'ltpc':' ',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'Basic Electronics',
            'code':'EE101',
            'slot':'C',
            'venue':'5G1',
            'instructor': 'EE101',
            'ltpc':' ',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'Chemistry',
            'code':'CH101',
            'slot':'D',
            'venue':'5G1',
            'instructor': 'CH101',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'Physics - I',
            'code':'PH101',
            'slot':'E',
            'venue':'5G1',
            'instructor': 'PH101',
            'midsem':' ',
            'endsem':' '
        }
    ]
    if data_map['Division']=='I' or data_map['Division']=='II':
        for c in courses:
            c['slot']=c['slot']+'1'
    if data_map['Division']=='II' or data_map['Division']=='IV':
        for c in courses:
            c['venue']='5G2'
    tutorial=[
        {
            'course':'MA 101 Tutorial',
            'code':'MA101',
            'slot':'b',
            'venue':data_map['Location'],
            'instructor': '',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'EE 101 Tutorial',
            'code':'EE101',
            'slot':'c',
            'instructor': '',
            'venue':data_map['Location'],
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'CH 101 Tutorial',
            'code':'CH101',
            'instructor': '',
            'slot':'d',
            'venue':data_map['Location'],
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'PH 101 Tutorial',
            'code':'PH101',
            'slot':'e',
            'venue': '',
            'instructor':data_map['Location'],
            'midsem':' ',
            'endsem':' '
        },
    ]
    lab=[
        {
            'course':'Chemistry Laboratory',
            'code':'CH110',
            'slot':'ML' if data_map['Division'] in ['II','I'] else 'AL',
            'instructor': 'CH110',
            'venue':'Chemistry Laboratory: Department of Chemistry, Academic Complex (AC) ',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'Physics Laboratory' if data_map['Division'] in ['II','I'] else 'Workshop I',
            'code':'PH110' if data_map['Division'] in ['II','I'] else 'ME110',
            'slot':'AL' if data_map['Division'] in ['III','IV'] else 'ML',
            'instructor': 'PH110' if data_map['Division'] in ['II','I'] else 'ME110',
            'venue':'Department of Physics, Academic Complex (AC)' if data_map['Division'] in ['II','I'] else 'Workshop (on the western side of Academic Complex (AC))',
            'midsem':' ',
            'endsem':' '
        },
        {
            'course':'Engineering Drawing Lab',
            'code':'CE110',
            'slot':'AL' if data_map['Division'] in ['III','IV'] else 'ML',
            'instructor': 'CE110',
            'venue':'Engineering Drawing (Practical): 1203 and 1204, Academic Complex (AC)',
            'midsem':' ',
            'endsem':' '
        },
    ]
    if data_map['Lab']=='L6' or data_map['Lab']=='L1':
        lab[0]['slot']=lab[0]['slot']+'1'
        lab[1]['slot']=lab[1]['slot']+'4'
        lab[2]['slot']=lab[2]['slot']+'2'
    elif data_map['Lab']=='L7' or data_map['Lab']=='L2':
        lab[0]['slot']=lab[0]['slot']+'3'
        lab[1]['slot']=lab[1]['slot']+'1'
        lab[2]['slot']=lab[2]['slot']+'4'
    elif data_map['Lab']=='L8' or data_map['Lab']=='L3':
        lab[0]['slot']=lab[0]['slot']+'5'
        lab[1]['slot']=lab[1]['slot']+'3'
        lab[2]['slot']=lab[2]['slot']+'1'
    elif data_map['Lab']=='L9' or data_map['Lab']=='L4':
        lab[0]['slot']=lab[0]['slot']+'2'
        lab[1]['slot']=lab[1]['slot']+'5'
        lab[2]['slot']=lab[2]['slot']+'3'
    elif data_map['Lab']=='L10' or data_map['Lab']=='L5':
        lab[0]['slot']=lab[0]['slot']+'4'
        lab[1]['slot']=lab[1]['slot']+'2'
        lab[2]['slot']=lab[2]['slot']+'5'
    
    for i in range(len(courses)):
        courses[i]['midsem'] = helper.get_midsem_time(courses[i]['slot'])
        courses[i]['endsem'] = helper.get_endsem_time(courses[i]['slot'])

    return {
        'roll_number':roll_number,
        'courses':courses+tutorial+lab
    }