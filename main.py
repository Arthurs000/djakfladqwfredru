# 2º ano Informática Matutino - Arthur Sales, Camila Cuéllar e Maria Rita Nogueira
# Programação Orientada a Objetos - 4º Bimestre
# Programa de delivery com login de clientes e loop de repetição básico com tratamento de exceção


# criação das classes
class Produto:
    def __init__(self, item, preco):
        self.item = item
        self.preco = preco
        self.produtinho = self.item, "R$:", self.preco


# também instanciando os objetos de produto
buchada = Produto("Marmita de Buchada", 14)
vatapa = Produto("Marmita de Vatapá", 14)
moqueca = Produto("Marmita de Moqueca Baiana", 14)
refrigerante = Produto("Refrigerante 350ml", 3.50)
agua = Produto("Água Mineral 500ml", 2.50)
suco = Produto("Suco de Laranja 400ml", 6.50)


class Pedido:
    def __init__(self):
        self.cliente = []
        self.preco_parcial = []
        self.itens_pedido = []
        self.valor_pedido = 0

    def adicionar_carrinho(self, produtoobj, clienteobj):
        print("=================================================")
        print("        ", clienteobj.nome, ", seu pedido até agora contém:")
        self.itens_pedido.append(produtoobj)
        self.preco_parcial.append(produtoobj.preco)
        listatm = len(self.preco_parcial)
        self.valor_pedido = 0
        for x in range(listatm):
            self.valor_pedido = self.preco_parcial[x] + self.valor_pedido
        for x in range(len(self.itens_pedido)):
            # imprimindo todos os itens de todas as posições da lista
            print("            ", self.itens_pedido[x].item, "R$:", self.itens_pedido[x].preco)
        print("         Valor:", self.valor_pedido)

    def finalizar_pedido(self, resposta):
        if resposta == "1":
            print("             Pedido Fechado")
            for x in range(len(self.itens_pedido)):
                # imprimindo todos os itens de todas as posições da lista
                print("            ", self.itens_pedido[x].item, "R$:", self.itens_pedido[x].preco)
            print("             Valor:", self.valor_pedido)
            print("=================================================")
        if resposta == "2":
            print("Pedido cancelado")
            self.itens_pedido = []
            self.preco_parcial = []
        if resposta == "3":
            self.itens_pedido = []
            self.preco_parcial = []

class Pagamento:
    def __init__(self):
        self.dinheiro = 0
        self.troco = 0

    def emitir_cupom(self, pedidoobj, clienteobj):
        print("-------------------------------------------------")
        print("            🌵RESTAURANTE  MANDACARU🌵")
        print("=================================================")
        print("              Cliente:", clienteobj.nome)

        for x in range(len(pedidoobj.itens_pedido)):
            print("            ", pedidoobj.itens_pedido[x].item, "R$:", pedidoobj.itens_pedido[x].preco)
        print("              Valor: R$", pedidoobj.valor_pedido)
        print("\n              Obrigado pelo pedido!")
        print("-------------------------------------------------")

    def calcular_troco(self, pedidoobj):
        while True:
            self.dinheiro = int(input("        Troco para quanto?"))
            listatm = len(pedidoobj.preco_parcial)
            pedidoobj.valor_pedido = 0
            for x in range(listatm):
                pedidoobj.valor_pedido = pedidoobj.preco_parcial[x] + pedidoobj.valor_pedido
            self.troco = (self.dinheiro - pedidoobj.valor_pedido)
            if self.troco <= 0:
                print("        Valor inválido")
                continue
            else:
                print("        Ok, troco de R$", self.troco)
                break



class Endereco:
    def __init__(self, bairro, rua, num_res):
        self.bairro = bairro
        self.rua = rua
        self.num_res = num_res


class Usuario:
    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.email_login = ""
        self.senha_login = ""
        self.login = None

    # Métodos do usuário
    def logar(self):
        while True:
            self.email_login = input("        E-mail:")
            self.senha_login = input("        Senha:")

            if self.senha_login == self.senha and self.email_login == self.email:
                print("=================================================")
                print("                     Logado")
                self.login = True
                break

            else:
                print("Falha no Login")
                self.login = False
                break


class Cliente(Usuario):

    def __init__(self, nome, email, senha, telefone, cpf, numero_cartao, cvv, validade_cartao, enderecoobj):
        Usuario.__init__(self, nome, email, senha, telefone)
        self.cpf = cpf
        self.endereco = enderecoobj  # objeto
        self.numero_cartao = numero_cartao
        self.cvv = cvv
        self.validade_cartao = validade_cartao
        self.alt = ""

    def alterar_dados(self, enderecoobj):
        while True:
            print("=================================================")
            self.alt = input("          Quais dados deseja alterar?\n        1 - Nome\n        2 - E-mail\n"
                             "        3 - Senha\n        4 - Telefone\n        4 - Endereço\n        6 - CPF\n"
                             "        7 - Cartão\n        8 - Fechar e Sair")
            if self.alt == "1":
                self.nome = input("Insira o novo Nome:")
                continue
            if self.alt == "2":
                self.email = input("Insira o novo E-mail:")
                continue
            if self.alt == "3":
                self.senha = input("insira a nova Senha:")
                continue
            if self.alt == "4":
                self.telefone = input("Insira o novo Telefone:")
                continue
            if self.alt == "5":
                enderecoobj.bairro = input("Insira o novo Bairro:")
                enderecoobj.rua = input("Insira a nova Rua:")
                enderecoobj.num_res = input("Insira o novo Número Nesidencial:")
                continue
            if self.alt == "6":
                self.cpf = input("Insira o novo CPF:")
            if self.alt == "7":
                self.numero_cartao = input("Insira o novo Número do Cartão:")
                self.cvv = input("Insira o novo CVV:")
                self.validade_cartao = input("Insira a nova Validade do Cartão:")
                continue
            if self.alt == "8":
                break

    # Antes, o método cadastrar era simplesmente o construtor. Como o código
    # foi feito apenas para cadastro de clientes, contém um input nessa classe
    def cadastrar_cliente(self):
      while True:
        print("              Insira seus dados")
        try:
          self.nome = input("        Nome:")
          for r in self.nome:
            if r.isalpha()==False:
              if ' ' not in r:
                raise ValueError
        except ValueError:
          print ("Por favor, utilize apenas letras.")
          break
        self.email = input("        E-mail:")
        self.senha = input("        Senha:")
        try:
          self.telefone = input("        Telefone:")
          for r in self.telefone:
            if r.isdigit()==False:
              raise ValueError
          if len(self.telefone) != 9 and len(self.telefone) != 11:
            raise IndexError
        except ValueError:
          print ("Por favor, insira apenas números.")
          break
        except IndexError:
          print("Por favor, insira um número válido")
          break
        self.endereco.bairro = input("        Bairro:")
        self.endereco.rua = input("        Rua:")
        try:
          self.endereco.num_res = input("        Número Residencial:")
          for r in self.endereco.num_res:
            if r.isdigit()==False:
              raise ValueError
            if len(self.endereco.num_res) != 4 and len(self.endereco.num_res) != 3:
              raise IndexError
        except ValueError:
          print ("Por favor, insira apenas números.")
          break  
        except IndexError:
          print ("Por favor, insira um número válido.")
          break
        try:
          self.cpf = input("        CPF:")
          for r in self.cpf:
            if r.isdigit()==False:
              raise ValueError
          if len(self.cpf) != 11:
            raise IndexError
        except ValueError:
          print ("Por favor, insira apenas números.")
          break
        except IndexError:
          print("Por favor, insira um cpf válido")
          break
        print("=================================================")
        print("              🔒Informações Financeiras🔒")
        try:
          self.numero_cartao = input("        Número do Cartão:")
          for r in self.numero_cartao:
            if r.isdigit()==False:
              raise ValueError
          if len(self.numero_cartao) != 16:
            raise IndexError
        except ValueError:
          print("Por favor, insira apenas números.")
          break
        except IndexError:
          print("Por favor, insira um número de cartão válido")
          break          
        try:
          self.cvv = input("        CVV:")
          for r in self.cvv:
            if r.isdigit()==False:
              raise ValueError
          if len(self.cvv) != 3:
            raise IndexError
        except ValueError:
          print("Por favor, insira apenas números.")
          break
        except IndexError:
          print("Por favor, insira um cvv válido.")
          break          
        try:
          self.validade_cartao = input("        Validade do Cartão:")
          for r in self.validade_cartao:
            if r.isdigit()==False:
              raise ValueError
          if len(self.validade_cartao) != 4:
            raise IndexError
        except ValueError:
          print("Por favor, digite apenas números.")
          break
        except IndexError:
          print("Por favor, digite uma data válida.")
          break

    def exibir_cliente(self):
        print("=================================================")
        print("        Seus Dados")
        print("        Nome:", self.nome)
        print("        E-mail:", self.email)
        print("        Senha:", self.senha)
        print("        Telefone:", self.telefone)
        print("        Bairro:", self.endereco.bairro)
        print("        Rua:", self.endereco.rua)
        print("        Número Residencial:", self.endereco.num_res)
        print("        CPF:", self.cpf)
        print("        Número do Cartão:", self.numero_cartao)
        print("        CVV:", self.cvv)
        print("        Validade do Cartão:", self.validade_cartao)

    def confirmar_recebimento(self, resposta_entrega):
        if resposta_entrega == "sim":
            print("        Recebimento Confirmado")
        else:
            print("        Recebimento não Confirmado")



class Funcionario(Usuario):
    def __init__(self, nome, email, senha, telefone, funcao):
        Usuario.__init__(self, nome, email, senha, telefone)
        self.funcao = funcao

    def exibir_funcao(self):
        print("=================================================")
        print("       ", self.nome, "\n        Função:", self.funcao)

    def confirmar_pedido(self):
        print("              O pedido foi aceito")


# Classe Entregador, herança de Funcionário

class Entregador(Funcionario):
    def __init__(self, nome, email, senha, telefone, funcao, cnh, placa_moto):
        Funcionario.__init__(self, nome, email, senha, telefone, funcao)
        self.cnh = cnh
        self.placa = placa_moto

    def exibir_entregador(self):
        print("        CNH:", self.cnh, "\n        Placa da moto:", self.placa)

    def realizar_entrega(self):
        print("              O pedido foi entregue")


# Instanciando usuários e objetos pedido e pagamento
endereco1 = Endereco('', '', '')
cliente1 = Cliente('', '', '', '', '', '', '', '', endereco1)
pedido1 = Pedido()
pagamento1 = Pagamento()
funcionario1 = Funcionario("Carlos", "carlos55@gmail.com", "5434", "8000-8000", "Gerente")
entregador1 = Entregador("Ana", "anagabi32@gmail.com", "4323", "9000-9000", "Entregadora", "00123456789", "AGB8681")

# Começo do loop
while True:

    print("=================================================")
    print("            🌵RESTAURANTE  MANDACARU🌵")
    print("=================================================")
    print("                  O QUE DESEJA?                  ")
    menu = input("        1 - Fazer Cadastro \n        2 - Fazer Login \n        3 - Fechar e Sair\n"
                 "=================================================")
    if menu == "1":
        cliente1.cadastrar_cliente()

    if menu == "2":
        print("              Fazer Login")
        cliente1.logar()
        if cliente1.login is False or None:
            continue
        else:
            while True:
                print("=================================================")
                print("            🌵RESTAURANTE  MANDACARU🌵")
                print("=================================================")
                print("                  O QUE DESEJA?                  ")
                menu2 = input("        1 - Fazer Pedido \n        2 - Alterar Dados\n"
                              "        3 - Consultar Dados\n        4 - Fechar e Sair\n")
                if menu2 == "1":
                    while True:
                        print("=================================================")
                        menu3 = input(
                            "        1 - Marmita de Buchada: R$ 14\n        2 - Marmita de Vatapá: R$ 14\n"
                            "        3 - Marmita de Moqueca Baiana: R$ 14\n        4 - Refrigerante 350ml: R$ 3,50\n"
                            "        5 - Água Mineral 500ml: R$ 2,50\n        6 - Suco de Laranja 400ml: R$ 6,50\n"
                            "=================================================\n"
                            "           Deseja finalizar o pedido?\n"
                            "      7 - Sim      8 - Não      9 - Cancelar")
                        if menu3 == "1":
                            pedido1.adicionar_carrinho(buchada, cliente1)
                        if menu3 == "2":
                            pedido1.adicionar_carrinho(vatapa, cliente1)
                        if menu3 == "3":
                            pedido1.adicionar_carrinho(moqueca, cliente1)
                        if menu3 == "4":
                            pedido1.adicionar_carrinho(refrigerante, cliente1)
                        if menu3 == "5":
                            pedido1.adicionar_carrinho(agua, cliente1)
                        if menu3 == "6":
                            pedido1.adicionar_carrinho(suco, cliente1)
                        if menu3 == "7":
                            print("=================================================")
                            pedido1.finalizar_pedido("1")
                            menu4 = input("        Qual será a forma de pagamento??\n"
                                          "     1 - Dinheiro              2 - Cartão")
                            if menu4 == "1":
                                print("=================================================")
                                pagamento1.calcular_troco(pedido1)
                                print("                   Obrigado!")
                                print("=================================================")
                                funcionario1.confirmar_pedido()
                                entregador1.realizar_entrega()
                                pedido1.finalizar_pedido("3")
                                break
                            if menu4 == "2":
                                print("=================================================")
                                funcionario1.confirmar_pedido()
                                print("=================================================")
                                print("             Seu Cupom Fiscal")
                                pagamento1.emitir_cupom(pedido1, cliente1)
                                entregador1.realizar_entrega()
                                pedido1.finalizar_pedido("3")
                                break
                        if menu3 == "8":
                            continue
                        if menu3 == "9":
                            pedido1.finalizar_pedido("2")
                            break

                if menu2 == "2":
                    cliente1.alterar_dados(endereco1)
                    continue
                if menu2 == "3":
                    print("=================================================")
                    print("             Consultar Dados de:")
                    dads = input("        1 - Meus Dados\n        2 - Dados de Funcionários")
                    if dads == "1":
                        cliente1.exibir_cliente()
                        continue
                    if dads == "2":
                        funcionario1.exibir_funcao()
                        entregador1.exibir_funcao()
                        entregador1.exibir_entregador()
                        continue
                if menu2 == "4":
                    break

    if menu == "3":
        break
