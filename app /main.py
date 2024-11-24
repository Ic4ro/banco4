from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    def menu():
        while True:  # Loop para manter o menu ativo
            print("\n === SENAI SOLUTION === ")
            print("1 - Adicionar usuário")
            print("2 - Pesquisar um usuário")
            print("3 - Atualizar dados de um usuário")
            print("4 - Excluir um usuário")
            print("5 - Exibir todos os usuários cadastrados")
            print("0 - Sair")
            
            try:
                opcao = int(input("\nEscolha a opção desejada: "))
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")
                continue
            
            match opcao:
                case 1:
                    service.criar_usuario()
                case 2:
                    service.pesquisar_usuario()
                case 3:
                    service.atualizar_usuario()
                case 4:
                    service.deletar_usuario()
                case 5:
                    print("\nListando usuários cadastrados: ")
                    usuarios = service.listar_todos_usuarios()
                    for usuario in usuarios:
                        print(f"{usuario.id} - {usuario.nome} - {usuario.email}")
                case 0:
                    print("Encerrando programa\n")
                    print("Programa Finalizado!")
                    break  # Encerra o loop e, portanto, o programa
                case _:
                    print("Opção inválida! Por favor, tente novamente uma opção válida.")

    menu()

if __name__ == "__main__":
    main()