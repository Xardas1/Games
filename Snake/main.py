import pygame

def init(screen_size):
    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode(screen_size)
    return screen

def check_for_quit(Events):
    for event in Events:
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
    return False

def get_input_events():
    return pygame.event.get()

def main():
    while True:
        init((1280, 720))
        Events = get_input_events()
        check_for_quit(Events)
        if check_for_quit(Events):
            break











if __name__ == "__main__":
    main()