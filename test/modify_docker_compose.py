#!/usr/bin/env python
#
# Modify Rucio's docker-compose.yml to add MetaCat container
# and MetaCat environment variable in Rucio server container.
#
# Requires PyYAML
#

import sys
import yaml

if len(sys.argv) != 3:
    print("Usage: python modify_docker_compose.py <input file> <output file>")
    sys.exit(1)

f = open(sys.argv[1], 'r')
docker_compose = yaml.safe_load(f)
f.close()

docker_compose["services"]["rucio"]["environment"].append("METACAT_SERVER_URL=http://dev-metacat-1:8080/")
docker_compose["services"]["metacat"] = {
    "image": "docker.io/jamespepcc/metacat_test",
    "ports": [ "127.0.0.1:8000:8080" ]
}

f = open(sys.argv[2], 'w')
yaml.dump(docker_compose, f)
f.close()
