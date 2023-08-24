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

ansible-playbook -i hosts main.yaml --tags=nginx -u vagrant -b


## UseCase: 1 : Dynamic inventory(aws)
https://www.cloudthat.com/resources/blog/step-by-step-guide-to-integrate-ansible-dynamic-inventory-plugin-for-aws-ec2-instances  
ansible-inventory --graph -vvv

## UseCase: 2 :