def solution(s):
    lst = []
    for i in range(0, len(s), 2):
        if i < len(s) - 1:
            lst.append(s[i:i+2])
        else:
            lst.append(s[-1]+"_")
    return lst

    #return [s[i:i+2] if i < len(s) - 1 else s[-1]+"_" for i in range(0,len(s),2]



    # result = []
    # if len(s) % 2:
    #     s += '_'
    # for i in range(0, len(s), 2):
    #     result.append(s[i:i+2])
    # return result


s = "heccccc"
print(solution(s))