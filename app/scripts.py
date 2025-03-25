

def update_weights(state):
    
    if state['all_human_results'][-4] == 'win' and state['all_human_choice'][-4] != state['all_human_choice'][-3] and state['all_human_results'][-2] == 'win':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['win']['change']['win']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['win']['change']['win']['same'] += 1
    
    elif state['all_human_results'][-4] == 'win' and state['all_human_choice'][-4] != state['all_human_choice'][-3] and state['all_human_results'][-2] == 'lose':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['win']['change']['lose']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['win']['change']['lose']['same'] += 1
    
    elif state['all_human_results'][-4] == 'win' and state['all_human_choice'][-4] == state['all_human_choice'][-3] and state['all_human_results'][-2] == 'win':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['win']['same']['win']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['win']['same']['win']['same'] += 1
    
    elif state['all_human_results'][-4] == 'win' and state['all_human_choice'][-4] == state['all_human_choice'][-3] and state['all_human_results'][-2] == 'lose':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['win']['same']['lose']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['win']['same']['lose']['same'] += 1
            
    elif state['all_human_results'][-4] == 'lose' and state['all_human_choice'][-4] != state['all_human_choice'][-3] and state['all_human_results'][-2] == 'win':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['lose']['change']['win']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['lose']['change']['win']['same'] += 1
    
    elif state['all_human_results'][-4] == 'lose' and state['all_human_choice'][-4] != state['all_human_choice'][-3] and state['all_human_results'][-2] == 'lose':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['lose']['change']['lose']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['lose']['change']['lose']['same'] += 1
    
    elif state['all_human_results'][-4] == 'lose' and state['all_human_choice'][-4] == state['all_human_choice'][-3] and state['all_human_results'][-2] == 'win':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['lose']['same']['win']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['lose']['same']['win']['same'] += 1
    
    elif state['all_human_results'][-4] == 'lose' and state['all_human_choice'][-4] == state['all_human_choice'][-3] and state['all_human_results'][-2] == 'lose':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['lose']['same']['lose']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['lose']['same']['lose']['same'] += 1
    
    return state