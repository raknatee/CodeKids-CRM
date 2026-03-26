from time import sleep
from typing import Final

from _ci.pkg.shell import run_shell_and_get_result


md: Final = """
# Exec cmd to mongo container 
### **container_id**
"""

def setup()->None:
    mongo_ids: list[str] = []
    
        
    stdout, stderr, returncode = run_shell_and_get_result("docker ps")
    for line in stdout.split("\n"):
        if "coredb" in line:
            container_id = line.split()[0]
            mongo_ids.append(container_id)

    
    for container_id in mongo_ids:
        while True:
            print((md.replace("**container_id**", container_id)))
            stdout, stderr, returncode = run_shell_and_get_result(f"docker exec {container_id} bash setmongo.sh")
            print(stdout)
            print(stderr)
            print(f"{returncode}")
            if returncode == 0 or "MongoServerError: already initialized" in stderr:    
                break
            sleep(2)


