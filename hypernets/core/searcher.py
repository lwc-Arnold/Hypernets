# -*- coding:utf-8 -*-
"""

"""
from .stateful import Stateful
import enum


class OptimizeDirection(enum.Enum):
    Minimize = 'minimize'
    Maximize = 'maximize'


class Searcher(Stateful):
    def __init__(self, space_fn, optimize_direction=OptimizeDirection.Minimize):
        self.space_fn = space_fn
        self.optimize_direction = optimize_direction

    def sample(self):
        raise NotImplementedError

    def get_best(self):
        raise NotImplementedError

    def update_result(self, space_id, params, result):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def export(self):
        raise NotImplementedError
