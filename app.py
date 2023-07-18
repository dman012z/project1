from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def backup():
    {'date': '2024-12-06T15:00:00Z',
         'action': 'TBA',
         'command': 'TBD',
         'status': 'SUCCESS'
         },
        {'date': '2024-12-07T16:00:00Z',
         'action': 'TBA',
         'command': 'TBD',
         'status': 'FAILED'
         }



if __name__ == '__main__':
    app.run(host='0.0.0.0')

