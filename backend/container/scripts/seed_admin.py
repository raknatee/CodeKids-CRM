"""
    docker compose -f _compose/dev/docker-compose.dev.all.yaml -p codekids-crm \\
        exec backend python scripts/seed_admin.py <email> "Name"
"""

import sys

from codekids_crm_backend.core.db import get_database
from codekids_crm_backend.users.models import Role
from codekids_crm_backend.users.repository import UserAlreadyExistsError, UserRepository


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python scripts/seed_admin.py <email> [name]")
        sys.exit(1)

    email = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else None

    repo = UserRepository(get_database())
    try:
        user = repo.create({"email": email, "role": Role.ADMIN, "name": name})
    except UserAlreadyExistsError:
        print(f"user email={email} already exists — skip")
        return

    print(f"created admin user_id={user['user_id']} email={user['email']}")


if __name__ == "__main__":
    main()