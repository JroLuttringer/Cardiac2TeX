import const

class Cardiac:
    def __init__(self,co=0, mem=[], inp=[], out=[]):
        """
        initialiser le compteur ordinal, la mémoire, l'input et l'ouput
        aux valeurs demandées
        """
        self.co = co #compteur ordinal
        self.curr_step = 1
        self.mem = mem #memoire
        self.input = inp #input
        self.output = out #output
        self.ri = "" #registre instruction
        self.end = False #fin à ce cycle ?
        self.inst = "" #instruction traduite
        self.curr_input = 0 #current input
        self.curr_output = 0 #current output
        self.acc = "0000" #acc
        self.acc_bool = True #is acc at 0000 ?

    def do_step(self):
        if self.curr_step == 1:
            self.load()
        if self.curr_step == 2:
            self.inc_co()
        if self.curr_step == 3:
            self.trad()
        if self.curr_step == 4:
            self.execute()



    def load(self):
        """
        charger dans le RI le contenu de la cellule mémoire
        pointée par le CO
        """
        self.ri = self.mem[int(self.co) ]
        if self.ri[0] == '9':
            self.end = True


    def inc_co(self):
        """
        incrémenter le compteur ordinal
        """
        self.co = str(int(self.co) + 1)

    def trad(self):
        opcode = self.ri[0]
        value = self.ri[1:]
        #inst_name = const.opcode_to_name[opcode]
        #inst_desc = const.opcode_to_desc[opcode]
        inst_trad = const.opcode_to_trad[opcode]
        self.inst = inst_trad.replace("$VALUE$", value) + '\n'
        self.inst = self.inst

    def execute(self):
        value = int(self.ri[1:])
        opcode = self.ri[0]
        if opcode == "0":
            self.mem[value] = self.input[self.curr_input]
            self.curr_input += 1

        elif opcode == "1":
            self.output[self.curr_output] = self.mem[value]
            self.curr_output += 1
        elif opcode == "2":
            self.acc = self.mem[value]
        elif opcode == "3":
            self.acc = self.mem[self.mem[value]]
        elif opcode == "4":
            to_mem = self.acc
            if int(to_mem) >= 1000:
                to_mem = to_mem[1:]
            self.mem[value] = to_mem
        elif opcode == "5":
            to_mem = self.acc
            if int(to_mem) >= 1000:
                to_mem = to_mem[1:]
            self.mem[self.mem[value]] = to_mem
        elif opcode == "6":
            self.acc = str(int(self.mem[value]) + int(self.acc))
            if int(self.acc) > 1000:
                self.acc = self.acc[1:]
        elif opcode == "7":
            self.acc = str(int(self.mem[value]) - int(self.acc))
            if int(self.acc) < 0:
                self.acc = "0000"
        elif opcode == "8":
            old_co = self.co
            self.co = value
            self.mem[99] = old.co
        elif opcode == "9":
            self.end = True

        if self.acc == "0000":
            self.acc_bool = True
        else:
            self.acc_bool = False
