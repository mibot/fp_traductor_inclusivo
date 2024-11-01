from inclusive import traductor_inclusivo

def test_traductor_inclusivo():

    assert traductor_inclusivo("todos somos programadores") == "todes somes programadores"

    assert traductor_inclusivo("las programadoras expertas") == "les programadores expertes"

    assert traductor_inclusivo("el arte es genial") == "el arte es genial"

    assert traductor_inclusivo("la el lo") == "le el le"

    assert traductor_inclusivo("") == ""

    assert traductor_inclusivo("todos  somos   alumnos") == "todes somes alumnes"

    assert traductor_inclusivo("todos. algunas, varios!") == "todes. algunes, varies!"

    assert traductor_inclusivo("el profesor es bueno") == "el profesor es buene"

    assert traductor_inclusivo("a o e i u") == "e e e i u"

    print("Todas las pruebas pasaron exitosamente.")

if __name__ == "__main__":
    test_traductor_inclusivo()