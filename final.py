import sys

'''
Se termatiko: python3 final.py onoma_arxeiou.
To onoma tou arxeiou elegxou einai test.txt
Se auto to programma exoume ylopoihsei ton pinaka symvolwn
kai ena mikro kommati tou telikou kwdika.
'''

try:
    fp = open(sys.argv[1], 'r')
except IndexError:
    fp = open('test.txt', 'r')

alfavito = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z',
]

arithmoi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

grammi = 1

# Xaraktires
leukos_xaraktiras = 0
grammata = 1
psifia = 2
sin = 3
meion = 4
epi = 5
dia = 6
mikrotero = 7
megalytero = 8
ison = 9
erwtimatiko = 10
komma = 11
anw_katw_teleia = 12
aristeri_parenthesi = 13
deksia_parenthesi = 14
aristeri_agkyli = 15
deksia_agkyli = 16
aristero_agkistro = 17
deksi_agkistro = 18
allagi_grammis = 19
EOF = 20
mi_apodekto_symvolo = 21

# Tokens
id_tk = 22
noumero_tk = 23
sin_tk = 24
meion_tk = 25
epi_tk = 26
dia_tk = 27
ison_tk = 28
mikrotero_tk = 29
megalytero_tk = 30
mikrotero_iso_tk = 31
megalytero_iso_tk = 32
diaforo_tk = 33
anathesi_tk = 34
erwtimatiko_tk = 35
komma_tk = 36
anw_katw_teleia_tk = 37
aristeri_parenthesi_tk = 38
deksia_parenthesi_tk = 39
aristeri_agkyli_tk = 40
deksia_agkyli_tk = 41
aristero_agkistro_tk = 42
deksi_agkistro_tk = 43
EOF_tk = 44

desmeumenes_lekseis = ['program', 'declare',
                       'if', 'then', 'else',
                       'while', 'doublewhile', 'loop', 'exit',
                       'forcase', 'incase', 'when', 'default',
                       'not', 'and', 'or',
                       'function', 'procedure', 'call', 'return', 'in', 'inout',
                       'input', 'print']

program_tk = 45
declare_tk = 46
if_tk = 47
then_tk = 48
else_tk = 49
while_tk = 50
doublewhile_tk = 51
loop_tk = 52
exit_tk = 53
forcase_tk = 54
incase_tk = 55
when_tk = 56
default_tk = 57
not_tk = 58
and_tk = 59
or_tk = 60
function_tk = 61
procedure_tk = 62
call_tk = 63
return_tk = 64
in_tk = 65
inout_tk = 66
input_tk = 67
print_tk = 68

# Katastaseis
arxiki_katastasi = 0
gramma_katastasi = 1
psifio_katastasi = 2
mikrotero_katastasi = 3
megalytero_katastasi = 4
anw_katw_teleia_katastasi = 5
anoigma_sxoliwn_katatastasi = 6
kleisimo_sxoliwn_katastasi = 7
sxolia1_katastasi = 8  # sxolia1 = sxolia me: '/*   */'
sxolia2_katastasi = 9  # sxolia2 = sxolia me: '//'
emfwleumena_sxolia1_katastasi = 10
emfwleumena_sxolia2_katastasi = 11

# Katigories errors
ERROR_MI_APODEKTO_SYMVOLO = -1
ERROR_PSIFIO_GRAMMA = -2
ERROR_ARITHMOS_EKTOS_DIASTIMATOS = -3
ERROR_2_ANW_KATW_TELEIES = -4
ERROR_SXOLIA1_EOF = -5
ERROR_EMFWLEUMENA_SXOLIA = -6

metavaseis = [
    # arxiki_katastasi
    [arxiki_katastasi, gramma_katastasi, psifio_katastasi, sin_tk, meion_tk, epi_tk, anoigma_sxoliwn_katatastasi,
     mikrotero_katastasi, mikrotero_katastasi, ison_tk,
     erwtimatiko_tk, komma_tk, anw_katw_teleia_katastasi, aristeri_parenthesi_tk, deksia_parenthesi_tk,
     aristeri_agkyli_tk, deksia_agkyli_tk, aristero_agkistro_tk, deksi_agkistro_tk,
     arxiki_katastasi, EOF_tk, ERROR_MI_APODEKTO_SYMVOLO],

    # gramma_katastasi
    [id_tk, gramma_katastasi, gramma_katastasi, id_tk, id_tk, id_tk, id_tk, id_tk, id_tk, id_tk, id_tk, id_tk, id_tk,
     id_tk, id_tk, id_tk, id_tk, id_tk, id_tk, id_tk, id_tk, ERROR_MI_APODEKTO_SYMVOLO],

    # psifio_katastasi
    [noumero_tk, ERROR_PSIFIO_GRAMMA, psifio_katastasi, noumero_tk, noumero_tk, noumero_tk, noumero_tk, noumero_tk,
     noumero_tk, noumero_tk,
     noumero_tk, noumero_tk, noumero_tk, noumero_tk, noumero_tk, noumero_tk,
     noumero_tk, noumero_tk, noumero_tk, noumero_tk, noumero_tk, ERROR_MI_APODEKTO_SYMVOLO],

    # mikrotero_katastasi
    [mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk,
     diaforo_tk, mikrotero_iso_tk, mikrotero_tk, mikrotero_tk
        , mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk, mikrotero_tk,
     mikrotero_tk, mikrotero_tk, ERROR_MI_APODEKTO_SYMVOLO],

    # megalytero_katastasi
    [megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk,
     megalytero_tk, megalytero_tk, megalytero_iso_tk, megalytero_tk
        , megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk, megalytero_tk,
     megalytero_tk, megalytero_tk, megalytero_tk, ERROR_MI_APODEKTO_SYMVOLO],

    # anw_katw_teleia_katastasi
    [anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk,
     anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk
        , anw_katw_teleia_tk, anathesi_tk, anw_katw_teleia_tk, anw_katw_teleia_tk, ERROR_2_ANW_KATW_TELEIES,
     anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk
        , anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk, anw_katw_teleia_tk,
     ERROR_MI_APODEKTO_SYMVOLO],

    # anoigma_sxoliwn_katastasi
    [dia_tk, dia_tk, dia_tk, dia_tk, dia_tk, sxolia1_katastasi, sxolia2_katastasi, dia_tk, dia_tk, dia_tk, dia_tk,
     dia_tk, dia_tk
        , dia_tk, dia_tk, dia_tk, dia_tk, dia_tk, dia_tk, dia_tk, dia_tk, ERROR_MI_APODEKTO_SYMVOLO],

    # kleisimo_sxoliwn_katastasi
    [sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     kleisimo_sxoliwn_katastasi, arxiki_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, ERROR_SXOLIA1_EOF, sxolia1_katastasi],

    # sxolia1_katastasi
    [sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     kleisimo_sxoliwn_katastasi, emfwleumena_sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, ERROR_SXOLIA1_EOF, sxolia1_katastasi],

    # sxolia2_katastasi
    [sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi,
     emfwleumena_sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi
        , sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi,
     sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi,
     arxiki_katastasi, EOF_tk, sxolia2_katastasi],

    # emfwleumena_sxolia1_katastasi
    [sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     ERROR_EMFWLEUMENA_SXOLIA, ERROR_EMFWLEUMENA_SXOLIA, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi, sxolia1_katastasi,
     ERROR_SXOLIA1_EOF, sxolia1_katastasi],

    # emfwleumena_sxolia2_katastasi
    [sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi,
     ERROR_EMFWLEUMENA_SXOLIA, ERROR_EMFWLEUMENA_SXOLIA, sxolia2_katastasi, sxolia2_katastasi,
     sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi,
     sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi, sxolia2_katastasi,
     EOF_tk, sxolia2_katastasi]

]


def lex():
    global grammi

    count_digits = 0
    leksi = ''
    above30 = False
    katastasi = arxiki_katastasi
    plithos_grammwn = grammi
    lektiki_monada = []

    while (katastasi >= 0 and katastasi <= 11):  # oso vriskomaste se mia katastasi
        xaraktiras = fp.read(1)  # diavazei ena xaraktira apto arxeio

        if (xaraktiras == ' ' or xaraktiras == '\t'):
            xaraktiras_tk = leukos_xaraktiras
        elif (xaraktiras in alfavito):
            xaraktiras_tk = grammata
        elif (xaraktiras in arithmoi):
            xaraktiras_tk = psifia
        elif (xaraktiras == '+'):
            xaraktiras_tk = sin
        elif (xaraktiras == '-'):
            xaraktiras_tk = meion
        elif xaraktiras == '*':
            xaraktiras_tk = epi
        elif (xaraktiras == '/'):
            xaraktiras_tk = dia
        elif (xaraktiras == '<'):
            xaraktiras_tk = mikrotero
        elif (xaraktiras == '>'):
            xaraktiras_tk = megalytero
        elif (xaraktiras == '='):
            xaraktiras_tk = ison
        elif (xaraktiras == ';'):
            xaraktiras_tk = erwtimatiko
        elif (xaraktiras == ','):
            xaraktiras_tk = komma
        elif (xaraktiras == ':'):
            xaraktiras_tk = anw_katw_teleia
        elif (xaraktiras == '('):
            xaraktiras_tk = aristeri_parenthesi
        elif (xaraktiras == ')'):
            xaraktiras_tk = deksia_parenthesi
        elif (xaraktiras == '['):
            xaraktiras_tk = aristeri_agkyli
        elif (xaraktiras == ']'):
            xaraktiras_tk = deksia_agkyli
        elif (xaraktiras == '{'):
            xaraktiras_tk = aristero_agkistro
        elif (xaraktiras == '}'):
            xaraktiras_tk = deksi_agkistro
        elif (xaraktiras == '\n'):
            plithos_grammwn = plithos_grammwn + 1
            xaraktiras_tk = allagi_grammis
        elif (xaraktiras == ''):
            xaraktiras_tk = EOF
        else:
            xaraktiras_tk = mi_apodekto_symvolo

        # xrisimopoioume ton pinaka gia na vroume se poia katastasi vriskomaste
        katastasi = metavaseis[katastasi][xaraktiras_tk]

        if (len(leksi) <= 30):
            if (katastasi == psifio_katastasi):
                count_digits += 1  # gia na apofygoume periptwsi yperxeilisis
            if (katastasi != anoigma_sxoliwn_katatastasi and
                    katastasi != sxolia1_katastasi and
                    katastasi != sxolia2_katastasi and
                    katastasi != kleisimo_sxoliwn_katastasi):
                if (katastasi != arxiki_katastasi):
                    leksi += xaraktiras
            else:
                if (len(leksi) == 0):
                    leksi = ''

        else:
            print("O metaglwttistis lamvanei ypopsin tou mono ta prwta 30 grammata mias leksis!")
            above30 = True

    # Elegxos se poia katastasi vriskomaste kai apothikeusi tou epomenou xaraktira
    if (katastasi == id_tk or katastasi == noumero_tk or
            katastasi == mikrotero_tk or katastasi == megalytero_tk or
            katastasi == dia_tk or katastasi == anw_katw_teleia_tk):
        if (xaraktiras == '\n'):
            plithos_grammwn -= 1
        xaraktiras = fp.seek(fp.tell() - 1, 0)

        leksi = leksi[:-1]

    # Elegxos an einai i leksi einai desmeumeni
    if (katastasi == id_tk):
        if (leksi == 'program'):
            katastasi = program_tk
        elif (leksi == 'declare'):
            katastasi = declare_tk
        elif (leksi == 'if'):
            katastasi = if_tk
        elif (leksi == 'then'):
            katastasi = then_tk
        elif (leksi == 'else'):
            katastasi = else_tk
        elif (leksi == 'while'):
            katastasi = while_tk
        elif (leksi == 'doublewhile'):
            katastasi = doublewhile_tk
        elif (leksi == 'loop'):
            katastasi = loop_tk
        elif (leksi == 'exit'):
            katastasi = exit_tk
        elif (leksi == 'forcase'):
            katastasi = forcase_tk
        elif (leksi == 'incase'):
            katastasi = incase_tk
        elif (leksi == 'when'):
            katastasi = when_tk
        elif (leksi == 'default'):
            katastasi = default_tk
        elif (leksi == 'not'):
            katastasi = not_tk
        elif (leksi == 'and'):
            katastasi = and_tk
        elif (leksi == 'or'):
            katastasi = or_tk
        elif (leksi == 'function'):
            katastasi = function_tk
        elif (leksi == 'procedure'):
            katastasi = procedure_tk
        elif (leksi == 'call'):
            katastasi = call_tk
        elif (leksi == 'return'):
            katastasi = return_tk
        elif (leksi == 'in'):
            katastasi = in_tk
        elif (leksi == 'inout'):
            katastasi = inout_tk
        elif (leksi == 'input'):
            katastasi = input_tk
        elif (leksi == 'print'):
            katastasi = print_tk

    if (katastasi == noumero_tk):
        if (count_digits > 5):
            katastasi = ERROR_ARITHMOS_EKTOS_DIASTIMATOS

        if (int(leksi) < -32767 or int(leksi) > 32767):
            katastasi = ERROR_ARITHMOS_EKTOS_DIASTIMATOS

    if (katastasi == ERROR_MI_APODEKTO_SYMVOLO):
        print("ERROR: Yparxei mi apodekto symbolo glwssas, GRAMMI: ", grammi)
        exit(-1)
    elif (katastasi == ERROR_PSIFIO_GRAMMA):
        print("ERROR: Yparxei Gramma meta apo kapoio psifio, GRAMMI: ", grammi)
        exit(-1)
    elif (katastasi == ERROR_ARITHMOS_EKTOS_DIASTIMATOS):
        print("ERROR: Arithmos pou den anikei sto diastima [-32767, 32767], GRAMMI: ", grammi)
        exit(-1)
    elif (katastasi == ERROR_2_ANW_KATW_TELEIES):
        print("ERROR: 2 anw katw teleies synexomenes, GRAMMI: ", grammi)
        exit(-1)
    elif (katastasi == ERROR_EMFWLEUMENA_SXOLIA):
        print("ERROR: Emfwleumena sxolia, GRAMMI: ", grammi)
        exit(-1)

    # I lektiki monada einai mia lista me 3 stoixeia. To prwto stoixeio einai to noumero tou token.
    # To deutero stoixeio einai i lektiki monada pou sximatistike apo ti lektiki analysi
    # To trito stoixeio einai o arithmos grammis tis lektikis monadas
    lektiki_monada.append(katastasi)
    lektiki_monada.append(leksi)
    lektiki_monada.append(plithos_grammwn)
    grammi = plithos_grammwn

    return lektiki_monada





###################################################################################
###################################################################################
###################################################################################
############################# ENDIAMESOS KWDIKAS ##################################
###################################################################################
###################################################################################
###################################################################################


global quads_list  # Lista pou periexei oles tis tetrades


quads_list = []
quad_id = 1  # O xaraktiristikos(monadikos) arithmos tis kathe tetradas

# Epistrefei ton arithmo tis epomenis tetradas pou prokeitai na paraxthei
def nextQuad():
    global quad_id
    return quad_id

# Dimiourgei tin epomeni tetrada
# O arithmos pou epistrefei i nextQuad tha eisaxthei prwtos sti lista
def genQuad(op, x, y, z):

    global quad_id
    global quads_list

    # I lista pou tha periexei tis pentades
    quintuple = []

    # Vazoume ton arithmo tis nextQuad
    apotelesma_nextQuad = nextQuad()

    # Vazoume ta ypoloipa orismata
    quintuple.extend((apotelesma_nextQuad, op, x, y, z))

    # Prosauksanoume kata 1 ton arithmo tis epomenis tetradas
    quad_id +=1

    # Vazoume tin pentada sti lista me oles tis tetrades
    quads_list.append(quintuple)

    return quintuple



T_id = 1
temp_list = []

# Dimiourgei kai prosthetei mia nea proswrini metavliti
def newTemp():
    global temp_list
    global T_id

    temp = 'T_'
    temp += str(T_id)       # temp = T_x opou x = 1,2,3,...

    # Prosauksanoume to xaraktiristiko arithmo tis kathe proswrinis metavlitis
    T_id +=1
    temp_list.append(temp)  # Vazoume tin proswrini metavliti stin temp_list

    entity = Entity()
    entity.type = "TEMP"
    entity.name = temp
    entity.tempVar.offset = calculate_offset()
    create_new_entity(entity)


    return temp


# Dimiourgei mia keni lista etiketwn tetradwn
def emptylist():

    list_of_pointers = []	#Arxikopoihsh pointer list.

    return list_of_pointers


# Dimiourgei mia lista etiketwn tetradwn pou periexei mono to x
def makeList(x):

    list_x = [x]

    return list_x

# Dimiourgei mia lista etiketwn tetradwn apo ti synenwsi twn listwn list1, list2
def merge(list1, list2):

    merged_list = []
    merged_list += list1 + list2

    return merged_list


'''
I lista list apoteleitai apo deiktes se tetrades twn opoiwn to teleutaio
teloumeno den einai symplirwmeno. I backPatch episkeptetai mia mia tis tetrades
autes kai tis symplirwnei me tin etiketa z.
'''

def backPatch(list, z):
    global quads_list

    # To megethos tis listas pou einai parametros
    list_size = len(list)
    # To megethos tis listas me oles tis tetrades
    all_quads_size = len(quads_list)

    i = 0

    '''
    Gia kathe tetrada pou yparxei stin quads_list kai exei idio prwto teloumeno
    me ti list, tha symplirwnoume to z se kathe keni thesi
    '''
    while i < list_size:
        for j in range(all_quads_size):
            if list[i] == quads_list[j][0]:
                quads_list[j][4] = z
                break
        i += 1

    return









###################################################################################
###################################################################################
###################################################################################
############################### PINAKAS SYMVOLWN ##################################
###################################################################################
###################################################################################
###################################################################################


class Argument():

    def __init__(self):
        self.type = "Int"
        self.name = ''
        self.parMode = ''

class Entity():
    def __init__(self):
        self.type = ''
        self.name = ''
        self.variable = self.Variable()
        self.tempVar = self.TempVar()
        self.subprogram = self.SubProgram()
        self.parameter = self.Parameter()


    class Variable:
        def __init__(self):
            self.type = "Int"
            self.offset = 0

    class SubProgram:
        def __init__(self):
            self.type = ''

            # H proti tetrada apo ton endiameso
            self.startQuad = 0

            # To mikos tou eggrafimatos drastiriopoiisis
            self.frameLength = 0
            self.list_of_arguments = []

    class Parameter:
        def __init__(self):
            self.mode = ''
            self.offset = 0
    class TempVar:
        def __init__(self):
            self.type = 'Int'
            self.offset = 0
class Scope():
    '(_)  <- Kyklos'
    def __init__(self):
        self.name = ''
        self.list_of_entities = []

        # Vathos fwliasmatos
        self.nestingLevel = 0
        self.enclosingScope = None



top_scope = None

# Dimiourgia scope
def create_new_scope(name):
    global top_scope

    nextScope = Scope()
    nextScope.name = name

    if(top_scope != None):
        # To epipedo fwliasmatos tha isoutai me oso eixe to panw scope + 1
        nextScope.nestingLevel = top_scope.nestingLevel + 1
    else:
        nextScope.nestingLevel = 0


    nextScope.enclosingScope=top_scope

    top_scope = nextScope


# Dimiourgia entity
def create_new_entity(object):
    'Add given object to list'
    global top_scope

    top_scope.list_of_entities.append(object)  # To neo entity mpainei sti lista


# Dimiourgia argument
def create_new_argument(object):
    'Add given object to list'
    global top_scope

    # Vazei sti lista to list_of_entities[-1], diladi to teleutaio entity, to opoio einai function i procedure
    top_scope.list_of_entities[-1].subprogram.list_of_arguments.append(object)



# Svisimo scope
def delete_scope():
    global top_scope

    # Diagrafei ola ta entities sti list_of_entities, ousiastika apodesmeuei ti mnimi
    if top_scope.list_of_entities:
        for i in range(len(top_scope.list_of_entities)):
            top_scope.list_of_entities.pop()

    # Exoume kainourio scope
    top_scope = top_scope.enclosingScope

# Ypologizei to offset kathe metavlitis
def calculate_offset():
    global top_scope

    # Metraei posa entities exoume vrei
    entity_counter=0

    # An i lista me ta entities den einai keni vriskoume posa entities exei
    if top_scope.list_of_entities:
        for ent in top_scope.list_of_entities:  # pigaino se OLA ta entities (orthogonia) tis grammis(optika) pou vriskomai
            if ent.type == "VAR" or ent.type == "TEMP" or ent.type == "PARAM":  # OXI 'SUBPR' = YPOPROGRAMMA (den exei offset)
                entity_counter += 1

    offset = 12 + entity_counter * 4

    return offset

def calculate_startQuad():
    global top_scope

    # Enimerwnei to startQuad tou teleutaio entity tis listas tou katw scope, to opoio einai function i procedure
    top_scope.enclosingScope.list_of_entities[-1].subprogram.startQuad = nextQuad()

def calculate_framelength(): # kaleite stin "block" PRIN to "end_block"
    'Compute frameLength of function or procedure.'
    global top_scope

    # Enimerwnei to frameLength tou teleutaio entity tis listas tou katw scope, to opoio einai function i procedure
    top_scope.enclosingScope.list_of_entities[-1].subprogram.frameLength = calculate_offset()

# Dimiourgei entities apo tis parametrous enos function i procedure
def add_parameters():
    global top_scope

    for argument in top_scope.enclosingScope.list_of_entities[-1].subprogram.list_of_arguments:
        entity = Entity()
        entity.type = "PARAM"
        entity.name = argument.name
        entity.parameter.mode = argument.parMode
        entity.parameter.offset = calculate_offset()
        create_new_entity(entity)

# Typwnei ton pinaka symvolwn
def print_table():
    'Prints Symbol-Table: Scopes, Entities, Arguments'
    global top_scope

    print("########################################################################################################################\n")

    current_scope=top_scope
    while current_scope != None:
        print("SCOPE: " + "name: " + current_scope.name + " nestingLevel:" + str(current_scope.nestingLevel))
        print("\tENTITIES:")
        for entity in current_scope.list_of_entities:
            if(entity.type == "VAR"):
                print("\tENTITY:" + " name: " + entity.name+"\t type: " + entity.type+"\t variable-type: " + entity.variable.type+"\t offset: " + str(entity.variable.offset))
            elif(entity.type == "TEMP"):
                print("\tENTITY:" + " name: " + entity.name+"\t type: " + entity.type+"\t temp-type: " + entity.tempVar.type+"\t offset: " + str(entity.tempVar.offset))
            elif(entity.type == "SUBPR"):
                if(entity.subprogram.type == "Function"):
                    print("\tENTITY:" + " name: " + entity.name+"\t type: " + entity.type+"\t function-type: " + entity.subprogram.type+"\t startQuad: " + str(entity.subprogram.startQuad) + "\t frameLength:" + str(entity.subprogram.frameLength))
                    print("\t\tARGUMENTS:")
                    for arg in entity.subprogram.list_of_arguments:
                        print("\t\tARGUMENT: " + " name:"+arg.name + "\t type: " + arg.type + "\t parMode: " + arg.parMode)
                elif(entity.subprogram.type == "Procedure"):
                    print("\tENTITY:" + " name: " + entity.name + "\t type: " + entity.type + "\t procedure-type: " + entity.subprogram.type + "\t startQuad: " + str(entity.subprogram.startQuad) + "\t frameLength:" + str(entity.subprogram.frameLength))
                    print("\t\tARGUMENTS:")
                    for arg in entity.subprogram.list_of_arguments:
                        print("\t\tARGUMENT:" + " name: " + arg.name+"\t type: " + arg.type + "\t parMode: " + arg.parMode)
            elif(entity.type == "PARAM"):
                print("\tENTITY:" + " name: " + entity.name + "\t type: " + entity.type + "\t mode: " + entity.parameter.mode + "\t offset: " + str(entity.parameter.offset))
        current_scope = current_scope.enclosingScope

    print("########################################################################################################################\n")





###################################################################################
###################################################################################
###################################################################################
############################# TELIKOS KWDIKAS ##################################
###################################################################################
###################################################################################
###################################################################################


asm_fd = open('final.asm', 'w')

# Antistoixizei se assembly entoles kathe 4ada pou exei dimiourgithei kai
# tis grafei sto arxeio final.asm 
def produce_final_code():
    global asm_fd
    global quads_list
    global top_scope

    for i in range(len(quads_list)):
        asm_fd.write('L' + str(quads_list[i][0]) + ':\n')

        if quads_list[i][1] == "JUMP":
            asm_fd.write("j L" + str(quads_list[i][4]) + '\n')
        elif quads_list[i][1] == '=':
            asm_fd.write("beq,$t1,$t2,L" + quads_list[i][4] + '\n')
        elif quads_list[i][1] == '<':
            asm_fd.write("blt,$t1,$t2,L" + str(quads_list[i][4]) + '\n')
        elif quads_list[i][1] == '>':
            asm_fd.write("bgt,$t1,$t2,L" + str(quads_list[i][4]) + '\n')
        elif quads_list[i][1] == '<=':
            asm_fd.write("ble,$t1,$t2,L" + str(quads_list[i][4]) + '\n')
        elif quads_list[i][1] == '>=':
            asm_fd.write("bge,$t1,$t2,L" + str(quads_list[i][4]) + '\n')
        elif quads_list[i][1] == '<>':
            asm_fd.write("bne,$t1,$t2,L" + str(quads_list[i][4]) + '\n')
        elif quads_list[i][1] == ':=':
            fill = 1
        elif quads_list[i][1] == '+':
            asm_fd.write("add,$t1,$t1,$t2\n")
        elif quads_list[i][1] == '-':
            asm_fd.write("sub,$t1,$t1,$t2\n")
        elif quads_list[i][1] == '*':
            asm_fd.write("mul,$t1,$t1,$t2\n")
        elif quads_list[i][1] == '/':
            asm_fd.write("div,$t1,$t1,$t2\n")
        elif quads_list[i][1] == "out":
            asm_fd.write("li $v0,1" + str(quads_list[i][4]) + '\n')
            asm_fd.write("move $a0,$t1" + str(quads_list[i][4]) + '\n')
            asm_fd.write("syscall\n")
        elif quads_list[i][1] == "in":
            asm_fd.write("li $v0,1\n")
            asm_fd.write("syscall\n")
            asm_fd.write("move $t1,$v0\n")
        elif quads_list[i][1] == "retv":
            asm_fd.write("lw $t0,-8($sp)\n")
            asm_fd.write("sw $t1,($t0)\n")
        elif quads_list[i][1] == "par":
            fill = 1










###################################################################################
###################################################################################
###################################################################################
############################# SYNTAKTIKI ANALYSI ##################################
###################################################################################
###################################################################################
###################################################################################

declare_flag = 0

def syntaktiki_analysi(c_fd):
    global grammi
    global result
    global isFunction
    global temp

    isFunction = 0

    result = lex()
    grammi = result[2]

    def program():
        global grammi
        global result

        if (result[0] == program_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == id_tk):
                program_name = result[1]
                result = lex()
                grammi = result[2]
                if (result[0] == aristero_agkistro_tk):
                    result = lex()
                    grammi = result[2]
                    block(program_name, 1)
                    if (result[0] == deksi_agkistro_tk):
                        result = lex()
                        grammi = result[2]
                        return

                    else:
                        print("Leipei to deksi agkistro '}', GRAMMI: ", grammi)
                        exit(-1)
                else:
                    print("Leipei to aristero agkistro '{', GRAMMI: ", grammi)
                    exit(-1)
            else:
                print("Leipei to onoma programmatos, GRAMMI: ", grammi)
                exit(-1)
        else:
            print("Leipei i leksi 'program', GRAMMI: ", grammi)
            exit(-1)

    def block(block_name, program_block):
        global result

        create_new_scope(block_name)

        if program_block != 1:
            add_parameters()

        declarations()
        subprograms()

        genQuad('begin_block', block_name, '_', '_')

        # Vriskoume to startQuad meta apo function i procedure tis epomenis tetradas
        if program_block != 1:
            calculate_startQuad()

        statements()

        if (program_block == 1):
            genQuad('halt', '_', '_', '_')
        else:
            calculate_framelength()
        genQuad('end_block', block_name, '_', '_')

        print("Pinakas Symvolwn:")
        print_table()

        produce_final_code()

        delete_scope()
        print("Diagrafike to teleutaio scope")


    def declarations():
        global result
        global declare_flag

        while (result[0] == declare_tk):
            c_fd.write("int ")
            result = lex()
            grammi = result[2]
            varlist()
            if (result[0] == erwtimatiko_tk):
                c_fd.write(';')

                result = lex()
                grammi = result[2]

            else:
                print("Leipei to erwtimatiko ';', GRAMMI: ", grammi)
                exit(-1)

        return

    def varlist():
        global result

        if (result[0] == id_tk):
            c_fd.write(result[1])

            ent = Entity()
            ent.type = "VAR"
            ent.name = result[1]
            ent.variable.offset = calculate_offset()
            create_new_entity(ent)

            result = lex()
            grammi = result[2]
            while (result[0] == komma_tk):
                c_fd.write(',')

                result = lex()
                grammi = result[2]
                if (result[0] == id_tk):
                    c_fd.write(result[1])

                    entity = Entity()
                    entity.type = "VAR"
                    entity.name = result[1]
                    entity.variable.offset = calculate_offset()
                    create_new_entity(entity)

                    result = lex()
                    grammi = result[2]

                else:
                    print("Leipei to komma ',' i leipei to onoma metavlitis. GRAMMI: ", grammi)
                    exit(-1)

        return

    def subprograms():
        global result

        while (result[0] == function_tk or result[0] == procedure_tk):
            subprogram()

        return

    def subprogram():
        global result

        if (result[0] == function_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == id_tk):
                sub_prog_name = result[1]

                entity = Entity()
                entity.type = "SUBPR"
                entity.name = result[1]
                entity.subprogram.type = "Function"
                create_new_entity(entity)

                result = lex()
                grammi = result[2]
                funcbody(sub_prog_name, 1)
                return

            else:
                print("Leipei to onoma tou 'function', GRAMMI: ", grammi)
                exit(-1)

        elif (result[0] == procedure_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == id_tk):
                sub_prog_name = result[1]

                entity = Entity()
                entity.type = "SUBPR"
                entity.name = result[1]
                entity.subprogram.type = "Procedure"
                create_new_entity(entity)

                result = lex()
                grammi = result[2]
                funcbody(sub_prog_name, 0)
                return

            else:
                print("Leipei to onoma tis procedure, GRAMMI: ", grammi)
                exit(-1)

        return

    def funcbody(block_name, isFunction):
        global result
        global grammi

        formalpars()
        if (result[0] == aristero_agkistro_tk):
            result = lex()
            grammi = result[2]
            block(block_name, -1)
            if (result[0] == deksi_agkistro_tk):
                result = lex()
                grammi = result[2]

            else:
                print("Leipei to deksi agkistro '}', GRAMMI: ", grammi)
                exit(-1)
        else:

            print("Leipei to aristero agkistro '{', GRAMMI: ", grammi)
            exit(-1)

        return

    def formalpars():
        global result
        global grammi

        if (result[0] == aristeri_parenthesi_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == in_tk or result[0] == inout_tk):
                formalparlist()
                if (result[0] == deksia_parenthesi_tk):
                    result = lex()
                    grammi = result[2]
                    return

                else:
                    print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                    exit(-1)

            elif (result[0] == deksia_parenthesi_tk):
                result = lex()
                grammi = result[2]
                return

        else:
            print("Leipei i aristeri parenthesi '(', GRAMMI: ", grammi)
            exit(-1)

    def formalparlist():
        global result

        formalparitem()
        while (result[0] == komma_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == in_tk or result[0] == inout_tk):
                formalparitem()

        return

    def formalparitem():
        global result

        if (result[0] == in_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == id_tk):
                argument = Argument()
                argument.name = result[1]
                argument.parMode = "CV"
                create_new_argument(argument)

                result = lex()
                grammi = result[2]
                return

            else:
                print("Leipei to onoma metavlitis meta to 'in', GRAMMI: ", grammi)
                exit(-1)

        elif (result[0] == inout_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == id_tk):
                argument = Argument()
                argument.name = result[1]
                argument.parMode = "REF"
                create_new_argument(argument)

                result = lex()
                grammi = result[2]
                return

            else:
                print("Leipei to onoma metavlitis meta to 'inout', GRAMMI: ", grammi)
                exit(-1)

        return

    def statements():
        global result

        if (result[0] == aristero_agkistro_tk):
            result = lex()
            grammi = result[2]
            statement()

            while (result[0] == erwtimatiko_tk):
                result = lex()
                grammi = result[2]
                statement()

            if (result[0] == deksi_agkistro_tk):
                result = lex()
                grammi = result[2]
                return

            else:
                print("Leipei to deksi agkistro '}', GRAMMI: ", grammi)
                exit(-1)
        else:
            statement()

        return

    def statement():
        global result

        if (result[0] == id_tk):
            assignment_stat()
        elif (result[0] == if_tk):
            if_stat()
        elif (result[0] == while_tk):
            while_stat()
        elif (result[0] == doublewhile_tk):
            doublewhile_stat()
        elif (result[0] == loop_tk):
            loop_stat()
        elif (result[0] == exit_tk):
            exit_stat()
        elif (result[0] == forcase_tk):
            forcase_stat()
        elif (result[0] == incase_tk):
            incase_stat()
        elif (result[0] == call_tk):
            call_stat()
        elif (result[0] == return_tk):
            return_stat()
        elif (result[0] == input_tk):
            input_stat()
        elif (result[0] == print_tk):
            print_stat()

        return

    def assignment_stat():
        global result
        global isFunction
        global temp

        assignmenT_idd = result[1]
        result = lex()
        grammi = result[2]

        if (result[0] == anathesi_tk):
            result = lex()
            grammi = result[2]
            E_place = expression()

            # P1
            if (isFunction == 1):
                genQuad(':=', temp, '_', assignmenT_idd)
                isFunction = 0
            else:
                genQuad(':=', E_place, '_', assignmenT_idd)
            return
        else:
            print("Leipei to symvolo tis anathesis ':=', GRAMMI:", grammi)
            exit(-1)

        return

    def if_stat():
        global result

        result = lex()
        grammi = result[2]

        if (result[0] == aristeri_parenthesi_tk):
            result = lex()
            grammi = result[2]

            '''
            Periexei 2 listes afou ginei klisi tis condition. Mia lista gia true kai mia gia
            false synthikes.
            true_false_lists[0] : gia tis true synthikes
            true_false_lists[1] : gia tis false synthikes
            '''
            true_false_lists = condition()

            if (result[0] == deksia_parenthesi_tk):
                result = lex()
                grammi = result[2]

                if (result[0] == then_tk):
                    result = lex()
                    grammi = result[2]

                    # P1
                    backPatch(true_false_lists[0], nextQuad())
                    statements()

                    # P2
                    ifList = makeList(nextQuad())
                    genQuad('jump', '_', '_', '_')
                    backPatch(true_false_lists[1], nextQuad())
                    elsepart()

                    # P3
                    backPatch(ifList, nextQuad())

                    return

                else:
                    print("Leipei to 'then', GRAMMI: ", grammi)
                    exit(-1)

            else:
                print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                exit(-1)

        else:
            print("Leipei i aristeri parenthesi '(', GRAMMI: ", grammi)
            exit(-1)

        is_true = true_false_lists[0]
        is_false = true_false_lists[1]

        return is_true, is_false

    def elsepart():
        global result

        if (result[0] == else_tk):
            result = lex()
            grammi = result[2]
            statements()

        return

    def while_stat():
        global result
        global grammi



        if (result[0] == while_tk):
            result = lex()
            grammi = result[2]

            if (result[0] == aristeri_parenthesi_tk):
                result = lex()
                grammi = result[2]

                # P1
                Bquad = nextQuad()

                true_false_lists = condition()

                if (result[0] == deksia_parenthesi_tk):

                    # P2
                    backPatch(true_false_lists[0], nextQuad())

                    result = lex()
                    grammi = result[2]
                    statements()

                    # P3
                    genQuad('jump', '_', '_', Bquad)
                    backPatch(true_false_lists[1], nextQuad())

                    return

                else:
                    print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                    exit(-1)
            else:
                print("Leipei i aristeri parenthesi '(', GRAMMI: ", grammi)
                exit(-1)
        else:
            print("Leipei to 'while', GRAMMI: ", grammi)
            exit(-1)

        WStrue = true_false_lists[0]
        WSfalse = true_false_lists[1]

        return WStrue, WSfalse

    def doublewhile_stat():
        global result
        global grammi

        if (result[0] == doublewhile_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == aristeri_parenthesi_tk):
                result = lex()
                grammi = result[2]
                condition()
                if (result[0] == deksia_parenthesi_tk):
                    result = lex()
                    grammi = result[2]
                    statements()
                    if (result[0] == else_tk):
                        result = lex()
                        grammi = result[2]
                        statements()
                        return
                    else:
                        print("Leipei to 'else', GRAMMI: ", grammi)
                        exit(-1)
                else:
                    print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                    exit(-1)
            else:
                print("Leipei i aristeri parenthesi '(', GRAMMI: ", grammi)
                exit(-1)
        else:
            print("Leipei to 'doublewhile', GRAMMI: ", grammi)
            exit(-1)

        return

    def loop_stat():
        global result
        global grammi

        if (result[0] == loop_tk):
            result = lex()
            grammi = result[2]
            statements()
            return
        else:
            print("Leipei to 'loop', GRAMMI: ", grammi)

    def exit_stat():
        global result
        global grammi

        if (result[0] == exit_tk):
            result = lex()
            grammi = result[2]
            return
        else:
            print("Leipei to 'exit', GRAMMI: ", grammi)
            exit(-1)

    def forcase_stat():
        global result
        global grammi

        if (result[0] == forcase_tk):
            # P1
            fc_quad = nextQuad()

            result = lex()
            grammi = result[2]
            while (result[0] == when_tk):
                result = lex()
                grammi = result[2]
                if (result[0] == aristeri_parenthesi_tk):
                    result = lex()
                    grammi = result[2]
                    true_false_lists = condition()
                    if (result[0] == deksia_parenthesi_tk):
                        # P1
                        backPatch(true_false_lists[0], nextQuad())

                        result = lex()
                        grammi = result[2]
                        if (result[0] == anw_katw_teleia_tk):
                            result = lex()
                            grammi = result[2]
                            statements()

                            # P2
                            genQuad("jump", '_', '_', fc_quad)
                            backPatch(true_false_lists[1], nextQuad())
                        else:
                            print("Leipei i anw katw teleia ':', GRAMMI: ", grammi)
                            exit(-1)
                    else:
                        print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                        exit(-1)
                else:
                    print("Leipei i aristeri parenthesi '(', GRAMMI: ", grammi)
                    exit(-1)

            if (result[0] == default_tk):
                result = lex()
                grammi = result[2]
                if (result[0] == anw_katw_teleia_tk):
                    result = lex()
                    grammi = result[2]
                    statements()
                    return

                else:
                    print("Leipei i anw katw teleia ':', GRAMMI: ", grammi)
                    exit(-1)
            else:
                print("Leipei to 'default: <statements>', GRAMMI: ", grammi)
                exit(-1)
        else:
            print("Leipei to 'forcase', GRAMMI: ", grammi)
            exit(-1)

        fcase_true = true_false_lists[0]
        fcase_false = true_false_lists[1]

        return fcase_true, fcase_false

    def incase_stat():
        global result
        global grammi

        if (result[0] == incase_tk):
            result = lex()
            grammi = result[2]
            while (result[0] == when_tk):
                result = lex()
                grammi = result[2]
                if (result[0] == aristeri_parenthesi_tk):
                    result = lex()
                    grammi = result[2]
                    condition()
                    if (result[0] == deksia_parenthesi_tk):
                        result = lex()
                        grammi = result[2]
                        if (result[0] == anw_katw_teleia_tk):
                            result = lex()
                            grammi = result[2]
                            statements()

                        else:
                            print("Leipei i anw katw teleia ':', GRAMMI: ", grammi)
                            exit(-1)
                    else:
                        print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                        exit(-1)
                else:
                    print("Leipei i aristeri parenthesi '(', GRAMMI: ", grammi)
                    exit(-1)
        else:
            print("Leipei to 'incase', GRAMMI: ", grammi)
            exit(-1)

        return

    def return_stat():
        global result
        global grammi

        if (result[0] == return_tk):
            result = lex()
            grammi = result[2]
            E_place = expression()

            # P1
            genQuad('retv', E_place, '_', '_')
            return
        else:
            print("Leipei to 'return', GRAMMI: ", grammi)
            exit(-1)

        return

    def call_stat():
        global result
        global grammi

        result = lex()
        grammi = result[2]
        id_name = result[1]
        if (result[0] == id_tk):
            result = lex()
            grammi = result[2]
            actualpars(0, id_name)
        else:
            print("Leipei to onoma tis synartisis, GRAMMI: ", grammi)
            exit(-1)

        return

    def print_stat():
        global result
        global grammi

        if (result[0] == print_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == aristeri_parenthesi_tk):
                result = lex()
                grammi = result[2]
                E_place = expression()
                if (result[0] == deksia_parenthesi_tk):
                    result = lex()
                    grammi = result[2]

                    # P2
                    genQuad('out', E_place, '_', '_')
                    return

                else:
                    print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                    exit(-1)
            else:
                print("Leipei i aristeri parenthesi '(', GRAMMI: ", grammi)
                exit(-1)
        else:
            print("Leipei to 'print', GRAMMI: ", grammi)
            exit(-1)

        return

    def input_stat():
        global result
        global grammi

        if (result[0] == input_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == aristeri_parenthesi_tk):
                result = lex()
                grammi = result[2]
                if (result[0] == id_tk):
                    id_place = result[1]

                    # P1
                    genQuad('inp', id_place, '_', '_')
                    result = lex()
                    grammi = result[2]

                    if (result[0] == deksia_parenthesi_tk):
                        result = lex()
                        grammi = result[2]
                        return

                    else:
                        print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                        exit(-1)

                else:
                    print("Leipei i parametros tou 'input', GRAMMI: ", grammi)
                    exit(-1)
            else:

                print("Leipei i aristeri parenthesi ')', GRAMMI: ", grammi)
                exit(-1)
        else:
            print("Leipei to 'input', GRAMMI: ", grammi)
            exit(-1)

    def actualpars(isFunction, id_name):
        global result
        global grammi
        global temp

        if (result[0] == aristeri_parenthesi_tk):
            actualparlist()
            if (result[0] == deksia_parenthesi_tk):
                result = lex()
                grammi = result[2]

                if (isFunction == 1):
                    w = newTemp()
                    genQuad('par', w, 'RET', '_')
                    genQuad('call', id_name, '_', '_')

                    temp = w

                else:
                    genQuad('call', id_name, '_', '_')

                return

            else:
                print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                exit(-1)

        return

    def actualparlist():
        global result
        global grammi

        actualparitem()
        while (result[0] == komma_tk):
            actualparitem()

        return

    def actualparitem():
        global result
        global grammi

        result = lex()
        grammi = result[2]

        if (result[0] == in_tk):
            result = lex()
            grammi = result[2]
            actual_expression = expression()
            genQuad('par', actual_expression, 'CV', '_')
        elif (result[0] == inout_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == id_tk):
                genQuad('par', result[1], 'REF', '_')
                result = lex()
                grammi = result[2]
                return

            else:
                print("Leipei i metavliti meta to 'inout', GRAMMI: ", grammi)
                exit(-1)
        else:
            print("Leipei to in i to inout, GRAMMI: ", grammi)
            exit(-1)

        return

    def condition():
        global result

        Q1 = boolterm()

        # P1
        B_true = Q1[0]
        B_false = Q1[1]

        while (result[0] == or_tk):
            result = lex()
            grammi = result[2]

            # P2
            backPatch(B_false, nextQuad())

            Q2 = boolterm()

            # P3
            B_true = merge(B_true, Q2[0])
            B_false = Q2[1]

        return B_true, B_false

    def boolterm():
        global result

        R1 = boolfactor()

        # P1
        Q_true = R1[0]
        Q_false = R1[1]

        while (result[0] == and_tk):
            result = lex()
            grammi = result[2]

            backPatch(Q_true, nextQuad())

            R2 = boolfactor()

            # P3
            Q_false = merge(Q_false, R2[1])
            Q_true = R2[0]

        return Q_true, Q_false

    def boolfactor():
        global result

        R_true = []
        R_false = []

        if (result[0] == not_tk):
            result = lex()
            grammi = result[2]
            if (result[0] == aristeri_agkyli_tk):
                result = lex()
                grammi = result[2]
                true_false_lists = condition()
                if (result[0] == deksia_agkyli_tk):
                    result = lex()
                    grammi = result[2]

                    # P1
                    R_true = true_false_lists[1]
                    R_false = true_false_lists[0]

                    return R_true, R_false

                else:
                    print("Leipei i deksia agkyli ']', GRAMMI: ", grammi)
                    exit(-1)
            else:
                print("Leipei i aristeri agkyli '[', GRAMMI: ", grammi)
                exit(-1)

        elif (result[0] == aristeri_agkyli_tk):
            result = lex()
            grammi = result[2]
            true_false_lists = condition()
            if (result[0] == deksia_agkyli_tk):
                result = lex()
                grammi = result[2]

                # P1
                R_true = true_false_lists[0]
                R_false = true_false_lists[1]

                return R_true, R_false

            else:
                print("Leipei i deksia agkyli ']', GRAMMI: ", grammi)
                exit(-1)
        else:
            Eplace1 = expression()
            relop = relational_oper()
            Eplace2 = expression()

            # P1
            R_true = makeList(nextQuad())
            genQuad(relop, Eplace1, Eplace2, '_')
            R_false = makeList(nextQuad())
            genQuad('jump', '_', '_', '_')

        return R_true, R_false

    def expression():
        global result

        optional_sign()
        T1_place = term()
        while (result[0] == sin_tk or result[0] == meion_tk):
            sin_plin = add_oper()
            T2_place = term()

            # P1
            w = newTemp()
            genQuad(sin_plin, T1_place, T2_place, w)
            T1_place = w

        # P2
        E_place = T1_place
        return E_place

    def term():
        global result

        F1_place = factor()
        while (result[0] == epi_tk or result[0] == dia_tk):
            epi_dia = mul_oper()
            F2_place = factor()

            # P1
            w = newTemp()
            genQuad(epi_dia, F1_place, F2_place, w)
            F1_place = w

        # P2
        T_place = F1_place

        return T_place

    def factor():
        global result
        global grammi

        if (result[0] == noumero_tk):
            F_place = result[1]
            result = lex()
            grammi = result[2]
            return F_place

        elif (result[0] == aristeri_parenthesi_tk):
            result = lex()
            grammi = result[2]
            E_place = expression()

            # P1
            F_place = E_place
            if (result[0] == deksia_parenthesi_tk):
                result = lex()
                grammi = result[2]
                return F_place

            else:
                print("Leipei i deksia parenthesi ')', GRAMMI: ", grammi)
                exit(-1)

        elif (result[0] == id_tk):
            # P2
            F_place = result[1]


            result = lex()
            grammi = result[2]

            idtail(F_place)

            return F_place
        else:
            print("Leipei stathera, ekfrasi i metavliti, GRAMMI: ", grammi)
            exit(-1)

    def idtail(id_name):
        global result
        global isFunction

        if (result[0] == aristeri_parenthesi_tk):
            isFunction = 1
            actualpars(1, id_name)

        return

    def relational_oper():
        global result
        global grammi

        rel_oper = ''

        if (result[0] == ison_tk):
            rel_oper = result[1]
            result = lex()
            grammi = result[2]
        elif (result[0] == mikrotero_iso_tk):
            rel_oper = result[1]
            result = lex()
            grammi = result[2]
        elif (result[0] == megalytero_iso_tk):
            rel_oper = result[1]
            result = lex()
            grammi = result[2]
        elif (result[0] == megalytero_tk):
            rel_oper = result[1]
            result = lex()
            grammi = result[2]
        elif (result[0] == mikrotero_tk):
            rel_oper = result[1]
            result = lex()
            grammi = result[2]

        elif (result[0] == diaforo_tk):
            rel_oper = result[1]
            result = lex()
            grammi = result[2]
        else:
            print("Leipei telestis sysxetisis, diathesimoi: ['=', '<=', '>=', '>', '<', '<>'], GRAMMI: ", grammi)
            exit(-1)

        return rel_oper

    def add_oper():
        global result
        global grammi

        sin_plin = ''

        if (result[0] == sin_tk):
            sin_plin = result[1]
            result = lex()
            grammi = result[2]
        elif (result[0] == meion_tk):
            sin_plin = result[1]
            result = lex()
            grammi = result[2]

        return sin_plin

    def mul_oper():
        global result
        global grammi

        epi_dia = ''

        if (result[0] == epi_tk):
            epi_dia = result[1]
            result = lex()
            grammi = result[2]
        elif (result[0] == dia_tk):
            epi_dia = '/'
            result = lex()
            grammi = result[2]
        else:
            print("Leipei '*' i '/', GRAMMI: ", grammi)
            exit(-1)

        return epi_dia

    def optional_sign():
        global result

        add_oper()

        return

    program()

    return




# Grafei ti lista me tis tetrades sto arxeio quads.int
def write_to_int_file():

    int_fd = open('quads.int', 'w')

    for quad in quads_list:
        int_fd.write(str(quad[0]) + ': ' + str(quad[1]) + ', ' + str(quad[2]) + ', ' + str(quad[3]) + ', ' + str(quad[4]) + '\n')

    int_fd.close()


# Grafei tis dilwseis metavlitwn sto arxeio C



def write_to_c_file(c_fd):
    global temp_list


    # An i temp_list den einai keni
    if temp_list:
        c_fd.write("int ")


    for i in range(len(temp_list)):
        c_fd.write(temp_list[i])
        if(len(temp_list) == i+1):
            c_fd.write(";\n\n\t")
        else:
            c_fd.write(',')


    for i in range(len(quads_list)):
        if(quads_list[i][1] == 'begin_block'):
            c_fd.write("L_" + str(i + 1) + ":\n\t")
        elif(quads_list[i][1] == ":="):
            c_fd.write("L_" + str(i+1) + ': '+ quads_list[i][4] + '=' + quads_list[i][2] + ";\n\t")
        elif(quads_list[i][1] == '+'):
            c_fd.write("L_" + str(i+1) + ': ' + quads_list[i][4] + '=' + quads_list[i][2] + '+' + quads_list[i][3] + ";\n\t")
        elif(quads_list[i][1] == '-'):
            c_fd.write("L_" + str(i + 1) + ': ' + quads_list[i][4] + '=' + quads_list[i][2] + '-' + quads_list[i][3]+";\n\t")
        elif(quads_list[i][1] == '*'):
            c_fd.write("L_" + str(i + 1) + ': ' + quads_list[i][4] + '=' + quads_list[i][2] + '*' + quads_list[i][3]+";\n\t")
        elif(quads_list[i][1] == '/'):
            c_fd.write("L_" + str(i + 1) + ': ' + quads_list[i][4] + '=' + quads_list[i][2] + '/' + quads_list[i][3]+";\n\t")
        elif(quads_list[i][1] == "jump"):
            c_fd.write("L_" + str(i + 1) + ': ' + "goto L_" + str(quads_list[i][4]) + ";\n\t")
        elif(quads_list[i][1] == "<"):
            c_fd.write("L_" + str(i+1) + ': ' + "if ("+quads_list[i][2] + '<' + quads_list[i][3] + ") goto L_" + str(quads_list[i][4]) + ";\n\t")
        elif(quads_list[i][1] == ">"):
            c_fd.write("L_" + str(i + 1) + ': ' + "if (" +quads_list[i][2] + '>' + quads_list[i][3] + ") goto L_" + str(quads_list[i][4]) + ";\n\t")
        elif(quads_list[i][1] == "<="):
            c_fd.write("L_" + str(i + 1) + ': ' + "if (" + quads_list[i][2] + "<=" + quads_list[i][3] + ") goto L_" + str(quads_list[i][4]) + ";\n\t")
        elif(quads_list[i][1] == ">="):
            c_fd.write("L_" + str(i + 1) + ': ' + "if (" + quads_list[i][2] + ">=" + quads_list[i][3] + ") goto L_" + str(quads_list[i][4]) + ";\n\t")
        elif(quads_list[i][1] == "<>"):
            c_fd.write("L_" + str(i + 1) + ': ' + "if (" + str(quads_list[i][2]) + "!=" + str(quads_list[i][3]) + ") goto L_" + str(quads_list[i][4]) + ";\n\t")
        elif(quads_list[i][1] == "="):
            c_fd.write("L_" + str(i + 1) + ': ' + "if (" + quads_list[i][2] + "==" + quads_list[i][3] + ") goto L_" + str(quads_list[i][4]) + ";\n\t")
        elif(quads_list[i][1] == "out"):
            c_fd.write("L_" + str(i + 1) + ': ' + "printf(\"" + quads_list[i][2] + " = %d \", " + quads_list[i][2] + ");\n\t")
        elif(quads_list[i][1] == 'halt'):
            c_fd.write("L_" + str(i + 1) + ": {}\n\t")


    c_fd.write('\n}')
    c_fd.close()



# Typwnei ti lista me tis tetrades
def print_quads_list():
    for i in range(len(quads_list)):
        print(str(quads_list[i][0]) + ': ' + str(quads_list[i][1]) + ', ' + str(quads_list[i][2]) + ', ' +
              str(quads_list[i][3]) + ', ' + str(quads_list[i][4]))


# Anoigei to arxeio c
c_fd = open('file_in_C.c', 'w')
c_fd.write("int main()\n")
c_fd.write('{\n')

syntaktiki_analysi(c_fd)
#print("Oloklirwthike epityxws i lektiki kai syntaktiki analysi\n")

write_to_int_file()
write_to_c_file(c_fd)


#print_quads_list()
