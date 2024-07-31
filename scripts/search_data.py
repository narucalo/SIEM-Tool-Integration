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

def search_data(service, query):
    """Search data in Splunk using the provided query."""
    job = service.jobs.create(query)
    for result in results.ResultsReader(job.results()):
        print(result)

if __name__ == '__main__':
    config = load_config()
    service = connect_to_splunk(config)
    query = 'search index=main | head 10'
    search_data(service, query)
