from _ci.pkg.shell import run_shell

def run_docker_context_default()->None:
    run_shell(f"docker context use default")
    

    
