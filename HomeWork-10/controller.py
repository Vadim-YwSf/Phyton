# 4.  Controller - модуль. View и Model импортируется только в него
import view
import model


def programm_run():
    view.hello()
    num_1 = model.from_user_data_to_list(view.element_input())
    num_2 = model.from_user_data_to_list(view.element_input())
    operator = view.operator_input()
    result = model.calculate(operator, num_1, num_2)
    view.result_print(num_1, num_2, operator, result)