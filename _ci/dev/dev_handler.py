from _ci.pkg.docker_helper import run_docker_context_default
from _ci.pkg.shell import run_shell


class DevHandler:
    compose_path : str
    project_name: str
    
    def __init__(self, compose_path: str, project_name:str)->None:
        self.compose_path = compose_path
        self.project_name = project_name
        
        run_docker_context_default()
        
        
    def start(self)->None:
        self.stop()
        run_shell(f"docker compose -f {self.compose_path} -p {self.project_name} up --build -d")
        
    def stop(self)->None:
        run_shell(f"docker compose -f {self.compose_path} -p {self.project_name} down")
        
    def use_docker(self, cmd: str)->None:
        
        run_shell(f"docker compose -f {self.compose_path} -p {self.project_name} {cmd}")
        
        
        