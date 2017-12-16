#// 1 START OMIT
from fabric.api import local, settings, run, env

# Lista servera
env.hosts = ["server.sedamcvrkuta.com"]
# SSH korisnik
env.user = "root"

# Varijable servisa
name = "primer2"
port = 8000
repository = "janos/radionica-primer2"
network = "radionica"
pg_user = "radionica"
pg_pass = "P4ss"
pg_port = 5432
pg_version = "9.6.2"
pg_volume = "radionica-postgres-data"
#// 1 END OMIT


#// 2 START OMIT
def build(tag=""):
    if tag is not "":
        tag = ":" + tag
    local(f"docker build -t {repository}{tag} .")


def push(tag=""):
    local(f"docker push {repository}{tag}")


def create_network():
    local(f"docker network create {network}")
#// 2 END OMIT

#// 3 START OMIT
def start(tag=""):
    local(f"""
        docker run -d \
            --name {name} \
            --net {network} \
            -p {port}:{port} \
            {repository}{tag}
        """)


def stop():
    local("docker stop {}".format(name))
    local("docker rm {}".format(name))


def restart():
    start()
    stop()
#// 3 END OMIT

#// 4 START OMIT
def db_start():
    with settings(warn_only=True):
        local(f"docker volume create {pg_volume}")
    local(f"""
        docker run -d \
            --name radionica-postgres \
            --net {network} \
            --restart unless-stopped \
            -e POSTGRES_USER={pg_user} \
            -e POSTGRES_PASSWORD={pg_pass} \
            -v {pg_volume}:/var/lib/postgresql/data \
            -p 127.0.0.1:5432:5432 \
            postgres:{pg_version}
        """)


def db_stop():
    local("docker stop radionica-postgres")
    local("docker rm radionica-postgres")
#// 4 END OMIT

#// 5 START OMIT
def deploy_db():
    with settings(warn_only=True):
        run(f"docker volume create {pg_volume}")
        run(f"docker network create {network}")
    run(f"""
        docker run -d \
            --name radionica-postgres \
            --net {network} \
            --restart unless-stopped \
            -e POSTGRES_USER={pg_user} \
            -e POSTGRES_PASSWORD={pg_pass} \
            -v {pg_volume}:/var/lib/postgresql/data \
            postgres:{pg_version}
        """.)
#// 5 END OMIT

#// 6 START OMIT
def deploy(tag=""):
    build(tag)
    push(tag)
    with settings(warn_only=True):
        run(f"docker stop {name}")
        run(f"docker rm {name}")
        run(f"docker network create {name}")
    run(f"""
        docker run -d \
            --name {name} \
            --net {network} \
            -p {port}:{port} \
            {repository}{tag}
        """)
#// 6 END OMIT
