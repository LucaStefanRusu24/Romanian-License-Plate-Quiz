# This is the non-GUI version of the game I made before adding a GUI using Pygame.

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

def game(rand, counties):
    i = 0

    for county in counties:
        i += 1
        if i == rand:
            answer = input(county + ': ')
            break

    if answer == counties[county]:
        return 1
    else:
        return 0



def main():
    play = input("Lets Play the Romanian Counties Quiz. Type Start to start: ")
    score = 0
    questions = 0

    while play == 'Start':
        rand = random.randint(1, 43)
        if game(rand, counties) == 1:
            score += 1
            questions += 1
            print("Correct!")
        else:
            questions += 1
            print("False!")

        play = input("want to continue playing? ")
        if play == 'yes' or play == 'Yes':
            play = 'Start'

    print("Score: " + str(score) + "/" + str(questions))

main()
