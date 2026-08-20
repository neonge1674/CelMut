class Tower:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def __str__(self):
        toString = ""
        for i in range(len(self.dimensions)):
            toString = toString + f"{self.dimensions[i]}"
            if i != len(self.dimensions) - 1:
                toString = toString + "\n"
        return toString

    def reverse(self):
        toReturn = Tower([])
        for i in range(len(self.dimensions)):
            toReturn.dimensions.append(self.dimensions[i].reverse())
        return toReturn

class Cell:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __str__(self):
        return f"[{self.head}, {self.tail}]"

    def reverse(self, doIt = True):
        if doIt:
            return Cell(self.tail, self.head)
        else:
            return Cell(self.head, self.tail)


def constructTower(material, dimensions):
    if type (material) == Cell:
        tempArr = []

        for i in range(dimensions[0]):
            material = Cell(material, material)

        for i in range(dimensions[1]):
            tempArr.append(material)

        return Tower(tempArr)

def add(mutated, mutator):
    if type(mutated) == int and type(mutator) == int:
        return mutated + mutator
    elif type(mutated) == Cell and type(mutator) == Cell:
        return Cell(add(mutated.head, mutator.tail), actSub(mutator.head, mutated.tail))
    elif type(mutated) == Cell and type(mutator) == int:
        return add(mutated, Cell(mutator, mutator))
    elif type(mutated) == int and type(mutator) == Cell:
        return add(Cell(mutated, mutated), mutator)
    elif type(mutated) == Tower:
        if type(mutator) == Tower:
            temp = []
            for i in range(mutated.dimensions.len()):
                temp.append(add(mutated.dimensions[i], mutator.dimensions[i]))
            return Tower(temp)
        else:
            temp = []
            for i in mutated:
                temp.append(add(i, mutator))
            return Tower(temp)


def actSub(mutated, mutator):
    if type(mutated) == int and type(mutator) == int:
        return mutated - mutator
    elif type(mutated) == Cell and type(mutator) == Cell:
        return Cell(actSub(mutated.head, mutator.tail), pasSub(mutator.head, mutated.tail))
    elif type(mutated) == Cell and type(mutator) == int:
        return actSub(mutated, Cell(mutator, mutator))
    elif type(mutated) == int and type(mutator) == Cell:
        return actSub(Cell(mutated, mutated), mutator)
    elif type(mutated) == Tower:
        if type(mutator) == Tower:
            temp = []
            for i in range(mutated.dimensions.len()):
                temp.append(actSub(mutated.dimensions[i], mutator.dimensions[i]))
            return Tower(temp)
        else:
            temp = []
            for i in mutated:
                temp.append(actSub(i, mutator))
            return Tower(temp)

def pasSub(mutated, mutator):
    if type(mutated) == int and type(mutator) == int:
        return mutated - mutator
    elif type(mutated) == Cell and type(mutator) == Cell:
        return Cell(add(mutated.tail, mutator.tail), pasSub(mutated.head, mutator.head))
    elif type(mutated) == Cell and type(mutator) == int:
        return pasSub(mutated, Cell(mutator, mutator))
    elif type(mutated) == int and type(mutator) == Cell:
        return pasSub(Cell(mutated, mutated), mutator)
    elif type(mutated) == Tower:
        if type(mutator) == Tower:
            temp = []
            for i in range(mutated.dimensions.len()):
                temp.append(pasSub(mutated.dimensions[i], mutator.dimensions[i]))
            return Tower(temp)
        else:
            temp = []
            for i in mutated:
                temp.append(pasSub(i, mutator))
            return Tower(temp)

def mult(mutated, mutator):
    if type(mutated) == Cell and type(mutator) == int:
        if mutator == 0:
            return None
        if mutator < 0:
            reverseThis = True
            mutator = abs(mutator)
        else:
            reverseThis = False
        OG_mutated = mutated
        for i in range(mutator):
            mutated = add(mutated, OG_mutated)
        return mutated.reverse(reverseThis)
    elif type(mutated) == Cell and type(mutator) == Cell:
        return Cell(mult(mutated, mutator.head), mult(mutator, mutated.tail))
    elif type(mutated) == int and (type(mutator) == Cell or type(mutator) == int):
        return mult(Cell(mutated, mutated), mutator)
    elif type(mutated) == Tower:
        if type(mutator) == Tower:
            temp = []
            for i in range(mutated.dimensions.len()):
                temp.append(mult(mutated.dimensions[i], mutator.dimensions[i]))
            return Tower(temp)
        else:
            temp = []
            for i in mutated:
                temp.append(mult(i, mutator))
            return Tower(temp)

def actDiv(mutated, mutator):
    if type(mutated) == Cell and type(mutator) == int:
        if mutator < 0:
            mutated = mutated.reverse()
            mutator = abs(mutator)

        if mutator % 2 == 0:
            return Cell(mutated.head - (mutated.tail * mutator), mutated.tail)
        elif mutator % 2 == 1:
            OG_tail = round((mutated.head - mutated.tail) / (mutator + 1))
            return Cell(mutated.head - (OG_tail *  mutator), OG_tail)
    elif type(mutated) == Cell and type(mutator) == Cell:
        if type(mutated.head) == Cell :
            return actDiv(mutated.head, mutator.head)
        elif type(mutated.head) == int :
            return actDiv(Cell(mutated.head, mutated.head), mutator.head)
    elif type(mutated) == int and (type(mutator) == Cell or type(mutator) == int):
        return actDiv(Cell(mutated, mutated), mutator)
    elif type(mutated) == Tower:
        if type(mutator) == Tower:
            temp = []
            for i in range(mutated.dimensions.len()):
                temp.append(actDiv(mutated.dimensions[i], mutator.dimensions[i]))
            return Tower(temp)
        else:
            temp = []
            for i in mutated:
                temp.append(actDiv(i, mutator))
            return Tower(temp)

def pasDiv(mutated, mutator):
    if type(mutated) == Cell and type(mutator) == Cell:
        if type(mutated.head) == Cell :
            return actDiv(mutated.tail, mutator.tail)
        elif type(mutated.head) == int :
            return actDiv(Cell(mutated.tail, mutated.tail), mutator.tail)
    elif type(mutated) == Cell and type(mutator) == int:
        return pasDiv(mutated, Cell(mutator, mutator))
    elif type(mutated) == int and type(mutator) == Cell:
        return pasDiv(Cell(mutated, mutated), mutator)
    elif type(mutated) == int and type(mutator) == int:
        return pasDiv(Cell(mutated, mutated), Cell(mutator, mutator))
    elif type(mutated) == Tower:
        if type(mutator) == Tower:
            temp = []
            for i in range(mutated.dimensions.len()):
                temp.append(pasDiv(mutated.dimensions[i], mutator.dimensions[i]))
            return Tower(temp)
        else:
            temp = []
            for i in mutated:
                temp.append(pasDiv(i, mutator))
            return Tower(temp)

def exp(mutated, mutator):
    if type(mutated) == Cell and type(mutator) == Cell:
        return Cell(Tower([mult(mutated, mutator), mult(mutator, mutated)]),
                    Tower([mult(mutated.reverse(), mutator.reverse()), mult(mutator.reverse(), mutated.reverse())]))
    elif type(mutated) == Cell and type(mutator) == int:
        return Cell(Tower([mult(mutated, mutator), mult(mutator, mutated)]),
                    Tower([mult(mutated.reverse(), mutator), mult(mutator, mutated.reverse())]))
    elif type(mutated) == int and type(mutator) == Cell:
        return exp(Cell(mutated, mutated), mutator)
    elif type(mutated) == int and type(mutator) == int:
        exp(Cell(mutated, mutated), Cell(mutator, mutator))

def root(mutated, mutator):
    if type(mutated) == Cell and (type(mutator) == Cell or type(mutator) == int):
        if type(mutated.head) == Tower:
            return actDiv(mutated.head[0], mutator)
        elif type(mutated.head) == Cell:
            return actDiv(mutated, mutator)
    elif type(mutated) == int and (type(mutator) == Cell or type(mutator) == int):
        print("bubble")
        return root(Cell(constructTower(mutated, [mutated, mutated]), constructTower(mutated, [mutated, mutated])), mutator)

def log(mutated, mutator):
    if type(mutated) == Cell and (type(mutator) == Cell or type(mutator) == int):
        if type(mutated.head) == Tower:
            return actDiv(mutated.head[1], mutator)
        elif type(mutated.head) == Cell:
            return pasDiv(mutated, mutator)
    elif type(mutated) == int and (type(mutator) == Cell or type(mutator) == int):
        return log(constructTower(mutated, [mutated, mutated]), mutator)

