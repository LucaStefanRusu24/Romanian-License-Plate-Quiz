import pygame
import random

counties = {
    'AB': 'Alba',
    'AG': 'Arges',
    'AR': 'Arad',
    'B': 'Bucuresti',
    'BC': 'Bacau',
    'BH': 'Bihor',
    'BN': 'Bistrita',
    'BR': 'Braila',
    'BT': 'Botosani',
    'BV': 'Brasov',
    'BZ': 'Buzau',
    'CJ': 'Cluj',
    'CL': 'Calaras',
    'CS': 'Caras-Severin',
    'CT': 'Constanta',
    'CV': 'Covasna',
    'DB': 'Dambovita',
    'DJ': 'Dolj',
    'GJ': 'Gorj',
    'GL': 'Galati',
    'GR': 'Giurgiu',
    'HD': 'Hunedoara',
    'HR': 'Harghita',
    'IF': 'Ilfov',
    'IL': 'Ialomita',
    'IS': 'Iasi',
    'MH': 'Mehedinti',
    'MM': 'Maramures',
    'MS': 'Mures',
    'NT': 'Neamt',
    'OT': 'Olt',
    'PH': 'Prahova',
    'SB': 'Sibiu',
    'SJ': 'Salaj',
    'SM': 'Satu Mare',
    'SV': 'Suceava',
    'TL': 'Tulcea',
    'TM': 'Timis',
    'TR': 'Teleorman',
    'VL': 'Valcea',
    'VN': 'Vrancea',
    'VS': 'Vaslui'
}

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Romanina Counties Quiz")

BACKGROUND = (30, 19, 128)

FPS = 60

BACKGROUND_IMAGE = pygame.image.load(
    '/Users/vladrusu/PycharmProjects/RomaniaCountiesQuiz/1200px-Flag_map_of_Romania.svg.png')
MAP_OF_ROMANIA = pygame.transform.scale(BACKGROUND_IMAGE, (700, 400))

input_font = pygame.font.SysFont(None, 30)
COLOR_INACTIVE = pygame.Color('black')
COLOR_ACTIVE = pygame.Color('black')
COLOR_FILL = pygame.Color('white')


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = input_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = input_font.render(self.text, True, self.color)

    def get_text(self):
        return self.text

    def clear_box(self):
        self.text = ''

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


input_box = InputBox(360, 320, 140, 32)


def random_county(rand, counties):
    i = 0
    for county in counties:
        i += 1
        if i == rand:
            return county


rand = random.randint(1, 43)
county = random_county(rand, counties)
score = 0

def draw_window():
    WIN.fill(BACKGROUND)
    WIN.blit(MAP_OF_ROMANIA, (110, 60))
    question_font = pygame.font.SysFont(None, 50)
    question_label = question_font.render(f"What county is {county}", 1, (0, 0, 0))
    WIN.blit(question_label, (WIDTH / 2 - question_label.get_width() / 2, 25))
    score_font = pygame.font.SysFont(None, 50)
    score_label = score_font.render(f"Score: {score}", 1, (0, 128, 0))
    WIN.blit(score_label, (10, 10))
    input_box.update()
    input_box.draw(WIN)
    pygame.display.flip()
    pygame.display.update()


def main():
    global county, score
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            input_box.handle_event(event)
            answer = input_box.get_text()
            if counties[county] == 'Teleorman' and answer == 'Liviu Dragnea PSD':
                score += 50
                randi = random.randint(1, 43)
                county = random_county(randi, counties)
                input_box.clear_box()
            if answer == counties[county]:
                score += 1
                randi = random.randint(1, 43)
                county = random_county(randi, counties)
                input_box.clear_box()
        draw_window()
    pygame.quit()


def main_menu():
    title_font = pygame.font.SysFont(None, 70)
    run = True
    while run:
        WIN.fill(BACKGROUND)
        title_label = title_font.render("Press the mouse to begin", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()


if __name__ == "__main__":
    main_menu()
