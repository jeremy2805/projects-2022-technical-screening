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
import re

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
    #note start the tree off with an AND condition that will be the head and it will only be the one condition
    #that is the beginning of the AND/OR tree
    #WILL LOOK LIKE THIS 
    #
    #         AND
    #          |
    # EXAMPLE (OR) 
    #         /  \
    #        152  251
    course_completed = create_hashmap(courses_list)
    tree = ANDcondition([create_tree(CONDITIONS[target_course])])
    return tree.conditionPassed(course_completed)
#will be all lowercase
def create_hashmap(courses_list):
    dic = {}
    for i, course in enumerate(courses_list):
        dic[course.lower()] = i
    return dic

def create_tree(conditions: str) -> condition:
    #will be a tree such as COMP1511 OR COMP2521 OR ETC...
    
    #first put to lower case
    conditions = conditions.lower()
    
    #EXAMPLE WILL BE LIKE: comp1511 or comp2521 or etc....
    conditionList = conditions.split()
    #EXAMPLE: comp1511,or,comp2521,or,comp31
    #now must check if is an AND or an OR
    bracketDiff = 0
    #first step, find the first word ie and/or and it will tell you if it is AND or OR condition in first nest
    conditions_created = []
    i = 0
    while i < len(conditionList):
        #means it is the start of a recursive statement
        #could use regex instead to just grab the string (PROB BETTER BET)
        #but how to handle if bracket in bracket?
        if "(" in conditionList[i]:
            #since we know that a bracket will have at least one condition ie. () will never happen 
            #I mean I cant say for certain so just in case
            bracketDiff = bracketDiff + conditionList[i].count("(") - conditionList[i].count(")")
            #now we begin searching from in here
            j = i + 1
            while bracketDiff != 0:
                #while we are still searching
                bracketDiff = bracketDiff + conditionList[j].count("(") - conditionList[j].count(")")
                j += 1
                #NOTE: since we know this is valid input there must be an eqal amount of "(" and ")"
                #so it will eventually end
            #now that we have taken the brackets
            #take brackets off the end of the string and keep going
            #excluding j since j has moved on since bracketDiff has become 0
            newCondList = conditionList[i:j]
            #remove from the string that isnt condition list since it is what matters
            recursiveConds = ' '.join(newCondList)
            conditions = conditions.replace(recursiveConds, '')
            #remove from conditions string
            #remove the brackets now
            recursiveConds = recursiveConds[1:]
            recursiveConds = recursiveConds[:-1]
            #now do same tree structure
            conditions_created.append(create_tree(recursiveConds))
            i = j
        else:
            i += 1
            
    #we now know that there are no substrings containing '(' or ')'
    #thus must be final condition
    #add the list of conditions created so far to this
    conditionList = conditions.split()
    #add to list of conditions created
    for word in conditionList:
        #check each word to see if it is AND / OR
        if word == "or":
            head = ORcondition([])
            break
        elif word == "and":
            head = ANDcondition([])
            break
    #now that we have created the head we can go in and make a new condition and add to head
    head.addConditions(conditions_created)
    #added the conditions that have been made so far (ones made thru recursion)
    #now add all the ones from the word list
    #TODO: check for condition which is x amount of units done
    for word in conditionList:
        #is a comp condition
        #not good at regex....
        #wildcard at end because sometimes there is a .
        val = re.compile(r'[a-z]?[a-z]?[a-z]?[a-z]?[\d][\d][\d][\d]*').match(word)
        if val is not None:
            val = val.group()
            print(val)
            #no need to format since it has prefix infront of it
            if  len(val) > 4:
                head.addCondition(SPECIFICcondition(val))
            else:
                #need to add comp to front
                head.addCondition(SPECIFICcondition("comp" + val))
        #TODO add the other requirement of NUMEROUScondition later
            
    return head

    