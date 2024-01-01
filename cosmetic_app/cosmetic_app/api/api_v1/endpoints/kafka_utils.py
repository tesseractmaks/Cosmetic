import json

from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
import pickle
from confluent_kafka import Consumer as ConfluentConsumer

# confluent_consumer = ConfluentConsumer({
#             'bootstrap.servers': ','.join(frame_config.KAFKA_BOOTSTRAP_SERVERS),
#             'group.id': 'frame_group',
#             'auto.offset.reset': 'earliest',
#             'enable.auto.commit': False
#         })


def get_consumer(topic):
    consumer = KafkaConsumer(
        f"{topic}",
        auto_offset_reset="earliest",
        bootstrap_servers=["127.0.0.1:9092"],
        api_version=(0, 10),
        max_poll_records=1000,
        # consumer_timeout_ms=100,
        # group_id="live-query-daac779b-a20d-41b2-868b-e90227949bf3",
    )

    for records in consumer:

        record = json.loads(records.value)
        # print(record, "+++")

        if consumer is not None:
            consumer.close()
        return record


def create_producer(values):
    kafka_producer = KafkaProducer(
        bootstrap_servers=["127.0.0.1:9092"],
        api_version=(0, 10),
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    # value = pickle.dumps(value_raw)
    try:
        # key_bytes = bytes(key, encoding="utf-8")
        # value_bytes = bytes(value, encoding="utf-8")

        # key_bytes = pickle.dumps(key)
        # value_bytes = pickle.dumps(value)
        kafka_producer.send(values["topic"], value=values)

        kafka_producer.flush()

        # print("Send Success! - ", values["topic"])
    except Exception as exc:
        print("--")
        print(str(exc))
    if kafka_producer is not None:
        kafka_producer.close()


# def get_consumer():
#     consumer = KafkaConsumer(
#         "users",
#         auto_offset_reset="earliest",
#         bootstrap_servers=["127.0.0.1:9092"],
#         api_version=(0, 10),
#         consumer_timeout_ms=1000
#     )
#     records = pickle.loads(consumer.value)
#     print(records)
#     for record in records:
#         print(record["users"])

# create_producer("hello", topic_name='users')
# res = get_consumer()
# res2 = get_consumer1()

# print(res)
# print(res2)


# Groups
# client = KafkaAdminClient(bootstrap_servers="localhost:9092")
# for group in client.list_consumer_groups():
#     print(group[0])
