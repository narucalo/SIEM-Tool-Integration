import json
import splunklib.client as client
import splunklib.results as results
import configparser

def load_config():
    """Load configuration from config.ini."""
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config['Splunk']

def connect_to_splunk(config):
    """Connect to the Splunk server using the provided configuration."""
    service = client.connect(
        host=config['host'],
        port=config['port'],
        username=config['username'],
        password=config['password']
    )
    return service

def ingest_data(service, index_name, data):
    """Ingest data into the specified Splunk index."""
    index = service.indexes[index_name]
    index.submit(json.dumps(data))

if __name__ == '__main__':
    config = load_config()
    service = connect_to_splunk(config)
    with open('data/sample_data.log') as f:
        sample_data = f.readlines()
    for event in sample_data:
        ingest_data(service, 'main', {"event": event.strip()})
