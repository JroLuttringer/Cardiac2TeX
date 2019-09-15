import cardiac
import latex_trad
import const
import sys

my_inp = []
my_out = []
for x in range(0,30):
    my_inp.append("---")
    my_out.append("---")
my_inp[0] = "023"
my_inp[1] = "010"

my_mem = []
for x in range(0,100):
    my_mem.append("---")
my_mem[20] = "034"
my_mem[21] = "035"
my_mem[22] = "234"
my_mem[23] = "635"
my_mem[24] = "628"
my_mem[25] = "436"
my_mem[26] = "136"
my_mem[27] = "900"
my_mem[28] = "009"


nb_iteration = 0
cardiac = cardiac.Cardiac(co=20, mem=my_mem, inp=my_inp, out=my_out)
step = 0
beamer = latex_trad.header() + "\n\\begin{document}\n"

while nb_iteration < const.MAX_ITERATIONS and cardiac.end == False:
    beamer += latex_trad.frame(cardiac)
    cardiac.do_step()
    beamer += latex_trad.frame(cardiac)
    cardiac.curr_step = max(1,(cardiac.curr_step + 1)%5)
    nb_iteration += 1

print(beamer+"\n\\end{document}\n")
