# Ansible
``````
vagrant #to create a vagrant box
awsec2  #to create ec2 instance in aws
main.yaml
        |
        roles   # ansible roles
            |
            - ping-test
            - 
``````

## Prerequisites:
> create aws ec2
cd awsec2
terraform init  
terraform apply -var="subnet_id=subnet-vvvvvvvvv" -var="vpc_id=vpc-xxxxx" -lock=false  

> create vagrant ## vagrant and vmware must be already installed
cd vagrant
vagrant up

> update above instances IP  in hosts file 

ansible-playbook -i hosts main.yaml -u vagrant -b --tags=ping-test -v

## Imp swithes
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

## UseCase: 1 : Dynamic inventory(aws)
https://www.cloudthat.com/resources/blog/step-by-step-guide-to-integrate-ansible-dynamic-inventory-plugin-for-aws-ec2-instances  
ansible-inventory --graph -vvv

## UseCase: 2 : Block
### Blocks can help in organizing code, but also enable rollbacks or output data for critical changes.  
[Ref:](https://www.redhat.com/sysadmin/ansible-block-rescue)