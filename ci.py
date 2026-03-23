import sys

from _ci.dev.dev_router import dev_router
import typer # type: ignore


app = typer.Typer()

app.add_typer(dev_router, name="dev")


@app.callback()
def main()->None:
    pass

@app.command("shell", help="runing in interactive mode (future work)")
def run_loop()->None:
    while True:
        input("<<")

    
    
if __name__ == "__main__":
    app()