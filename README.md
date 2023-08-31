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


## : Ansible playbook "block" :
### Blocks can help in organizing code, but also enable rollbacks or output data for critical changes.  
[Ref: Document](https://www.redhat.com/sysadmin/ansible-block-rescue)

## : Ansible Vault :
### Example1:
``````
cd vault-example
# Encrypt variables file( In this example it includes docker hub creds) with vault.
ansible-vault encrypt vars/vault.yaml

#Include encripted vars in playbook
  tasks:
    - name: Include vault for registry login
      include_vars:
        file: vars/vault.yaml
    - name: Log into Docker Registry and force re-authorization
      docker_login:
        registry: registry-1.docker.io
        username: "{{docker_user}}"
        password: "{{docker_pass}}"
# Run playbook with runtime argument --ask-valut-pass        
ansible-playbook -i ../hosts deploy-web.yaml --ask-vault-pass -v
``````
## : [Molecule](https://www.ansible.com/hubfs/AnsibleFest%20ATL%20Slide%20Decks/Practical%20Ansible%20Testing%20with%20Molecule.pdf) : 
- Install yamllint, ansible-lint, and molecule.
``````
pip3 install yamllint
pip3 install ansible-lint
brew install molecule (or) pip3 install molecule
pip3 install molecule-docker
pip3 install lint
``````
- In Mac, make sure the the following change ~/.docker/config.json 
"credsStore": "desktop" - ISSUE
"credStore": "desktop"  - FIXED

- Initialize molecule scenario from playbook role.
molecule init scenario --driver-name docker
Note: update tasks and playbook in converge.yml according to requirements.


- Run molecule converge from example apache2
cd apache2 
molecule converge #It will run molecule and leave container running for verifying
molecule destroy
MOLECULE_DISTRO=Debian10 molecule converge
MOLECULE_DISTRO=Debian10 molecule destroy

- Run molecule Verify
molecule verify

molecule test
#To change runtime container to debian10
MOLECULE_DISTRO=Debian10 molecule test  # It will spin container for molecule to test playbook, then destorys.




## : Ansible Galaxy :
``````
============================================================================
$ ansible-galaxy --version
ansible-galaxy 2.4.2.0
============================================================================
ansible-galaxy install --roles-path . -r requirements.yml
ansible-galaxy --offline init role_name
============================================================================
ansible-galaxy install -r requirements.yml
ansible-playbook playbook.yml -i inventory 
============================================================================
ANSIBLE_ROLES_PATH -> The default path is /etc/ansible/roles
ANSIBLE_ROLES_PATH -> Ansible Galaxy saves every role you install and look when resolving the imports from your playbook
============================================================================
ansible-galaxy init role_name -> Initialize the base structure of a new role
ansible-galaxy search *jenkins* -> List of roles filtered
ansible-galaxy install geerlingguy.jenkins -> Download roles from the Galaxy website
============================================================================
Find ansible role's id in ansible-galaxy -> ansible-galaxy info YourUser.RoleName | grep -E 'id: [0-9]' | awk {'print $2'}
View all ansible role details -> ansible-galaxy info YourUser.RoleName
============================================================================
``````
