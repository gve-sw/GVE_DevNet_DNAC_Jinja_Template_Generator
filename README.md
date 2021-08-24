# GVE_DevNet_DNAC_Jinja_Template_Generator
script that reads a config file then creates a jinja template based on the information from a stack of 24 port Catalyst 2960 switches and convert it into a configuration of 48 ports Catalyst 9300 switches. The template is then pushed onto DNAC.


## Contacts
* Jorge Banegas

## Solution Components
* DNAC
* Catalyst
* PRIME

## Installation/Configuration
Create and enter virtual environment

```bash
virtualenv env
source env/bin/activate
```

Install project dependencies

```bash
pip install -r requirements.txt
```
Include the credentials of your DNAC/Prime instance inside the config.py file

```python
PI=""
USER=""
PASSWORD=""

USER_DNAC=""
PASS_DNAC=""
DNAC=""
```

Be sure to include the ios configuration file inside the project folder and name it config.txt

Run python prime.py or ssh.py, if you want to install the configuration file from prime (will need prime credentials). prime.py will retrieve the configuration using prime APIs and ssh.py will use ssh to retrieve "show startup-config" results and will generate the config.txt file.  

```bash
python ssh.py
```

```bash
python prime.py
```

Run python main script to create the new jinja template

```bash
python main.py
```

Run python converter script to submit the jinja template onto your dnac instance

Be sure to include an existing DNAC project name

```python
#TODO: Enter the DNAC template project name 
TEMPLATE_PROJECT_NAME = "GVE_DevNet_Jorge"
```

```bash
python converter.py
```

# Screenshots
Starting the main.py script, it will parse the configuration file called config.txt and display all the line cards. User will select which line cards to transfer over. 

![/IMAGES/step1.png](/IMAGES/step1.png)

Next, the script will display all the switches from the DNAC environment. Select the 48 port stacked switch. 

![/IMAGES/step2.png](/IMAGES/step2.png)

Will parse the configuration of the selected devices and display all the line cards. User will select which line cards and then it will create a template consisting of the 2:1 port mapping from the 24 port stacks switch to the 48 port stacks switch. 

![/IMAGES/step3.png](/IMAGES/step3.png)

Running the converter script will push the jinja2 template onto the dnac instance.

![/IMAGES/converter.png](/IMAGES/converter.png)

Now, the newly created template is pushed onto the DNAC environment

![/IMAGES/dnac_template.png](/IMAGES/dnac_template.png)


![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
