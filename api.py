import requests
import config
import datetime

CONFIG = config.load_config()

def load_current_values(player):
    result = []
    skill_pos = 0
    full_url = CONFIG['url'] + player
    # 0 - id
    # 1 - level
    # 2 - current experience
    # Making a get request 
    response = requests.get(full_url)

    for values in response.text.split('\n')[1:]:
        content = values.split(',')
        add = False
        type = 'unknown'
        print(content)
        if len(content) == 3:
            add = True
            result.append({
                'player': player,
                'name': CONFIG['skills'][skill_pos],
                'level': int(content[1]),
                'experience': int(content[2]),
                'type': 'skill',
                'request_date': datetime.datetime.now()
            })
            skill_pos += 1
        elif len(content) == 2 and content[0] != "-1" and content[0] != "":
            result.append({
                'player': player,
                'name': CONFIG['skills'][skill_pos],
                'kc': int(content[1]),
                'type': 'scroll' if "Scroll" in CONFIG['skills'][skill_pos] else 'monster',
                'request_date': datetime.datetime.now()
            })
            skill_pos += 1
        
    return result