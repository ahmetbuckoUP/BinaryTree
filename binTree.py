class nyja:
    def __init__(self, data):
        self.data = data
        self.majt = None
        self.djathte = None


class BinaryTree:
    def __init__(self):
        self.rrenja = None


    def gjejLartesine(self, temp):
        if (self.rrenja == None):
            print("Pema eshte e shprazet")
            return 0
        else:
            majtLartesi = 0
            djathteLartesi = 0

            # gjen lartesine e subtreete majte
            if (temp.majt != None):
                majtLartesi = self.gjejLartesine(temp.majt)

                # gjen lartesine e subtreetedjathte
            if (temp.djathte != None):
                djathteLartesi = self.gjejLartesine(temp.djathte)

            if (majtLartesi > djathteLartesi):
                max = majtLartesi
            else:
                max = djathteLartesi

            return (max + 1)


bTree = BinaryTree()
bTree.rrenja = nyja(1)
bTree.rrenja.majt = nyja(2)
bTree.rrenja.djathte = nyja(3)
bTree.rrenja.majt.majt = nyja(4)
bTree.rrenja.djathte.majt = nyja(5)
bTree.rrenja.djathte.djathte = nyja(6)
bTree.rrenja.djathte.djathte.djathte = nyja(7)
bTree.rrenja.djathte.djathte.djathte.djathte = nyja(8)

print(str(bTree.rrenja))

# Display the maximum Lartesi of the given binary tree
print("Lartesia Maksimale: " + str(bTree.gjejLartesine(bTree.rrenja)))