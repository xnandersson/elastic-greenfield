from jinja2 import Template
import os
from subprocess import check_output


def run():
    id = check_output(["docker", "inspect", "--format='{{ .Id }}'", "elastic-greenfield_slapd_1" ]) 
    id = id.strip()[1:-1]
    t = Template(open('templates/filebeat.yml.jinja2').read())
    with open('filebeat.yml', 'w') as f:
        f.write(t.render(
                    id = id))
        
if __name__ == '__main__':
    run()
