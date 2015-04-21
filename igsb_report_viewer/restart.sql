drop database if exists report_viewer;
show databases;
create database if not exists report_viewer;
grant all on report_viewer.* to jgrundst@localhost identified by 'wh!tel@b';
grant all on report_viewer.* to jgrundst@127.0.0.1 identified by 'wh!tel@b';
flush privileges;
use report_viewer;
insert into viewer_caller(name) values('MuTect');
insert into viewer_caller(name) values('VarScan');
