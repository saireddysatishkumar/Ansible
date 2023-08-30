# Ansible

Managing infrastructure through code! Dive into Ansible code snippets for provisioning and configuring resources across cloud platforms.  


``````
- vagrant       #to create a vagrant box
- awsec2        #to create ec2 instance in aws
- main.yaml
        |
        roles   # ansible roles
            |
            - ping-test
            - 
``````

## Prerequisites:

>Setup up the AWX(ansible tower) local environment using minikube.  
[Ansible Tower/AWX](https://github.com/saireddysatishkumar/K8S/tree/main/awx)  

> create aws ec2  
cd awsec2  
terraform init  
terraform apply -var="subnet_id=subnet-0a0578d12a6334d5c" -var="vpc_id=vpc-05d12ae07a7397ab2" -lock=false  

> create vagrant ## vagrant and vmware must be already installed  
cd vagrant  
vagrant up  

> update above instances IP  in hosts file  

ansible-playbook -i hosts main.yaml -u vagrant -b --tags=ping-test -v  

## Important ansible commandline swithes
``````
ansible-playbook -i hosts main.yaml --tags=nginx --step  -v  #interactive steps
ansible-playbook -i hosts main.yaml --tags=nginx --check  -v  #dryrun
ansible-playbook -i hosts main.yaml --tags=nginx --start-at-task="healthChecker" #To start from a task
``````
``````
ansible-playbook -i hosts main.yaml --tags=ping-test --list-tasks #shows tasks and tags
ansible-playbook -i hosts main.yaml --tags=ping-test --list-tags #shows tags
ansible-playbook -i hosts main.yaml --tags=ping-test --list-hosts #shows hosts
ansible-playbook -i hosts main.yaml --tags=ping-test --syntax-check #checks syntax
``````


## UseCase: 1 : Ansible playbook "block"
### Blocks can help in organizing code, but also enable rollbacks or output data for critical changes.  
[Ref: Document](https://www.redhat.com/sysadmin/ansible-block-rescue)

## UseCase: 2 : Ansible Vault
### variable selection:

