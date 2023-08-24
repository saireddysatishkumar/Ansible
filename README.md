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

ansible-playbook -i hosts main.yaml --tags=nginx -u vagrant -b

## UseCase: 1 : Dynamic inventory(aws)
https://www.cloudthat.com/resources/blog/step-by-step-guide-to-integrate-ansible-dynamic-inventory-plugin-for-aws-ec2-instances
ansible-inventory --graph -vvv

## UseCase: 2 :