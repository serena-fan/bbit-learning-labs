import pika
import os
import sys

class mqProducer(): 
    
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables
        self.routing_key = routing_key 
        self.exchange_name = exchange_name 
        # Call setupRMQConnection
        self.setupRMQConnection()
        
        # pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        self.conParams = pika.URLParameters(os.environ['AMQP_URL'])
        self.connection = pika.BlockingConnection(parameters=self.conParams)  

        # Establish Channel
        self.channel = self.connection.channel()
        # Create the exchange if not already present
        self.channel.exchange_declare(
            exchange="Exchange Name", exchange_type="topic"
        )
        # pass

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(
            exchange="Exchange Name",
            routing_key="Routing Key",
            body="Message",
        )
        # Close Channel
        self.channel.close()
        # Close Connection
        self.connection.close()
    
        # pass

# print("Name of the program using sys.argv[0]: ", sys.argv[0])
# print("Length of arguments given including program name: ", len(sys.argv))
# print("Argument list: ", sys.argv)
# print("Argument list type: ", type(sys.argv))
# print("Give the first argument (after program name): ", sys.argv[1])
