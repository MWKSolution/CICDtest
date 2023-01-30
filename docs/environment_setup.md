# On VBox with Ubuntu
1. Configure VBox Host-Only Ethernet Adapter for each service

## Ubuntu
1. disable GUI  
2. install open-ssh

## Docker
1. Install Docker on Ubuntu  
https://docs.docker.com/engine/install/ubuntu/  
2. Make it remote  
https://docs.docker.com/config/daemon/remote-access/  
    > configure with systemd, deamon.json dont work !!!  
    change 127.0.0.1 to 0.0.0.0

## Jenkins
1. Install Jenkins on Ubuntu  
https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-22-04  
2. Open firewall
    > opening firewall wasn't necessary  
3. Continue with jenkins configuration...  
    > for changing GUI language to english - install plugin locale
   > in configuration locale change lan to en_US

    > docker containers as build agents: instal plugin docker

    > to get crumb data for jenkins plugin in pycharm: http://<jenkins_url>/crumbIssuer/api/json?tree=crumb  
   > log with api token created in jenkins instead of password!!!!
    
   > configure clouds - docker

   