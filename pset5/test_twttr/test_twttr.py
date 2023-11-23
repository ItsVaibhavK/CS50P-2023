from twttr import shorten


# EUNOIA is the shortest word in English which has all five vowels.
# sphynx to test for consonants only
def test_shorten_lowercase():
    assert shorten("eunoia") == "n"
    assert shorten("sphynx") == "sphynx"


def test_shorten_uppercase():
    assert shorten("EUNOIA") == "N"
    assert shorten("SPHYNX") == "SPHYNX"


def test_shorten_num_punct():
    assert shorten("33") == "33"
    assert shorten("!?") == "!?"


if __name__ == "__main__":
    main()