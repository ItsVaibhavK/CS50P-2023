from um import count

def test_zero_matches():
    assert count("hello, how are you?") == 0
    assert count("My phone number is +91-12345678") == 0
    assert count("?!#$what$^*&$()") == 0


def test_single_match():
    assert count("Um, what's that?") == 1
    assert count("I hear someone saying 'um'") == 1
    assert count("Thanks, um, for dinner.") == 1


def test_multiple_matches():
    assert count("Um, thanks, um... for the album.") == 2
    assert count("Hey, um, what's it like... um... to be a programmer?") == 2
    assert count("Um, um, um, um.") == 4


if __name__ == "__main__":
    main()