import requests
import pandas as pd

def hit_train_view_endpoint():
    url = "https://www3.septa.org/api/TrainView/index.php"
    headers = {'content-type': 'application/json'}
    response = requests.get(url, params=headers).json()
    
    train_to_status_map = {}
    for entry in response:
        train_dict = dict(entry)
        train_id = train_dict['trainno']
        late_status = train_dict['late']
        train_to_status_map[train_id] = late_status

    df = pd.DataFrame(list(train_to_status_map.items()), columns=['train_id', 'late'])
    return df