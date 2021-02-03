<img src='https://1.cms.s81c.com/sites/default/files/styles/band_inline_image_standard/public/2019-06/apache-hbase-logo_0.png?itok=GfW4z5QC' alt='HBase logo'></img>

<h2>HBase Section</h2>

<p>This section shows how to run a HBase service and REST on top of it. To know more about HBase, <a href='https://hbase.apache.org/book.html#arch.overview'>click here</a>.</p>

<h3>Enable the REST service on top of HBase</h3>
<p>First, start HBase service, then enable a port in the server to communicate with your client. After that, start the REST Server on top hadoop with (if you are using the HDP, type):</p>

<code>/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8001 --infoport 8002</code>
