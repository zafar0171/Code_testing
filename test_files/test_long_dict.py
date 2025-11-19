




def test_long_dic():

    result = {'key': 'value','lastname': 'deza','firstname': 'alfredo'}
    expected = {'key': 'value','lastame':'deza','firstname':'alfredo'}

    assert result == expected