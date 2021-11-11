from cassandra.cluster import Cluster
from cassandra.query import named_tuple_factory
from cassandra.auth import PlainTextAuthProvider


def connect_dataset():
    client_id = 'eqGJcMRfbvJCggwzlZFrFuar'
    client_secret = 'Rnn,eM323,ZSpZHGgXGPLLGddMxslotgkgKNmrs5.-YvSyB8SwmrIQAPsb-cIL1y6G3HuTbGhhz1Kg' \
                    '+Cg14ArErpKPIIsZ4Y9u9lJuf6+Q7B7um2QBXPcEETNwTsmOjB '
    cloud_config = {
        'secure_connect_bundle': './secure-connect-bankbot.zip'
    }
    auth_provider = PlainTextAuthProvider(client_id, client_secret)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    session.row_factory = named_tuple_factory
    return session
