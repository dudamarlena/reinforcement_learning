""" Main module to run learning choice robot and algorithm """

import config
from training import (
    robot_ddpg,
    robot_dql,
)

if __name__ == "__main__":

    choice_robot = None
    robot_name = input('You can choose two robots: Walker and HalfCheetah. \n')
    while not choice_robot:
        if robot_name == 'Walker':
            choice_robot = config.WALKER

        elif robot_name == 'HalfCheetah':
            choice_robot = config.HALFCHEETAH

        else:
            print('Wrong name of robot. Try one more time.')

    print(f'You chose the robot: {robot_name}\n\n')

    algorithm_name = input('You can choose two algorithms: '
                           '\nDeep Q-Learning(DQL) '
                           '\nor Deep Deterministic Policy Gradient (DDPG). '
                           '\nWrite short name of algorithm: \n')

    print(f'You chose the algorithm: {algorithm_name}\n\n Start learning the robot...')
    if algorithm_name == 'DQL':
        robot_dql.main(choice_robot)

    elif algorithm_name == 'DDPG':
        robot_ddpg.main(choice_robot)
