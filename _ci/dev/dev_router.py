from _ci.config import DEV_PROJECT_NAME
from _ci.dev.dev_handler import DevHandler
from _ci.mongo import mongo_container_helper
import typer # type: ignore



dev_router = typer.Typer()
@dev_router.command("start")
# @dev_router.command("start", help=START_CONTAINER_HELP)
def start_endpoint()->None:
    compose_path = "./_compose/dev/docker-compose.dev.all.yaml"
    DevHandler(compose_path, DEV_PROJECT_NAME).start()
    # mongo_container_helper.setup()
    
@dev_router.command("stop")
def stop_endpoint()->None:
    compose_path = "./_compose/dev/docker-compose.dev.all.yaml"
    DevHandler(compose_path, DEV_PROJECT_NAME).stop()