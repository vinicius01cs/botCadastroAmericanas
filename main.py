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
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

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

    def cadastrar_americanas(self):
        #<svg viewBox="0 0 20 20" class="sc-hjGYWY lmIfJs"><circle cx="10" cy="10" r="9" class="sc-fIoroj YbkeR"></circle><path d="M10,7 C8.34314575,7 7,8.34314575 7,10 C7,11.6568542 8.34314575,13 10,13 C11.6568542,13 13,11.6568542 13,10 C13,8.34314575 11.6568542,7 10,7 Z" class="sc-gUQueJ eMhYQW inner"></path><path d="M10,1 L10,1 L10,1 C14.9705627,1 19,5.02943725 19,10 L19,10 L19,10 C19,14.9705627 14.9705627,19 10,19 L10,19 L10,19 C5.02943725,19 1,14.9705627 1,10 L1,10 L1,10 C1,5.02943725 5.02943725,1 10,1 L10,1 Z" class="sc-fXeWgy cJudXV outer"></path></svg>
        #<input data-cy="formField__name" type="text" required="" name="name" placeholder="" class="inputcomponent__InputFieldInput-x88sc3-3 hzTWms" value="">
        self.driver.get('https://cliente.americanas.com.br/minha-conta/cadastro?next=https%3A%2F%2Fwww.americanas.com.br%2F')
        campo_nome = self.driver.find_element_by_xpath("//*[@id='input-border']/input")
        campo_nome.click()
        campo_nome.send_keys(self.nome)
        time.sleep(1)
        campo_sexo = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[2]/div[2]/label[3]")
        campo_sexo.click()
        time.sleep(1)
        campo_data = self.driver.find_element_by_name('birthDate')
        campo_data.click()
        campo_data.send_keys(self.nascimento)
        time.sleep(1)
        campo_cpf = self.driver.find_element_by_name('cpf')
        campo_cpf.click()
        campo_cpf.send_keys(self.cod_cpf)
        time.sleep(1)
        campo_telefone = self.driver.find_element_by_name('phone')
        campo_telefone.click()
        campo_telefone.send_keys(self.telefone)
        time.sleep(1)
        campo_email = self.driver.find_element_by_name('email')
        campo_email.click()
        campo_email.send_keys(self.end_email)
        time.sleep(1)
        campo_senha = self.driver.find_element_by_name('password')
        campo_senha.click()
        campo_senha.send_keys("741963Wesley!")

bot = americanas_bot()
bot.web_scraping()
bot.cadastrar_americanas()
