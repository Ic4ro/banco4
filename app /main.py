from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    def menu():
        print("======== SENAI SOLUTION =========")
        print("BEM VINDO!\n")
        print(f"
              \n1 - Adicionar usuário 
              \n2 - Pesquisar um usuário 
              \n3 - Atualizar dados de um usuário
              \n4 - Excluir um usuário 
              \n5 - Exibir todos os usuários cadastrados 
              \n0 - Sair)")
        
        try:
            opcao = int(input("\nSelecione a opção desejada: "))
        except ValueError:
            print("Opção inválida!! Por favor, tente um número inteiro.")
            return 

        match opcao:
            case 1:
                return service.criar_usuario()
            case 2:
                return service.pesquisar_usuario()
            case 3:
                return service.atualizar_usuario()
            case 4: 
                return service.deletar_usuario()
            case 5: 
                print("\nListando usuários cadastrados: ")
                usuarios = service.listar_todos_usuarios()

                for usuario in usuarios:
                    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")
                return  
            case 0:
                print("Encerrando programa\n")
                print("Programa Finalizado!")
                return  
            case _:
                print("Opção inválida! Por favor, tente novamente uma opção válida.")


    menu()

if __name__ == "__main__":
        main()