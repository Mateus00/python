from Produto import ProdutoEstoque, ProdutoVenda
from Venda import Venda

def pergunta(mensagem, tipo=int):
        while True:
            try:
                resp = input(mensagem)
                return tipo(resp)
            except ValueError:
                print("Valor Inválido, tente novamente.")
                
def confirma(mensagem, resposta):
    resp = input(mensagem).strip()
    if resposta.lower() == resp.lower():
        return True
    return False

class Caixa():
    def __init__(self):
        self._produtos = {}
        self._vendas = []
        
    @classmethod
    def menu(self):
        print()
        print('********************************')
        print('* CAIXA *')
        print('********************************')
        print('(C) Cadastrar/atualizar produto ')
        print('(E) Entrada de estoque ')
        print('(V) Vender ')
        print('(R) Relatório de vendas ')
        print('(S) Sair ')
        print('*****************************')
        escolha = input('Informe sua opção: ').upper()
        return escolha
    
    def busca_produto(self):
        if len(self._produtos) == 0:
            print("Nenhum produto cadastrado")
            return None
        print('\nProdutos:')
        for cod, produto in self._produtos.items():
            print(cod, ": ", produto)
        codigo = pergunta('Código do produto: ')
        if codigo in self._produtos:
            return self._produtos[codigo]
        print('Produto não encontrado!')
        return None
    
    @classmethod
    def dados_produto(cls):
        descricao = input('Descrição: ')
        preco = pergunta('Preço: ', float)
        return descricao, preco
    
    def cadastro_produto(self):
        produto = self.busca_produto()
        if produto is not None:
            print('Produto cadastrado:', produto)
            if confirma('Alterar? (S/N) ', 'S'):
                descricao, preco = self.dados_produto()
                produto.descricao = descricao
                produto.preco = preco
        else:
            if confirma('Incluir? (S/N) ', 'S'):
                descricao, preco = self.dados_produto()
                produto = ProdutoEstoque(descricao, preco)
                codigo = len(self._produtos)
                self._produtos[codigo] = produto
                
    def entrada_estoque(self):
        produto = self.busca_produto()
        if produto is not None:
            quantidade = pergunta('Quantidade de entrada: ', float)
            produto.entrada(quantidade)
            
    def venda(self):
        print('Venda')
        venda = Venda()
        while True:
            produto = self.busca_produto()
            if produto is not None:
                quantidade = pergunta('Quantidade vendida: ', float)
                if produto.saida(quantidade):
                    produto_venda = ProdutoVenda(produto.descricao, produto.preco, quantidade)
                    venda.adiciona_produto(produto_venda)
            print(venda)
            if confirma('Adicionar mais produtos? (S/N) ', 'N'):
                break
        if venda.numero_produtos > 0:
            self._vendas.append(venda)
            
    def relatorio_vendas(self):
        if len(self._vendas) == 0:
            print('Nenhuma venda encontrada!')
            return
        total_geral = 0
        for cont, venda in enumerate(self._vendas):
            print('\nVenda', cont)
            print(venda)
            total_geral += venda.total
        print('TOTAL GERAL:', total_geral)
        input('Pressine ENTER para voltar')

    def iniciar(self):
        while True:
            escolha = self.menu()
            if escolha == 'C':
                self.cadastro_produto()
            elif escolha == 'E':
                self.entrada_estoque()
            elif escolha == 'V':
                self.venda()
            elif escolha == 'R':
                self.relatorio_vendas()
            elif escolha == 'S':
                break
    
if __name__ == '__main__':
    Caixa().iniciar()
