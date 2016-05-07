__author__ = 'Hinshitsu-IT'
'''
To be, or not to be: that is the question.
Whether 'tis nobler in the mind to suffer.
The slings and arrows of outrageous fortune.
Or to take arms against a sea of troubles.
And by opposing end them, to die: to sleep.

To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR.
ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE.
Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS.
AnD bY oPpOsInG eNd ThEm, To DiE: tO sLeEp.
'''

test_cases = open('roller_coaster.txt','r')
for test in test_cases:
    string = test.strip()
    new_string = []
    for i in range(len(string)):
        if i