import pygame
from firebase_admin import credentials, firestore, initialize_app

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Firebase Pygame Example")

# Initialize Firebase
cred = credentials.Certificate("key/diabetes-f2cdc-firebase-adminsdk-tgd8n-6e46735b22.json")
initialize_app(cred)
db = firestore.client()

# Font setup
font = pygame.font.Font(None, 36)

# Text input class
class TextInputBox:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.label = label

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
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
        text_surface = font.render(self.text, True, (0, 0, 0))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        label_surface = font.render(self.label, True, (0, 0, 0))
        surface.blit(label_surface, (self.rect.x, self.rect.y - 30))


# Button class
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect.inflate(-6, -6))
        text_surface = font.render(self.text, True, (0, 0, 0))
        surface.blit(text_surface, (self.rect.x + 3, self.rect.y + 3))

    def perform_action(self):
        return self.action()


# Function to save data to Firebase
def save_to_firebase(user_id, name, age):
    user_data = {
        "id": user_id,
        "name": name,
        "age": age
    }
    try:
        db.collection("users").add(user_data)
        print("Data saved to Firebase!")
        return True
    except Exception as e:
        print("Error saving data to Firebase:", e)
        return False

# Main game loop
id_input = TextInputBox(width // 2 - 100, height // 2 - 50, 200, 30, "Enter 6-digit ID:")
name_input = TextInputBox(width // 2 - 100, height // 2 + 20, 200, 30, "Enter Name:")
age_input = TextInputBox(width // 2 - 100, height // 2 + 90, 200, 30, "Enter Age:")
save_button = Button(width // 2 - 50, height // 2 + 160, 100, 40, "Save to Firebase", lambda: save_to_firebase(id_input.text, name_input.text, age_input.text))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        id_input.handle_event(event)
        name_input.handle_event(event)
        age_input.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if id_input.active or name_input.active or age_input.active:
                # If any input box is active, don't perform button action
                continue
            if save_button.perform_action():
                running = False  # Exit the loop if data is saved

    id_input.update()
    name_input.update()
    age_input.update()

    screen.fill((255, 255, 255))
    id_input.draw(screen)
    name_input.draw(screen)
    age_input.draw(screen)
    save_button.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
