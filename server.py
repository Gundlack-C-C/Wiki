from flask import Flask, redirect, url_for, jsonify
from flask_cors import CORS

import logging
import argparse
import os, sys
from wiki_api import get_random_wiki, get_wiki

app = Flask(__name__)
CORS(app)

app.add_url_rule("/", endpoint="index", build_only=True)
app.add_url_rule("/random", endpoint="random", build_only=True)

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('random'))

@app.route('/get/<name>', methods=['GET'])
def get(name):
    return jsonify(get_wiki(name))


@app.route('/random', methods=['GET'])
def random():
    return jsonify(get_random_wiki())

if __name__ == '__main__':

    try:
        LOG = "./.log/wiki-server.log"

        # Setup Argument Parser
        parser = argparse.ArgumentParser(description='Argument Parser')
        parser.add_argument('-l', '--log', dest='LOGFILE', type=str, default=LOG,
                            help=f'path for logfile (default: {LOG})')
        parser.add_argument("--production", action='store_const', help="set to production mode", const=True, default=False)

        args = parser.parse_args()
        # Check if production is set
        PRODUCTION = args.production
        os.environ['PRODUCTION'] = str(PRODUCTION)
        port = int(os.environ.get('PORT', 5001))
        
        if not os.path.exists(os.path.abspath(os.path.dirname(args.LOGFILE))):
                os.makedirs(os.path.abspath(os.path.dirname(args.LOGFILE)))

      
        # Setup Logging
        logging.basicConfig(filename=args.LOGFILE, level=logging.INFO if PRODUCTION else logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s')
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

        logging.info(f"Starting Server with [{args}] and test")
        
        # Start Server
        app.run(host="0.0.0.0", debug=False, port = port)

    except Exception as e:
        logging.error(e)
