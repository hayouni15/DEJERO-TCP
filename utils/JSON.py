import json
import datetime

def write_json(data,client):
    json_data = {}

    json_data['client']={
        'ip':client[0],
        'port': client[1]
    }

    json_data['data']=[]

    for blob in data:
        value=[]
        for val in blob.value :
            value.append(val.decode('ascii'))
        json_data['data'].append({
            'type': blob.type.decode('ascii'),
            'length':blob.length,
            'value':value
        })

    print('TLV-Json saved :',json_data)

    # Serializing json
    file_path='history/'+datetime.datetime.now().strftime("%m-%d-%Y@%H-%M-%S")+'.json'
    print (name)
    with open(name, 'w') as outfile:
        json.dump(json_data, outfile)
