import pygame

pygame.init()

window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

white = (255, 255, 255)
blue = (0, 0, 255)

font = pygame.font.Font(None, 36)

rect_width = 100
rect_height = 50
rect_x = (window_size[0] - rect_width) // 2
rect_y = (window_size[1] - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.rect(screen, blue, rectangle)

    text = font.render("Hello, Pygame!", True, blue)
    text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 + 100))
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()