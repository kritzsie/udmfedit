#!/usr/bin/env python3

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

class Vertex(Table):
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y

class Sector(Table):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Sidedef(Table):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Linedef(Table):
    def __init__(self, v1, v2, sidefront, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v1 = v1
        self.v2 = v2
        self.sidefront = sidefront

class Thing(Vertex):
    def __init__(self, type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = type

class Map(Table):
    def __init__(self, namespace = "ZDoom", template = False):
        self.namespace = namespace
        self.vertices = [
            Vertex(-1, -1),
            Vertex(1, -1),
            Vertex(1, 1),
            Vertex(-1, 1)
        ] if template else []
        self.sectors = [
            Sector("FLOOR4_8", "CEIL3_5", heightfloor = 0, heightceiling = 128, lightlevel = 128)
        ] if template else []
        self.sidedefs = [
            Sidedef(0, texturemiddle = "STARTAN3"),
            Sidedef(0, texturemiddle = "STARTAN3"),
            Sidedef(0, texturemiddle = "STARTAN3"),
            Sidedef(0, texturemiddle = "STARTAN3")
        ] if template else []
        self.linedefs = [
            Linedef(0, 1, 0),
            Linedef(1, 2, 1),
            Linedef(2, 3, 2),
            Linedef(3, 0, 3)
        ] if template else []
        self.things = [
            Thing(0, 0, 1)
        ] if template else []
