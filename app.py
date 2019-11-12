from flask import Flask
from sample import get_records
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
app = Flask(__name__)
if __name__ == "__main__":
    print("hi")


    def get_device_data():
        index = "device_data"
        doc_type = "device"
        query = "SELECT * from device_data LIMIT 50"
        records = get_records(query)
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


    # res = es.get(index='index', doc_type='doctype', id=0)
    # print(res)

    data = get_device_data()

    app.run(debug=True)
