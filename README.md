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

ansible-inventory --graph -vvv