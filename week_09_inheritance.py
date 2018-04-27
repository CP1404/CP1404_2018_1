from silentmusician import SilentMusician
from musician import Musician
from specialmusician import SpecialMusician


def main():
    m1 = Musician("Miles Davis")
    m2 = SpecialMusician("Lincoln Brewster")

    # Operator overloading:
    result = m1 + m2
    print("==", result)
    print(m1 < m2)
    m3 = SpecialMusician("Joni Mitchell")
    print(m1 == m3)

    # Polymorphism:
    musicians = [m1, m2, Musician("Jay Z"), SilentMusician("John Cage")]
    for i, musician in enumerate(musicians):
        musician.play(i + 1)


main()
