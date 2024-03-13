import pygame
import sys
import pandas as pd

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ID Lookup Program")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Font setup
font = pygame.font.Font(None, 36)

# CSV file setup
csv_file = "numbers.csv"
df = pd.read_csv(csv_file)

# Text input class
class TextInputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self):
        width = max(200, font.size(self.text)[0] + 10)
        self.rect.w = width

    def draw(self, surface):
        pygame.draw.rect(surface, blue if self.active else black, self.rect, 2)
        text_surface = font.render(self.text, True, black)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


# Button class
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, black, self.rect)
        pygame.draw.rect(surface, white, self.rect.inflate(-6, -6))
        text_surface = font.render(self.text, True, black)
        surface.blit(text_surface, (self.rect.x + 3, self.rect.y + 3))

    def perform_action(self):
        self.action()


# ID lookup function
def lookup_id():
    try:
        user_id = int(input_box.text)
        if 100000 <= user_id <= 999999:
            result_label.text = f"Checking ID {user_id}..."
            pygame.display.flip()

            # Check if the ID is present in the file
            if user_id in df["ID"].values:
                # Display the corresponding number
                result = df.loc[df["ID"] == user_id, "Number"].values[0]
                result_label.text = f"Result for ID {user_id}: {result}"
                result_label.color = blue
            else:
                result_label.text = f"Number not available for ID {user_id}"
                result_label.color = red
        else:
            result_label.text = "Please enter a 6-digit integer ID."
            result_label.color = black
    except ValueError:
        result_label.text = "Please enter a valid 6-digit integer ID."
        result_label.color = black


# Main game loop
input_box = TextInputBox(width // 2 - 100, height // 2 - 25, 200, 50)
submit_button = Button(width // 2 - 50, height // 2 + 50, 100, 40, "Submit", lookup_id)
result_label = TextInputBox(width // 2 - 100, height // 2 + 120, 200, 50)
result_label.color = black

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input_box.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            submit_button.perform_action()
        result_label.update()

    input_box.update()

    screen.fill(white)
    input_box.draw(screen)
    submit_button.draw(screen)
    result_label.draw(screen)

    pygame.display.flip()
    