from pystray import Icon, MenuItem
from PIL import Image
import subprocess

# Path to your Docker Compose file
DOCKER_COMPOSE_PATH = "D:/Python/BotKeeper/docker-compose.yml"

def start_container(icon, item):
    subprocess.Popen(['docker-compose', '-f', DOCKER_COMPOSE_PATH, 'up', '-d'])
    icon.visible = False

def stop_container(icon, item):
    subprocess.Popen(['docker-compose', '-f', DOCKER_COMPOSE_PATH, 'down'])
    icon.visible = False

def main():
    # Load icon image
    image = Image.open("Process.png")

    # Create icon
    icon = Icon("Chatbot", image)

    # Create menu items
    menu_items = [
        MenuItem('Start', lambda icon, item: start_container(icon, item)),
        MenuItem('Stop', lambda icon, item: stop_container(icon, item))
    ]

    # Set menu for icon
    icon.menu = menu_items

    # Run icon in system tray
    icon.run()

if __name__ == "__main__":
    main()
