
def header():
    str = ""
    str += "\\documentclass[8pt]{beamer}\n"
    str += "\\usepackage{tikz}\n"
    str += "\\usepackage{varwidth}\n"
    str += "\\usepackage[utf8]{inputenc}\n"
    str += "\\mode<presentation>{\n"
    str += "	\\usefonttheme{professionalfonts} % normal font for math formulas\n"
    str += "	\\AtBeginSection[]{\n"
    str += "	\\begin{frame}%[noframenumbering] % remove this if you do not want to number section page\n"
    str += "	\\vfill\n"
    str += "	\centering\n"
    str += "	\\begin{beamercolorbox}[sep=8pt,center,shadow=true,rounded=true]{title}\n"
    str += "	\\usebeamerfont{title}\insertsectionhead\par%\n"
    str += "	\\end{beamercolorbox}\n"
    str += "	\\vfill\n"
    str += "	\\end{frame}}}\n"
    str += "\\usepackage{amsmath}\n"
    str += "\\usepackage{amsfonts}\n"
    str += "\\usepackage{amssymb}\n"
    str += "\\usepackage{multirow}% for the \multirow command\n"
    str += "\\usepackage{rotating}% for the sideways environment\n"
    str += "\\newcommand\\nvl[1]{\multicolumn{1}{c}{#1}}\n"
    str += "\\newcommand\\redhead[1]{\nvl{\color{red}#1}}\n"
    str += "\\newcommand\ma[1]{\nvl{\scriptsize#1}}\n"
    str += "% \\tikznode[options]{label}{contents}\n"
    str += "\\newcommand\\tikznode[3][]%\n"
    str += "   {\\tikz[remember picture,baseline=(#2.base)]\n"
    str += "      \\node[minimum size=0pt,inner sep=0pt,#1](#2){#3};%\n"
    str += "   }\n"
    str += "\\setbeamertemplate{theorems}[numbered] % numbering theorem environment\n"
    str += "\\theoremstyle{plain} % other style are definition and example, you can also define your own \n"
    str += "\\usepackage[bibstyle=authoryear, citestyle=authoryear, maxcitenames=2, maxbibnames=100, backend=bibtex]{biblatex}\n"
    return str





def frame(cardiac):
    frame = "\\begin{frame}{}\n"
    frame += diagram(cardiac)
    frame += str_input_output_mem(cardiac)
    frame += "\\end{frame}\n\n"
    return frame



def diagram(cardiac):
    color = []
    step = cardiac.curr_step
    for x in range(0,6):
        color.append("black")
    color[step] = "red"
    str = ""
    str += "\\begin{tikzpicture}\n"
    str += "\\node[text width=2cm,align=center, rectangle, draw=%s,thick] (C) at (0,0) {1 - Charger dans le RI l'instr pointée par CO};\n" % color[1]
    str += "\\node[rectangle,draw=orange,thick] (CA) at (0,-1) {%s};\n" % cardiac.ri
    str += "\\node[text width=2cm,align=center, rectangle, draw=%s,thick] (O) at (3,0) {2 - Incr CO};\n" % color[2]
    str += "\\node[rectangle,draw=orange,thick] (OA) at (3,-0.5) {%s};\n" % cardiac.co
    str += "\\draw[->,thick] (C) -- (O);\n"
    str += "\\node[text width=2cm,align=center, rectangle, draw=%s,thick] (T) at (6,0) {3 - Traduire Inst};\n" % color[3]
    str += "\\node[rectangle,draw=orange,thick,text width=3cm, align=center] (TA) at (6,-0.85) {\\begin{varwidth}{3cm}%s\\end{varwidth}};\n" % cardiac.inst
    if not cardiac.end:
        str += "\\draw[->,thick] (O) -- (T);\n"
    str += "\\node[text width=2cm,align=center, rectangle, draw=%s,thick] (E) at (9,0) {4 -Exec + Acc};\n" % color[4]
    str += "\\node[rectangle,draw=orange,thick] (EA) at (9,-0.5) {Acc: %s (%s)};\n" % (cardiac.acc, cardiac.acc_bool)
    str += "\\draw[->,thick] (T) -- (E);\n"
    str += "\\path[->,thick] (E) edge[bend right=15] node [left] {} (C);\n"
    str += "\\node[text width=2cm,align=center, rectangle, draw=%s,thick] (S) at (3,1.2) {STOP};\n" % color[5]
    if cardiac.end:
        str += "\\draw[->,thick,red] (O) -- (S);\n"
    str += "\\end{tikzpicture}\n"
    return str



def str_input_output_mem(cardiac):
    str = ""
    str += "\\begin{small}\n"
    str += "\\begin{minipage}[t]{.20\\textwidth}\n"
    str += "\\vspace{0pt}\n"
    str += "\\begin{tabular}{|c|c|}\n"

    for i in range(0,15):
        str += ("\\hline\n")
        if i == cardiac.curr_input:
            str += ("\\textbf{\color{red}%s: %s} & %s: %s\\\\\n" % (i,cardiac.input[i], i+15,cardiac.input[i+15]))
        elif i+15 == cardiac.curr_input:
            str += ("%s: %s & \\textbf{\color{red}%s: %s}\\\\\n" % (i,cardiac.input[i], i+15,cardiac.input[i+15]))
        else:
            str += ("%s: %s & %s: %s\\\\\n" % (i,cardiac.input[i], i+15,cardiac.input[i+15]))


    str += "\\hline\n"
    str += "\end{tabular}\n"
    str += "\n\n"
    str += "\\begin{center}\n"
    str += "\\textbf{\\small Input}\n"
    str += "\\end{center}\n"
    str += "\end{minipage}%\n"
    str += "\\begin{minipage}[t]{.6\\textwidth}\n"
    str += "\\vspace{0pt}\n"
    str += "\\begin{center}\n"
    str += "\\begin{tabular}{|c|c|c|c|c|}\n"
    for i in range(0,20):
        str += "\\hline\n"
        str += "%s: %s & %s: %s & %s: %s & %s: %s & %s: %s \\\\\n" % (i,cardiac.mem[i],i+20,cardiac.mem[i+20],
            i+40,cardiac.mem[i+40],i+60,cardiac.mem[i+60],i+80,cardiac.mem[i+80])
    str += "\\hline\n"
    str += "\end{tabular}\n"
    str += "\n\n"
    str += "\\textbf{\\small mémoire centrale}\n"
    str += "\\end{center}\n"
    str += "\\end{minipage}\hfill%\n"
    str += "\\begin{minipage}[t]{.20\\textwidth}\n"
    str += "\\vspace{0pt}\n"
    str += "\\begin{tabular}{|c|c|}\n"
    for i in range(0,15):
        str += ("\\hline\n")
        if i == cardiac.curr_output:
            str += ("\\textbf{\color{red}%s: %s} & %s: %s\\\\\n" % (i,cardiac.output[i], i+15,cardiac.output[i+15]))
        elif i+15 == cardiac.curr_output:
            str += ("%s: %s & \\textbf{\color{red}%s: %s}\\\\\n" % (i,cardiac.output[i], i+15,cardiac.output[i+15]))
        else:
            str += ("%s: %s & %s: %s\\\\\n" % (i,cardiac.output[i], i+15,cardiac.output[i+15]))
    str += "\\hline\n"
    str += "\\end{tabular}\n"
    str += "\n\n"
    str += "\\begin{center}"
    str += "\\textbf{\\small Output}\n"
    str += "\\end{center}\n"
    str += "\\end{minipage}\hfill%\n"
    str += "\\end{small}\n"
    return str
