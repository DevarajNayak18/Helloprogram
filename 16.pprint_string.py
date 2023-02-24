import pprint
message='''FULL NAME
Email ID: <name>@thundersoft.com				
CARRIER OBJECTIVE
A Dynamic personality ready to have dedication towards betterment of organization through my technical and managerial skills owned by me and through my practical exposure towards the work to be done by me.
PROFESSIONAL SUMMARY
Experience with C, C++, C#, and RTOS concepts.
Having good understanding on the Visual studio tools.
Knowledge on Perforce.
Knowledge on STLC.
Tools: QACT, JIRA, Git, Gerrit.
ACADEMIC DETAILS
B.E in Electronics and Communication Engineering in 2019 from Lovely Professional university, Jalandhar, Punjab with an aggregate of 7.04 CGPA.
Intermediate (+2) in 2015 from Narayana Junior College Nandyal, with an aggregate of 86.8%
SSC in 2013 from Good Shepherd English Medium School, Nandyal with an aggregate of 8.7 CGPA.
PROFESSIONAL SUMMARY
Software Trainee at ThunderSoft India Private Limited, Hyderabad (22 June 2019 - till date)  
AWARDS AND ACHIEVEMENTS
Participated in multiple cultural activities throughout my schooling.
Awarded winner up in Handball at Zonal level, 2011.
Awarded winner up in Handball at Central Zonal level, 2011. 
PROJECTS
PROJECT : QUALCOMM CODEC EVALUATION TOOL PLUGIN(QCET)
DESCRIPTION: Qualcomm Codec Evaluation Tool (QCET) is a software application for assessing the capabilities of the WCD audio codec chip. It is a PC based tool that connects via USB cable on audio codec chip that is hosted on a controller board and a daughter card.
Roles and Responsibilities:
Did Manual and automation testing 
Prepared Test Plan and Test Suite for the Project
Executed 360+ Manual Test Cases
Written 50+ Automation Test Cases
Did first cut analysis on the bug'''
count={}
for letter in message.lower():
    count.setdefault(letter,0)
    count[letter]=count[letter]+1
pprint.pprint(count)