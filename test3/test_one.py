import pytest
import random

@pytest.mark.flaky(reruns=3)
def test_flaky():
    assert random.chioce([True,False])

@pytest.mark.flaky_two(reruns=3,reruns_delay =2)
def test_flaky():
    assert random.chioce([True,False])



# fail screenshot 
#pytest -lf (runs only for  falied testcase)
#pyest --reruns 3 --lf # Reruns only for failed testcase , upto 3 times



#flaky testcases ??
#element 
# element --- visible , {force:true}  -----> wait 


# application  -----< user action -----> request ------ response ------ element 
# cypress ----- element (element creater X --- reponse -----> elelement)
# cypress ----- element (element creater X --- reponse -----> element {cy.wait(1000)})
# certain scenario -- admin element , user not visble ??
# element is visible and element exist ??
# element -- not exist ----> testcase ? ----- skip ?