class Blockworld:
    def __init__(self, blocks):
        self.state = {}
        for block in blocks:
            self.state[block] = None

    def stack(self, block1, block2):
        if self.state[block1] is None and self.state[block2] is None:
            self.state[block1] = block2
            print("Stacked", block1, "on", block2)
        else:
            print("Cannot stack", block1, "on", block2)

    def unstack(self, block1):
        if self.state[block1] is not None:
            block2 = self.state[block1]
            self.state[block1] = None
            print("Unstacked", block1, "from", block2)
        else:
            print(block1, "is not stacked on anything")

    def show_state(self):
        print("Current Blockworld State:")
        for block, on in self.state.items():
            print(block, "is on", on if on else "nothing")

bw = Blockworld(['A', 'B', 'C'])
bw.show_state()

bw.stack('A', 'B')
bw.stack('C', 'A')
bw.show_state()

bw.unstack('A')
bw.show_state()
