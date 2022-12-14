import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def set_up_fuzzy_tip(section_count: int):
    max_people_count = section_count * 2
    people_count = ctrl.Antecedent(np.arange(0, max_people_count, 1), 'people_count')
    tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

    people_count.automf(3)
    tip.automf(3)

    # fuzzy variables
    people_count['few'] = fuzz.trimf(people_count.universe, [0, 0, 2])
    people_count['fair'] = fuzz.trimf(people_count.universe, [0, 2, max_people_count])
    people_count['lot'] = fuzz.trimf(people_count.universe, [2, max_people_count, max_people_count])

    tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
    tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
    tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

    # fuzzy rules
    rule1 = ctrl.Rule(people_count['lot'], tip['low'])
    rule2 = ctrl.Rule(people_count['fair'], tip['medium'])
    rule3 = ctrl.Rule(people_count['few'], tip['high'])


    tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

    tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

    return tipping

