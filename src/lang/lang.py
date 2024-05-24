"""
main
"""
from lang import logger
from lang.vm.env import ENV
from lang.vm.vm import VM


def execute(filename: str):
    """script"""
    env = ENV()

    idx = env.compile_file(filename)

    logger.debug('=' * 100)

    vm = VM()
    vm.env = env
    vm.idx = idx

    vm.init([])
