__author__ = 'Kalyan'

#fill up this routine to test if the 2 words given are anagrams of each other. 
def are_anagrams(first, second):
    pass


def test_are_anagrams():
    assert True == are_anagrams("Rat", "Tar")
    assert True == are_anagrams("live", "vile")
    assert True == are_anagrams("least", "slate")
    assert False == are_anagrams("big", "small")
    assert False == are_anagrams("big", "gibs")
