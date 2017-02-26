#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Table(dict):
    def __getattr__(self, name):
        return self[name] if name in self else None

    def __setattr__(self, name, value):
        if value is None:
            del self[name]
        else:
            self[name] = value

    def __delattr__(self, name):
        del self[name]

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for i, v in enumerate(args):
            self[i] = v
