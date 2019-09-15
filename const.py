MAX_ITERATIONS = 50

opcode_to_name = {
    '0': "INP",
    '1': "OUT",
    '2': "LDA",
    '3': "LDI",
    '4': "STA",
    '5': "STI",
    '6': "ADD",
    '7': "SUB",
    '8': "JAZ",
    '9': "HRS",
}

opcode_to_desc = {
    '0': "Input",
    '1': "Output",
    '2': "Load to Acc",
    '3': "Load Indirect",
    '4': "Store from Acc",
    '5': "Store indirect",
    '6': "Add",
    '7': "Substract",
    '8': "Jump if Acc is zero",
    '9': "Halt and Reset",
}

opcode_to_trad = {
    '0': "Copier l'Input vers @$VALUE$ puis avancer input",
    '1': "Contenu de @$VALUE$ $=>$ out, avancer output",
    '2': "Charger dans Acc le contenu de @$VALUE$",
    '3': "Charger dans Acc le contenu à @ indiqué à \@ $VALUE$",
    '4': "Stocker le contenu de Acc à @$VALUE$",
    '5': "Stocker le contenu de Acc à @ indiqué à $VALUE$",
    '6': "Ajouter à l'Acc le contenu de @$VALUE$",
    '7': "Soustraite à Acc le contenu de @$VALUE$",
    '8': "Mettre le CO à $VALUE$ et sa valeur précédente à @ 99",
    '9': "END",
}
