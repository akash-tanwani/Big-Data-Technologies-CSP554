Use scp to move the hql.zip demo file to your EMR master node (/home/hadoop).

Once the demo file is on your master node decomporess it using 'unzip hql.zip'.

To use this demo make sure your current directory is /home/hadoop/hql
by doing 'cd /home/hadoop/hql'.

Then start up the Hive CLI by entering 'hive'.

Now enter the following into the Hive CLI:
1) source ./basicsetup.hql;
2) source ./partsetup.hql;
3) source ./salaries.hql;
4) source ./loadsalaries.hql;
5) source ./salaries2.hql;
6) source ./salaries3.hql;



