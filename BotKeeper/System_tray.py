from pystray import Icon, MenuItem
from PIL import Image
import subprocess

DOCKER_COMPOSE_PATH = "D:/Python/BotKeeper/docker-compose.yml"

def start_container(icon, item):
    subprocess.Popen(['docker-compose', '-f', DOCKER_COMPOSE_PATH, 'up', '-d'])
    icon.visible = False

def stop_container(icon, item):
    subprocess.Popen(['docker-compose', '-f', DOCKER_COMPOSE_PATH, 'down'])
    icon.visible = False

def main():
    image = Image.open("Process.png")

    icon = Icon("Chatbot", image)

    menu_items = [
        MenuItem('Start', lambda icon, item: start_container(icon, item)),
        MenuItem('Stop', lambda icon, item: stop_container(icon, item))
    ]

    icon.menu = menu_items
    
    icon.run()

if __name__ == "__main__":
    main()
