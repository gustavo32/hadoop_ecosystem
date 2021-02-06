users = LOAD '/user/maria_dev/data/users.user' USING PigStorage('|') AS
(userId:int, age:int, gender:chararray, title:chararray, zip:chararray);

STORE users INTO 'hbase://users'
USING org.apache.pig.backend.hadoop.hbase.HBaseStorage
('userinfo:age, userinfo:gender, userinfo:title, userinfo:zip');