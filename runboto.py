#This part of the application launches the EMR
#Lives on the openstack instance (usr/local/hybrid )

import os
import boto.emr
import time
from boto.emr.connection import EmrConnection
from boto.emr.instance_group import InstanceGroup
from boto.emr.step import StreamingStep
conn = EmrConnection('//accesskey', '//secretkey')
from boto.emr.step import StreamingStep
holder='agbocloudmsc2015mapreduce'
step = StreamingStep(name='Streamer',
        mapper='s3://'+holder+'/indexer/indexmap.py',reducer='s3://'+holder+'/i$
        input='s3://'+holder+'/indexer/input/suspicious/',output='s3://'+holder$
conn = boto.emr.connect_to_region("eu-west-1")

#noofnodes +=  
instance_groups = []
instance_groups.append(InstanceGroup(
    num_instances=1,
    role="MASTER",
    type="m1.large",
    market="ON_DEMAND",
    name="Main node"))
instance_groups.append(InstanceGroup(
    num_instances=6,
    role="CORE",
    type="m1.large",
    market="ON_DEMAND",
    name="node"))
instance_groups.append(InstanceGroup(
    num_instances=6,
    role="TASK",
	type="m1.large",
	    market="SPOT",
	    name="spot node",
	    bidprice="0.004"))

	job_id = conn.run_jobflow(
	'MyCluster',
	instance_groups=instance_groups,
	action_on_failure='TERMINATE_JOB_FLOW',
	keep_alive=False,
	enable_debugging=True,
	log_uri='s3://'+holder+'/log',
	hadoop_version=None,
	ami_version="2.4.9",
	steps=[step],
	bootstrap_actions=[],
	ec2_keyname='euireland1kp',
	visible_to_all_users=True,
	job_flow_role="EMR_EC2_DefaultRole",
	service_role="EMR_DefaultRole")