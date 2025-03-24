

def update_weights(state):
    if state['all_human_results'][-2] == 'win':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['win']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['win']['same'] += 1
    elif state['all_human_results'][-2] == 'loss':
        if state['all_human_choice'][-2] != state['all_human_choice'][-1]:
            state['strategy']['loss']['change'] += 1
        elif state['all_human_choice'][-2] == state['all_human_choice'][-1]:
            state['strategy']['loss']['same'] += 1
    return state