import json
import datetime
from utils import colors


def write_json(data, client):

    json_data = {}
    timestamp = datetime.datetime.now().strftime("%m-%d-%Y@%H-%M-%S")
    # add time stamp to json file
    json_data['timestamp'] = timestamp
    # add client info to json file
    json_data['client'] = {
        'ip': client[0],
        'port': client[1]
    }
    # add data to json file
    json_data['data'] = []

    for blob in data:
        value = []
        for val in blob.value:
            value.append('0x' + val.decode('ascii'))
        json_data['data'].append({
            'type': blob.type.decode('ascii'),
            'length': blob.length,
            'value': value
        })
    # Serializing json
    file_path = 'history/' + timestamp + '.json'
    with open(file_path, 'w') as outfile:
        json.dump(json_data, outfile)
