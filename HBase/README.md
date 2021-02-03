<img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ibm.com%2Fanalytics%2Fhadoop%2Fhbase&psig=AOvVaw1YjtBMEiflMrLpR09N5SQl&ust=1612470724622000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODy2NjHzu4CFQAAAAAdAAAAABAJ' alt='HBase logo'></img>

<h2>HBase Section</h2>

<p>This section shows how to run a HBase service and REST on top of it. To know more about HBase, <a href='https://hbase.apache.org/book.html#arch.overview'>click here</a>.</p>

<h3>Enable the REST service on top of HBase</h3>
<p>First, start HBase service, then enable a port in the server to communicate with your client. After that, start the REST Server on top hadoop with (if you are using the HDP, type):</p>

<code>/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8001 --infoport 8002</code>
