<div align='center'>
    <img src='https://ourcodeworld.com/public-media/articles/articleocw-5d78ebb022d1e.webp' alt='NoSQL logo' width='800px'></img>
</div>

<h2>Feeding Data Section</h2>

<p>This section shows how to publish/consume data to our cluster with Kafka and Flume.

<h3>Running an example with Kafka</h3>
<p>First create a topic to publish and consume data. Goes where Kafka lives and type the following command line:</p>
<code>./kafka-topics.sh --create --zookeeper sandbox-hdp.hortonworks.com:2181 --replication-factor 1 --partitions 1 --topic kafkaExample</code><br/>
<p>Then, to publish some data, type:</p>
<code>./kafka-console-producer.sh --broker-list sandbox-hdp.hortonworks.com:6667 --topic kafkaExample</code><br/>
<p>Type some random text to see the results in consumer.
To consume these text, you need to get another terminal instance, goes where kafka lives and do the following:</p>
<code>./kafka-console-consumer.sh --bootstrap-server sandbox-hdp.hortonworks.com:6667 --topic kafkaExample --from-beginning</code><br/>
