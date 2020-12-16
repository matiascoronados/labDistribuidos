from kafka import KafkaConsumer
from json import loads
try:
    consumer = KafkaConsumer(
   'Temas',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=["34.68.42.248:9091"])

    for m in consumer:
        print(m.value)
except expression as identifier:
    print('mati')
