def get_highest_paid(nestedDict):
    result = None
    highest_s = None
    for i in nestedDict:
        if (highest_s) == None or (highest_s)<nestedDict[i]['Salary']:
            highest_s = nestedDict[i]['Salary']
            result = i
    return result