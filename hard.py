"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json
from condition import *
from venv import create

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    if target_course == "COMP1511":
        return True
    #might use a tree for calculating things, go thru recursive search since it is useful to do that
    #for the AND / OR
    course_completed = create_hashmap(courses_list)
    tree = create_tree(CONDITIONS[target_course])
    return recursive_search(tree, course_completed)

def create_hashmap(courses_list):
    dic = {}
    for i, course in enumerate(courses_list):
        dic[course] = i
    return dic

#goes through each condition of "the tree", and recursively go through them
#note, recurse when there is a new () since it is a new group
def recursive_search(conditions_tree, courses_completed):
    #conditions passed through
    pass
    
    #seperate by word Or/And
    
def create_tree(conditions: str):
    #will be a tree such as COMP1511 OR COMP2521 OR ETC...
    
    #first put to lower case
    conditions = conditions.lower()
    
    #EXAMPLE WILL BE LIKE: comp1511 or comp2521 or etc....
    conditionList = conditions.split()
    #EXAMPLE: comp1511,or,comp2521,or,comp31
    #now must check if is an AND or an OR
    openBrackets = 0
    closedBrackets = 0
    #first step, find the first word ie and/or and it will tell you if it is AND or OR condition in first nest
    if first_word == "or":
        head = ORcondition
    else:
        head = ANDcondition
    #then rope all the words that are not in brackets and put them in the or condition
    #NOTE count the amount of open and unopened brackets to determine when the brackets stop and start
    #then delete all the words, bar the ones that existed while /(/ != /)/
    
    #then delete the first openBracket and the last closedBracket
    
    #repeat the steps using a recursion 
    
    #return the head of the condition tree
    return head
    #NOTE: THINK ABOUT CASE IF THERE ARE 2 () () IN THE BEGINNING CONDITIONS STATEMENT
    
#TODO: create a condition tree based on what has been inputted and then use that in recursive search

    