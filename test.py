""""
TEST for Turing Machine
"""
#
# from TM-Accept_Bal_Parens  import TuringMachine
from g import apple

from TMProject import TuringMachine





testCases = {'0011':"Acceept",'1100':"Acceept",'101':"Acceept",'':"Acceept",'001':"Reject",'1':"Reject",'001111':"Reject"}


for case in testCases:
    print("test case" + "  " +  case)
    print("expected " + testCases[case])
    m = TuringMachine(case,[6])
    m.execute()
    print()