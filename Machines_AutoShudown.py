
"""
1. collect what machines to power off
2. state - on or off
3. result status of machines
4. execute action
"""
from time import sleep


ATTEMPTS =5

def _dummy_all_shutdown(machine):
    """
    This is dummy for AWS api to shutdown machine
    :param machine,: this is the lsit of the machines to shuwdown
    :return: State
    """
    print(f"shutting down machines {machine}")

def _dummy_shutdown(machine, wait_for_completion=True, attempts=5):
    """
    This is dummy for AWS api to shutdown machine
    :param machine,: this is the lsit of the machines to shuwdown
    :return: State
    """
    print(f"shutting down machines {machine}")
    if wait_for_completion:
        while _dummy_state(machine) and ATTEMPTS > 0:
            sleep(10)
            attempts -= 1
        raise RuntimeError("The machine was not turned off")
    return True

def _dummy_state(machine):
    """
    This is dummy for AWS api to shutdown machine
    :param machine,: this is the list of the machines to shutdown
    :return: State
    """
    print(f"state of the machines {machine} is true")
    return True

def auto_shutdown(machines_to_shutdown, attempts=5):
    """
    Start the entire shutdown process
    :return:
    """

    for machine in machines_to_shutdown:
        _dummy_all_shutdown(machine)
    for machine in machines_to_shutdown:
        if _dummy_state(machine):
            _dummy_shutdown(machine, wait_for_completion=True, attempts=attempts)

    for machine in machines_to_shutdown:
        if not _dummy_state(machine):
            print(f"the following machine failed to shutdown... {machine}")