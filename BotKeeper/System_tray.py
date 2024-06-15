from pystray import Icon, Menu, MenuItem
from PIL import Image
import subprocess
import threading

DOCKER_COMPOSE_PATH = "docker-compose.yml"

def start_container(icon, item, app):
    subprocess.Popen(['docker-compose', '-f', DOCKER_COMPOSE_PATH, 'up', '-d'])
    app.start_scheduler()
    icon.update_menu()

def stop_container(icon, item, app):
    subprocess.Popen(['docker-compose', '-f', DOCKER_COMPOSE_PATH, 'down'])
    app.stop_scheduler()
    icon.update_menu()

def main(app):
    image = Image.open("Process.png")

    icon = Icon("Chatbot", image)

    menu = Menu(
        MenuItem('Start', lambda icon, item: start_container(icon, item, app)),
        MenuItem('Stop', lambda icon, item: stop_container(icon, item, app))
    )

    icon.menu = menu

    threading.Thread(target=icon.run).start()

if __name__ == "__main__":
    from app import ChatApplication
    app = ChatApplication()
    main(app)
