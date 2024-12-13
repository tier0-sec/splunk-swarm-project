import os

def run_command(command):
    os.system(command)

def update_server_and_time():
    run_command("sudo apt update && sudo apt upgrade -y")
    run_command("sudo timedatectl set-timezone EST")

def install_docker():
    run_command("sudo apt-get update")
    run_command("sudo apt-get install -y ca-certificates curl")
    run_command("sudo install -m 0755 -d /etc/apt/keyrings")
    run_command("sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc")
    run_command("sudo chmod a+r /etc/apt/keyrings/docker.asc")
    run_command('echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
    run_command("sudo apt-get update")
    run_command("sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin")
    run_command("sudo systemctl enable docker")
    run_command("sudo systemctl start docker")

def add_user_to_docker_group():
    run_command("sudo usermod -aG docker $USER")

def verify_docker():
    run_command("docker run hello-world")

def verify_docker_compose():
    run_command("docker-compose --version")
    result = os.system("docker-compose --version")
    if result != 0:
        run_command("sudo rm /usr/local/bin/docker-compose")
        run_command('sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        run_command("sudo chmod +x /usr/local/bin/docker-compose")
        run_command("docker-compose --version")

if __name__ == "__main__":
    update_server_and_time()
    install_docker()
    add_user_to_docker_group()
    verify_docker()
    verify_docker_compose()
