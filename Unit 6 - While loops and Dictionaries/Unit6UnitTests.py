def item_frequency_unit_test(item_frequency):
    '''
    Test suite for testing item frequency function
    '''
    print("Testing sorted tuples")
    test_cases = [['hi', 'my', 'name', 'kanye', 'and', 'i', 'love', 'kanye',
                   'and', 'if', 'my', 'name', 'wasnt', 'kanye', 'then', 'i',
                   'would', 'change', 'it', 'to', 'kanye']]
    solutions = [[('kanye', 4), ('name', 2), ('my', 2), ('i', 2), ('and', 2),
                  ('would', 1), ('wasnt', 1), ('to', 1), ('then', 1),
                  ('love', 1), ('it', 1), ('if', 1), ('hi', 1), ('change', 1)]]
    for i, case in enumerate(test_cases):
        try:
            assert item_frequency(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: item_frequency({case})!={solutions[i]}")

            
def item_frequency_counter_unit_test(item_frequency_counter):
    '''
    Test suite for testing item_frequency_counter function
    '''
    print("Testing sorted tuples")
    test_cases = [['hi', 'my', 'name', 'kanye', 'and', 'i', 'love', 'kanye',
                   'and', 'if', 'my', 'name', 'wasnt', 'kanye', 'then', 'i',
                   'would', 'change', 'it', 'to', 'kanye']]
    solutions = [[('kanye', 4), ('my', 2), ('name', 2), ('and', 2), ('i', 2), ('hi', 1),
 ('love', 1), ('if', 1), ('wasnt', 1), ('then', 1), ('would', 1), ('change', 1), ('it', 1), ('to', 1)]]
    for i, case in enumerate(test_cases):
        try:
            assert item_frequency_counter(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: item_frequency_counter({case})!={solutions[i]}")

            
def word_frequency_unit_test(word_frequency):
    '''
    Test suite for testing word_frequency function
    '''
    print("Testing sorted tuples")
    test_cases = ['my name is lauren lauren lauren my']
    solutions = [[('lauren', 3), ('my', 2), ('name', 1), ('is', 1)]]
    for i, case in enumerate(test_cases):
        try:
            assert word_frequency(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: word_frequency({case})!={solutions[i]}")

            
def letter_frequency_unit_test(letter_frequency):
    '''
    Test suite for testing letter_frequency function
    '''
    print("Testing sorted tuples")
    test_cases = ['my name is lauren lauren lauren my']
    solutions = [[(' ', 6), ('n', 4), ('e', 4), ('a', 4), ('u', 3), ('r', 3), ('m', 3), ('l', 3), ('y', 2), ('s', 1), ('i', 1)]]
    for i, case in enumerate(test_cases):
        try:
            assert letter_frequency(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: letter_frequency({case})!={solutions[i]}")
            
            
def ith_word_unit_test(ith_word):
    '''
    Test suite for testing ith_word function
    '''
    print("Testing ith word")
    test_cases = [10]
    solutions = ['aardvark']
    for i, case in enumerate(test_cases):
        try:
            assert ith_word(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: ith_word({case})!={solutions[i]}")
            
            
def ith_to_last_unit_test(ith_to_last):
    '''
    Test suite for testing ith_to_last function
    '''
    print("Testing ith word")
    test_cases = [5]
    solutions = ['zythums']
    for i, case in enumerate(test_cases):
        try:
            assert ith_to_last(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: ith_to_last({case})!={solutions[i]}")
            
def word_to_index_unit_test(word_to_index):
    '''
    Test suite for testing word_to_index function
    '''
    print("Testing word_to_index")
    test_cases = ['zymurgies', 'p2p']
    solutions = [267743, -1]
    for i, case in enumerate(test_cases):
        try:
            assert word_to_index(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: word_to_index({case})!={solutions[i]}")
            
def dollar_value_unit_test(dollar_value):
    '''
    Test suite for testing dollar_value function
    '''
    print("Testing dollar_value")
    test_cases = ['poo', 'breatharian']
    solutions = [35, 200]
    for i, case in enumerate(test_cases):
        try:
            assert dollar_value(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: dollar_value({case})!={solutions[i]}")

def find_max_unit_test(find_max):
    '''
    Test suite for testing find_max function
    '''
    print("Testing find_max")
    try:
        assert find_max() == (295, 'bacchanalianism')
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: find_max()!=295, bacchanalianism")
        
        
        
def word_dictionary_unit_test(word_dictionary):
    '''
    Test suite for testing dollar_value function
    '''
    print("Testing word_dictionary")
    try:
        assert len(word_dictionary()) == 282
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: len(word_dictionary())!= 282 ")
    try:
        assert word_dictionary()[295] == ['bacchanalianism']
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: word_dictionary()[295] != ['bacchanalianism']")
    try:
        assert word_dictionary()[14] == ['oy', 'swy', 'us', 'yo']
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: word_dictionary()[14] != ['oy', 'swy', 'us', 'yo']")
        
        
def n_smallest_unit_test(n_smallest):
    '''
    Test suite for testing n_smallest function
    '''
    print("Testing n_smallest")
    try:
        assert n_smallest(10) == [(3, ['zzz']), (8, ['yu', 'zuz']), (9, ['xu']), (11, ['zzzs']), (13, ['ut', 'zo']), (14, ['oy', 'swy', 'us', 'yo']), (15, ['ny', 'ox', 'st', 'tuzz', 'ur', 'wry', 'yuzu']), (16, ['my', 'ow', 'pyx', 'tux', 'wo', 'yus', 'yutz']), (17, ['oxy', 'sty', 'up']), (18, ['ky', 'ou', 'try', 'wus', 'yow'])]
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: n_smallest()!=[(3, ['zzz']), (8, ['yu', 'zuz'])...(18, ['ky', 'ou', 'try', 'wus', 'yow'])]")
        
def n_largest_unit_test(n_largest):
    '''
    Test suite for testing n_largest function
    '''
    print("Testing n_largest")
    try:
        assert n_largest(10) == [(295, ['bacchanalianism']),
 (293, ['deacidification']),
 (292, ['brachiocephalic', 'mechanochemical']),
 (291, ['decalcification']),
 (288, ['chalcographical', 'damageabilities']),
 (286, ['dieffenbachias']),
 (285, ['acknowledgeable', 'thalamencephala']),
 (283, ['acanthocephalan', 'archaebacteria', 'unchallengeable']),
 (282,
  ['clearheadedness',
   'democratifiable',
   'disaccharidases',
   'dolichocephalic',
   'haemoflagellate',
   'hendecasyllabic',
   'lackadaisically']),
 (281, ['bibliographical', 'changeabilities', 'interchangeable'])]
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: n_largest!=[(295, ['bacchanalianism'])... (281, ['bibliographical', 'changeabilities', 'interchangeable'])]")
        
def max_words_unit_test(max_words):
    '''
    Test suite for testing max_words function
    '''
    print("Testing max_words")
    try:
        assert max_words() == (129, 2542)
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: max_words!=(129, 2542)")
        
def is_prime_unit_test(is_prime):
    '''
    Test suite for testingis_prime function
    '''
    print("Testing is_prime")
    test_cases = [6,7,2,-5,5.5 ]
    solutions = [False, True, True, False, False]
    for i, case in enumerate(test_cases):
        try:
            assert is_prime(case) == solutions[i]
            print(f"Passed")
        except AssertionError:
            print(f"FAILED: is_prime({case})!={solutions[i]}")
            
            
def min_prime_unit_test(min_prime):
    '''
    Test suite for testing min_prime function
    '''
    print("Testing min_prime")
    try:
        assert min_prime(175,275) == (269, ['affordabilities',
          'antifashionable',
          'archaeobotanies',
          'carpetbaggeries',
          'circumjacencies',
          'diamagnetically',
          'disacknowledged',
          'discapacitating',
          'encephalopathic',
          'hepaticological',
          'macrencephalia',
          'redeemabilities'])
        print(f"Passed")
    except AssertionError:
        print(f"FAILED: min_prime!=(269, ['affordabilities','antifashionable','archaeobotanies','carpetbaggeries', 'circumjacencies','diamagnetically','disacknowledged','discapacitating','encephalopathic', 'hepaticological','macrencephalia','redeemabilities'])")
