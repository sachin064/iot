from flask import Flask
from sample import get_records
from elasticsearch import Elasticsearch

app = Flask(__name__)

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def get_device_data():
    query = "SELECT * from device_data"
    records = get_records(query)
    return records


def data_parser_v2(records):
    data_dict = {}
    for record in records:
        print(type(record[4]))
        parsed_data = record[4].replace('[', '').replace(']', '').replace('}', '').replace('{', '').split(',')
        for i in range(0, len(parsed_data), 5):
            data_dict['id'] = parsed_data[0].split(':')[1].replace('"', '')
            data_dict['variable'] = parsed_data[1].split(':')[1].replace('"', '')
            data_dict['created_on'] = parsed_data[2].split(':', 1)[1].replace('"', '')
            data_dict['updated'] = parsed_data[3].split(':', 1)[1].replace('"', '')
            data_dict['is_warning'] = parsed_data[4].split(':')[1].replace('"', '')
        print(parsed_data)


def data_parser(records):
    index = "device_data"
    doc_type = "device"
    print(records)
    labels = ["id", "device_id", "variable", "data", "iot_data", "created_at", "updated_at", ]
    idx = 0
    dictr = {}
    for record in records:
        for i in range(len(labels)):
            dictr[labels[i]] = record[i]
        res = es.index(index=index, doc_type=doc_type, id=idx, body=dictr)
        print(res)
        idx += 1
    return dictr


if __name__ == "__main__":
    # res = es.get(index='index', doc_type='doctype', id=0)
    # print(res)
    data = get_device_data()
    data_parser_v2(data)
    # print('data received')
    # data_parser(data)
    app.run(debug=True)
