import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize("parenthesesstring", [("(()))()))()"),("()())()()))))(())"),("))())()())())())(((())))"),("()(((()))))"),("()())()()))((()))")])
def test_nonmatching_parentheses(parenthesesstring):
    assert not matching_parentheses(parenthesesstring), f" {parenthesesstring} does not match"


@pytest.mark.parametrize("parenthesesstringcorrect", [("((((((()))))))"), ("(((())))"), ("(((((((((((((((((((())))))))))))))))))))")])
def test_matching_parentheses(parenthesesstringcorrect):
    assert matching_parentheses(parenthesesstringcorrect), f" {parenthesesstringcorrect} does match"
