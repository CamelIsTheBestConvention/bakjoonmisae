def solution(participant, completion):
    participant_list = {}
    
    for parti in participant:
        if parti in participant_list:
            participant_list[parti] += 1
        else:
            participant_list[parti] = 1
            
    for comple in completion:
        if comple in participant_list:
            participant_list[comple] -= 1
            
    for parti in participant_list:
        if participant_list[parti] == 1:
            return parti
