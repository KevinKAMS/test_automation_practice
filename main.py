import unittest
import L001_Login_Correto, L002_Login_Incorreto, L003_Senha_Incorreta, L004_Login_Nao_Informado
import L005_Senha_Nao_Informada, L006_Recuperacao_de_senha, L007_Recuperacao_email_nao_cadastrado, L008_Recuperacao_email_vazio
import C001_Cadastro_Correto, C002_Cadastro_Email_Incorreto, C003_Cadastro_Email_Cadastrado
import C004_Cadastro_Campos_Vazios, C005_Cadastro_Campos_Incorretos

suite = unittest.TestSuite()
suite.addTests(
    [
        L001_Login_Correto.L001(),
        L002_Login_Incorreto.L002(),
        L003_Senha_Incorreta.L003(),
        L004_Login_Nao_Informado.L004(),
        L005_Senha_Nao_Informada.L005(),
        L006_Recuperacao_de_senha.L006(),
        L007_Recuperacao_email_nao_cadastrado.L007(),
        L008_Recuperacao_email_vazio.L008(),
        C001_Cadastro_Correto.C001(),
        C002_Cadastro_Email_Incorreto.C002(),
        C003_Cadastro_Email_Cadastrado.C003(),
        C004_Cadastro_Campos_Vazios.C004(),
        C005_Cadastro_Campos_Incorretos.C005(),
    ]
)
unittest.TextTestRunner().run(suite)
