<div style='text-align:center'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Apache_Hive_logo.svg/1024px-Apache_Hive_logo.svg.png' alt='Hive logo' width='500px'></img>
</div>

<h2>Hive Section</h2>

<p>This section shows how to use Hive. To know more about Hive, <a href='https://hive.apache.org/'>click here</a>.</p>

<h3>Import data to hive from MySQL</h3>

<p>Set the database privileges to the server, to be possible import data to hive</p>
<code>mysql -u root -p</code>
<code>GRANT ALL PRIVILEGES ON movielens.* TO ''@'localhost';</code>
<code>exit</code>

<p>After that, import data with sqoop:</p>
<code>sqoop import --connect jdbc:mysql://localhost/movielens --driver com.mysql.jdbc.Driver -- table movies</code>


<h3>Export data to MySQL from Hive</h3>

<p>First, create your table on mysql to hadoop export to it:</p>
<code>mysql -u root -p</code>
<code>CREATE DATABASE movielens;</code>
<code>USE movielens;</code>
<code>CREATE TABLE movies (movieId INTEGER, title VARCHAR(255), releaseDate DATE);</code>
<code>exit</code>

<p>After, export the hive table to mysql with the following command:</p>
<code>sqoop export --connect jdbc:mysql://localhost/movielens --driver com.mysql.jdbc.Driver --table movies --export-dir /apps/hive/warehouse/movies --input-fields-terminated-by '\0001' --username `YOUR_USERNAME` --password `YOUR_PASSWORD`</code>

<h3>Codes using HiveQL</h3>
<ul>
<li>most_loved_movies.hql -> here, we find the movies with the highests ratings. Also, we filter just the movies with more than 10 rates</li>
<li>most_watched_movies.hql -> here, we find the movies more rated.</li>
</ul>

