from fabric.api import *
import fabric

a = "ubuntu@123.206.33.85"

# env.hosts = [
#     a, a, a
# ]

env.dedupe_hosts = False  # 列表主机可重复

env.roledefs = {
    "ubuntu": [a]
}

env.passwords = {
    a: "4dAGX7~fU4T4mDD="
}

env.sudo_passwords = {
    a: "4dAGX7~fU4T4mDD="
}


@roles('ubuntu')
def ls():
    env.password = env.passwords[env.host_string]
    print(env.host_string)
    env.sudo_password = env.sudo_passwords[a]
    with settings(warn_only=True):
        print(run("ls"))
        sudo("ls")
