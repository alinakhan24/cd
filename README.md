Report
3 Topics:
....................................................................
Nginx Server
....................................................................
Nginx ("engine x") is an HTTP web server, reverse proxy, content cache, load balancer, TCP/UDP proxy server, and mail proxy server. Originally written by Igor Sysoev and distributed under the 2-clause BSD License.
NGINX can manage incoming and outgoing traffic as a reverse proxy server and API gateway, acting as an intermediary for client requests seeking resources from other servers.
When a user requests a web page, NGINX quickly locates and serves the necessary static content.
The NGINX reverse proxy acts as a mediator that handles client requests before they reach the back-end servers.
Implementing NGINX as a reverse proxy protects back-end servers from direct exposure to the internet

...............................................................................
Digital Ocean
...............................................................................
DigitalOcean is a cloud hosting provider that offers cloud computing services and Infrastructure as a Service (IaaS).
Droplets are Linux-based virtual machines (VMs) that run on DigitalOcean hardware. Each virtual machine is a droplet.To deploy DigitalOcean's IaaS environment, developers 
launch a private virtual machine (VM) instance, which the company calls a droplet. 
..............................................................................
Github Actions
...............................................................................
GitHub Actions is a feature of GitHub. GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows to automate build, test, and deployment pipeline.
With GitHub Actions, developers can define workflows that describe how the code should be built, tested, and deployed. These workflows can be triggered automatically based on certain events, 
such as code pushes or pull requests.
Workflow is a YAML file that defines a set of actions that should be performed automatically when a certain event occurs within a project.
.......................................................................................................
How Nginx , Digital Ocean and Github Actions relate with eachother
.......................................................................................................
First of all, I configure Nginx Server as the reverse proxy in Digital Ocean ( which acts as hosting provider),  
which sends incoming HTTP requests to Gunicorn. Gunicorn then prepares a response by using simple Flask application as an example and returns it to NGINX, which then sends it back to the client again. 
To deploy this simple Flask application to Digital Ocean, Github Actioins have been implemented, which took care of building solution, testing and then logging into droplet to copy the files from 
github repo to Digital Ocean VPS using SCP.

...........................................................................................................
3 Problems
..........................................................................................................
A - Unable to install Gunicorn in Virtual Machine
Error:  This environment is externally managed. 
Solution: I used Virtual environments isolate your Python packages, ensuring they don’t interfere with
      system-level Python.
     python3 -m venv ~/myenv
     source ~/myenv/bin/activate
     pip install gunicorn --upgrade

B- Running tests in Github Pipeline failing
Error:  Missing dependencies 
Solution:  Including separate txt file in git repo, and configuring pipeline to install the dependencies, before building solution, has prevented pipeline to crash due to missing dependencies.

C- Restarting Gunicorn cause No Gunicorn Service has been found
Solution:  This means that Gunicorn is not running as a systemd service (or it’s not set up 
correctly). Creating a Gunicorn systemd service file, with relevant configuration, pointing the 
server to correct working directory where the flask application has to be hosted, has resolved
the error and allowed to restart Gunicorn on fresh deploy.
