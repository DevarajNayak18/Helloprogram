'''

import copy
old_list=[1,2,3,4]
old_list[1]="hi"
old_list[0]="hello"
new_list=copy.deepcopy(old_list)
print(old_list, id(old_list))
print(new_list,id(new_list))



import copy
old_list=[[10,20,30,40],[11,22,33]]
new_list=copy.deepcopy(old_list)
new_list[1][1]='dev'
print(old_list,id(old_list))
print(new_list,id(new_list))


#PrintBoard
TheBorad={"Top_L":"","Top_M":"","Top_R":"","Mid_L":"","Mid_M":"","Mid_R":"","Low_L":"","Low_M":"","Low_R":""}
import pprint
TheBorad["Top_L"]='x'
TheBorad["Top_M"]='I'
TheBorad["Top_R"]='x'
TheBorad["Mid_L"]='0'
TheBorad["Mid_R"]='x'
TheBorad["Low_M"]='U'
TheBorad["Mid_M"]='L'
TheBorad["Low_L"]='Y'
TheBorad["Low_R"]='Z'
#pprint.pprint(TheBorad)
def printboard(board):
    print(board['Top_L'] + '|'+board['Top_M'] + '|' +board['Top_R'])
    print("-----")
    print(board['Mid_L'] + '|'+board['Mid_M'] + '|' +board['Mid_R'])
    print("-----")
    print(board['Low_L'] + '|'+board['Low_M'] + '|' +board['Low_R'])
printboard(TheBorad)

output= \
x|I|x
-----
0|L|x
-----
Y|U|Z
'''







