import subprocess
from subprocess import CompletedProcess


def run_shell(command:str)->int:
    print(command)
    subprocess.run(command, shell=True)
    return 0

def run_shell_and_get_result(command: str)->tuple[str, str, int]:
    print(command)
    process_result: CompletedProcess[bytes] = subprocess.run(command, shell=True, capture_output=True)
    return process_result.stdout.decode(), process_result.stderr.decode(), process_result.returncode