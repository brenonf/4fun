
import xlrd
book = xlrd.open_workbook("corretagem1.xls")
print("Número de abas: ", book.nsheets)
print("Nomes das Planilhas:", book.sheet_names())
sh = book.sheet_by_index(0)
print(sh.name, sh.nrows, sh.ncols)
# Nao esquecer: print("Valor da célula D30 é ", sh.cell_value(rowx=29, colx=3))
for rx in range(sh.nrows):
    print(sh.row(rx))


total=[]
win =[]
qwin = 0
wdo=[]
qwdo=0
ind=[]
qind=0
dol=[]
qdol=0
papel=[]
menor = 0
maior = 0
saldo = 0

lin =sh.nrows
col =sh.ncols

for i in range(lin-1,1,-1):
    if sh.cell_value(rowx=i,colx=1)[0:3] == "WIN":
            #print(qwin)
            if sh.cell_value(rowx=i,colx=0) == "C":
                qwin += sh.cell_value(rowx=i,colx=3)
                result = (sh.cell_value(rowx=(i-1),colx=4) - sh.cell_value(rowx=i,colx=4))*qwin*0.2
                #result = (sh.cell_value(rowx=(i-1),colx=4)*(sh.cell_value(rowx=(i-1),colx=3)) - sh.cell_value(rowx=i,colx=4)*sh.cell_value(rowx=(i-1),colx=3))
            else:
                qwin -= sh.cell_value(rowx=i,colx=3)
                result = (sh.cell_value(rowx=i,colx=4) - sh.cell_value(rowx=(i-1),colx=4))*abs(qwin)*0.2
            if qwin !=0:
                win.append(result)
                saldo += result
                if saldo > maior:
                    maior = saldo
                if saldo < menor:
                    menor = saldo
            result=0

    if sh.cell_value(rowx=i,colx=1)[0:3] == "WDO":
            #print(qwdo)
            if sh.cell_value(rowx=i,colx=0) == "C":
                qwdo += sh.cell_value(rowx=i,colx=3)
                result = (sh.cell_value(rowx=(i-1),colx=4) - sh.cell_value(rowx=i,colx=4))*qwdo*10
                #result = (sh.cell_value(rowx=(i-1),colx=4)*(sh.cell_value(rowx=(i-1),colx=3)) - sh.cell_value(rowx=i,colx=4)*sh.cell_value(rowx=(i-1),colx=3))
            else:
                qwdo -= sh.cell_value(rowx=i,colx=3)
                result = (sh.cell_value(rowx=i,colx=4) - sh.cell_value(rowx=(i-1),colx=4))*abs(qwdo)*10
            if qwdo !=0:
                wdo.append(result)
                saldo+= result
                if saldo > maior:
                    maior = saldo
                if saldo < menor:
                    menor = saldo
            result=0

print()
print()
print()
#soma
a=sum(win)
b=sum(wdo)
total.append(a+b)
print(" O resultado foi: {}".format(total))
print(" O menor saldo atingido foi: {}".format(menor))
print(" O maior saldo atingido foi: {}".format(maior))
