import pytest
from main import check_balance_of_string

@pytest.mark.parametrize('test_input, expected',
                            [
                                ('(((([{}]))))', 'Сбалансированно'),
                                ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
                                ('{{[()]}}', 'Сбалансированно'),
                                ('}{}', 'Несбалансированно'),
                                ('{{[(])]}}', 'Несбалансированно'),
                                ('[[{())}]', 'Несбалансированно')
                            ]
                         )
def test_check_func(test_input, expected):
    assert check_balance_of_string(test_input) == expected