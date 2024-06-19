from game import Game
import json

def main(settings):
    game = Game(settings['WIDTH'], settings['HEIGHT'], settings['FPS'])
    game.run()

if __name__ == '__main__':
    try:
        with open('settings.json', 'r') as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {
            "WIDTH": 960,
            "HEIGHT": 540,
            "FPS": 60
            }
        with open('settings.json', 'w') as file:
            json.dump(settings, file)
    
    main(settings)