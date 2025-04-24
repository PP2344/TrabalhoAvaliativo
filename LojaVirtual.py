class NumeroInvalidoError(Exception):
    def __init__(self, numero):
        super().__init__(f"Número inválido: {numero}")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, total):
        super().__init__(f"Saldo insufuciente para a compra desejada: Saldo->{saldo} Total->{total}")
    
class CarrinhoVazioError(Exception):
    def __init__(self):
        super().__init__("O carrinho está vazio.")

stock = {"Computador": 1000, "Rato": 60, "Teclado": 40, "Fones": 50}
carrinho = {}
total = 0
saldo = 0

def Menu():
    print("\n1. Visualizar produtos")
    print("2. Adicionar produto ao carrinho")
    print("3. Quantidade existente e valor do carrinho")
    print("4. Adicionar Saldo")
    print("5. Pagar")
    print("0. Sair")

def AdicionarProduto():
    global total
    i = 0
    for produto in stock:
        i += 1
        print(f"{i}.{produto}: {stock[produto]}€")
    try:
        
        prodn = int(input("Produto a adicionar: "))

        if(prodn<=0 or prodn>=4):
            raise NumeroInvalidoError(prodn)

        quantidade = int(input("Quantidade: "))

        if(quantidade<=0):
            raise NumeroInvalidoError(quantidade)

        match prodn:
            case 1: 
                carrinho.update({"Computador" : quantidade})               
                total += (1000*quantidade)                       
            case 2:
                carrinho.update({"Rato" : quantidade})               
                total += (60*quantidade)      
            case 3:
                carrinho.update({"Teclado" : quantidade})               
                total += (40*quantidade)                          
            case 4:
                carrinho.update({"Fones" : quantidade})               
                total += (50*quantidade)
    
    except NumeroInvalidoError as e:
        print(e)

    except TypeError as e:
        print(e)
    
    finally:
        print("\nOperação finalizada")

def AdicionarSaldo():
    global saldo
    try:
        quantia = int(input("Quantia a adicionar: "))
        if(quantia<=0):
            raise NumeroInvalidoError(quantia)
        else:
            saldo += quantia
    except NumeroInvalidoError as e:
        print(e)
    except TypeError as e:
        print("Insira um número")
    
    finally:
        print("\nOperação finalizada")
       
def VisProd():
    global stock
    for produto in stock:
        print(f"{produto}: {stock[produto]}€")

def MostrarQuant():
    global carrinho
    try:
        if(len(carrinho)!=0):
            for produto in carrinho:
                print(f"{produto}: {carrinho[produto]}")
            print(f"\nO total do carrinho é igual a {total}€")
        else:
            raise CarrinhoVazioError
    except CarrinhoVazioError as e:
        print(e)
        print(f"\nO total do carrinho é igual a {total}€")

def Pagar():
    global total
    global saldo
    global carrinho
    try:
        if(len(carrinho)==0):
            raise CarrinhoVazioError
        
        if(total<=saldo):
            saldo -=total
            total = 0
            carrinho.clear()
            print(f"Compra efetuada com sucesso o novo saldo é de {saldo}€")
        else:
            raise SaldoInsuficienteError(saldo, total)
    except SaldoInsuficienteError as e:
        print(e)
    except CarrinhoVazioError as e:
        print("Impossível pagar. "+e)
    finally:
        print("\nOperação finalizada")

while True:
    Menu()
    try:
        op = int(input("\nOpção: "))

        if(op<=5 and op>=0):
            match op:
                case 0: 
                    exit()                     
                case 1:
                    VisProd()
                case 2:
                    AdicionarProduto()                          
                case 3:
                    MostrarQuant()
                case 4:
                    AdicionarSaldo()
                case 5:
                    Pagar()
        else:
            raise NumeroInvalidoError(op)
    except NumeroInvalidoError as e:
        print(e)
    except TypeError as e:
        print("Opção inválida")
    except ValueError as e:
        print("Opção inválida")
    finally:
        print("\nOperação finalizada")
                

        
