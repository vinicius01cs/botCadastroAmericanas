from random import randint
from selenium import webdriver
import time

class americanas_bot:
    def __init__(self):
        self.nome = ""
        self.cod_cpf = ""
        self.nascimento = ""
        self.telefone = ""
        self.end_email= ""
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-BR')
        #self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')

    def web_scraping(self):
        self.driver.get('https://www.4devs.com.br/gerador_de_pessoas')
        self.driver.find_element_by_xpath('//*[@id="app-wrapper"]/div[2]/div[2]/div[4]/div[1]/div[3]/label/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="bt_gerar_pessoa"]').click()
        time.sleep(1)
        self.nome = self.driver.find_element_by_xpath('//*[@id="nome"]/span[1]').text
        self.cod_cpf = self.driver.find_element_by_xpath('//*[@id="cpf"]').text
        self.nascimento = self.driver.find_element_by_xpath('//*[@id="data_nasc"]').text
        self.end_email = self.driver.find_element_by_xpath('//*[@id="email"]').text
        self.telefone = self.driver.find_element_by_xpath('//*[@id="celular"]').text
        print(self.nome, self.cod_cpf, self.nascimento, self.end_email, self.telefone)
        self.tratar_email(self.end_email)

    def tratar_email(self, end_email):
        email = end_email
        numero = randint(1,1000)
        indice_dominio = email.find('@')
        domino_email = "@outlook.com"
        email_base = email[:indice_dominio]
        email_base = email_base[0:7] + str(numero)
        email_final = str(email_base) + domino_email
        self.end_email = email_final

    def cadastrar_americanas(self):
        self.driver.get('https://cliente.americanas.com.br/simple-login/cadastro/pf?next=https%3A%2F%2Fwww.americanas.com.br%2Fhotsite%2Fapp%3Faf_adset%3D1869%26shortlink%3Dae2bc25a%26pid%3Dlasa_downloads_loja%26c%3DLASA%2520-%2520Downloads%2520por%2520Loja%26is_retargeting%3Dtrue')
        campo_nome = self.driver.find_element_by_xpath('//*[@id="input-border"]/input')
        campo_nome.click()
        campo_nome.send_keys(self.nome)
        time.sleep(3)
        campo_sexo = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[2]/div[2]/label[3]")
        campo_sexo.click()
        time.sleep(3)
        campo_data = self.driver.find_element_by_name('birthDate')
        campo_data.click()
        campo_data.send_keys(self.nascimento)
        time.sleep(3)
        campo_cpf = self.driver.find_element_by_name('cpf')
        campo_cpf.click()
        campo_cpf.send_keys(self.cod_cpf)
        time.sleep(3)
        campo_telefone = self.driver.find_element_by_name('phone')
        campo_telefone.click()
        campo_telefone.send_keys(self.telefone)
        time.sleep(3)
        campo_email = self.driver.find_element_by_name('email')
        campo_email.click()
        campo_email.send_keys(self.end_email)
        time.sleep(3)
        campo_senha = self.driver.find_element_by_name('password')
        campo_senha.click()
        campo_senha.send_keys("741963Wesley!")

bot = americanas_bot()
bot.web_scraping()
bot.cadastrar_americanas()