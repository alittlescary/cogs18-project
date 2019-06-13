from functions import *
    
def test_villain_counter():
    test = VillainQuiz()
    test.villain_counter("jafar")
    assert test.counter_jafar == 1
    

def test_result():
    test = VillainQuiz()
    test.counter_jafar = 3
    test.counter_ursula = 2
    test.counter_scar = 1
    test.counter_gaston = 0
    test.result()
    assert test.villain == "jafar"
    