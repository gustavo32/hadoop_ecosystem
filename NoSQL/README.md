<div align='center'>
    <img src='https://1.cms.s81c.com/sites/default/files/styles/band_inline_image_standard/public/2019-06/apache-hbase-logo_0.png?itok=GfW4z5QC' alt='HBase logo' width='800px'></img>
</div>

<h2>HBase Section</h2>

<p>This section shows how to run a HBase service and REST on top of it. To know more about HBase, <a href='https://hbase.apache.org/book.html#arch.overview'>click here</a>.</p>

<h3>Enable the REST service on top of HBase</h3>
<p>First, start HBase service, then enable a port in the server to communicate with your client. After that, start the REST Server on top hadoop with (if you are using the HDP, type):</p>

<code>sudo su</code><br/>
<code>/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8001 --infoport 8002</code><br/>

<h2>Considerations</h2>
<p>To run the codes in this folder, is necessary properly install cassandra and mongoDB to your cluster.</p>
<p>Remember, mongoDB does not create a default index as Cassandra, so create one over the primary key to get the data more efficiently. To that, use the following code (1 - ascending order; 2 - descending order):</p>
<code>db.`your_collection_name`.createIndex({`your_primary_key`: 1})</code><br/>

