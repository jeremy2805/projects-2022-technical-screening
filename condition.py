class condition:
    def __init__(self) -> None:
        pass
    def conditionPassed(self, courses_completed: dict) -> bool:
        pass

class ORcondition(condition):
    def __init__(self, conditions: "list[condition]") -> None:
        super().__init__()
        self.conditions = conditions
    def addCondition(self, condition: condition):
        self.conditions.append(condition)
    def addConditions(self, conditions: "list[condition]"):
        self.conditions.extend(conditions)
    def conditionPassed(self, courses_completed: dict) -> bool:
        for condition in self.conditions:
            if condition.conditionPassed(courses_completed):
                return True
        return False

class ANDcondition(condition):
    def __init__(self, conditions: "list[condition]") -> None:
        super().__init__()
        self.conditions = conditions
    #slight repetition here....
    #would be bad if we were to introduce more conditions like XOR etc.. but unlikely?
    def addCondition(self, condition: condition):
        self.conditions.append(condition)
    def addConditions(self, conditions: "list[condition]"):
        self.conditions.extend(conditions)
    def conditionPassed(self, courses_completed: dict) -> bool:
        for condition in self.conditions:
            if not condition.conditionPassed(courses_completed):
                return False
        return True
#condition that the specific course has been taken and it is given by its course Code
#note if the prereqs are just numbers example: 5312, just add COMP infront and maake this condition

#make sure courseName is a string
class SPECIFICcondition(condition):
    def __init__(self, courseName: str) -> None:
        super().__init__()
        self.name = courseName
    def conditionPassed(self, courses_completed: dict) -> bool:
        if courses_completed.get(self.name) is not None:
            return True
        else:
            return False

#if a certain number of courses need to be taken for example 12 units first year courses...
class NUMEROUScondition(condition):
    pass