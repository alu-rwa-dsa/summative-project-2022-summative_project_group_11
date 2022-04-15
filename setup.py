from setuptools import setup
from setuptools import find_packages


setup(
    name='radix_sorting_with_deck_of_cards_animation',
    version='1.0.0',
    description='This project contains a radix sorting machine program and a program that sorts a deck of cards using'
                ' the radix sorting machine built in the previous program',
    author='Melissa GIRAMATA, Gabin ISHIMWE, Evelyne UMUBYEYI, Jessie UMUHIRE UMUTESI, and Adrine UWERA',
    author_email='m.giramata@alustudent.com, g.ishimwe@alustudent.com, e.umubyeyi@alustudent.com, '
                 'j.umuhire@alustudent.com, a.uwera@alustudent.com',
    url='https://github.com/alu-rwa-prog-1/assignment_summative_2021-summative_project_group_16',
    install_requires=['tkinter, PIL, Queue'],
    packages=find_packages(),

)
