scenario 1:

The content below is part of a configuration for AWX. I need to copy and change a parts of the content inorder to apply it to (PE,QA,PROD) for both SMB and AV. 

Write a playbook that will loop through the content and provide the output to a file named: `output_results.yml`.
Desired output(see file) is a yaml file with a list of 6 different items under `controller_workflows:` (PE/QA/Prod) AV and (PE,QA,PROD) SMB


########################## content ############################
controller_workflows:
  - name: {{ PE }} Broadsoft - RI {{ AV }} Install 2.9_3.x
	description: This Workflow includes VM cloning from the existing template and install broadsoft on top of it
	extra_vars:
	  application: broadsoft
	  app_domain: {{ AV }}   
	survey_enabled: true
	allow_simultaneous: false
	ask_variables_on_launch: false
	inventory:
	state: present
	limit:
	ask_labels_on_launch: false
	ask_skip_tags_on_launch: false
	labels:
	  - {{ PE }}
	scm_branch:
	ask_inventory_on_launch: true
	ask_scm_branch_on_launch: false
	ask_limit_on_launch: false
	organization: Test_Org
	schedules:
	simplified_workflow_nodes:
################################################################## 


requirements:
- create a task to or playbook to formulate desire result
- provide an explanation on your thought process
