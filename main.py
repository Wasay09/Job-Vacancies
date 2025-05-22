
"""
    Cis2250DemoQ3.py
    Author(s):
    Oliver Simm
    Shayan Safaei, Oliver Simm, Bassem Sourour, Wasayuddin Syed




How to run syntax: | python3 "main.py" preprocessed_q1.csv preprocessed_q2.csv preprocessed_q3.csv


"""

#imports
import sys
import csv
import src.Q1_graph as cdq1
import src.Cis2250DemoQ2 as cdq2
import src.Q3Plot as cdq3


def main(argv):
    while True:
        choice = input("Enter a choice (1.Run Q1\t2.Run Q2\t3.Run Q3\t-1: Exit): ")
        if choice in ['1', '2', '3','-1']:
            if choice == '1':
                print("You chose Run Q1")
                cdq1.q1(argv)
            elif choice == '2':
                print("You chose Run Q2")
                q2Parameter = input("Enter Your Parameter (Canada/Province): ")
                cdq2.runQ2(argv, q2Parameter)
            elif choice == '3':
                print("You chose Run Q3")
                cdq3.q3(argv)
            else:
                print("Goodbye!!")
                sys.exit(0)
        else:
            print("Invalid input. Please enter 1, 2, 3 or -1")








main(sys.argv)