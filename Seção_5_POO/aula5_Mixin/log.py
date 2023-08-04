# Abstração
# A classe Log é uma abstração. Eu não quero que use ela diretamente. 
# Python já tem classes abstratas(ABC). Aqui é um exercício para entendimento

# NotImplementedError
# Aqui nesse exemplo está sendo usada uma classe que não era p ser usada.
# Está usando a superclass quando é para usar a subclass - LogFileMixin(Log)

# Classes com nome Mixin:
# É para adicionar funcionalidades na sua herança múltipla ou seja, vai adicionar
# coisas dentro das outras classes que herdarão. Isso não fará parte da família
# do objeto.

# OBS: a assinatura do método: -->  def log(self, msg):
# O nome do método, parâmetros, tipos e retorno é a aassinatura do método.
# Ao alterar nome, parâmetros e retorno quebra um princípio da programação - LSP

# Esse é uma padrão de projeto chamado Template Method.
# Significa um método que não está implementado 

# LogFileMixin é um Log pois herdou tudo de Log()
# LogPrintMixin também herda de Log.

# O Log é um tipo: Tipo LOG() que engloba LogFileMixin e LogPrintMixin.
# Esses tiipos vão pdoer se comportar de maneiras diferentes dentro das funções
# somente chamando Log. Isso é chamado Polimorfismo 

# O método log_error será repassado para as classes abaixo.
# Caso tenha mutias classes de LogFileMixin não vai precisar implementar em todas
# o método log_error posi todas vão herdas.


# A class Log é um contrato para fazer a mediação entre as outras classes
# Esse é o método, o nome e a assinatura. O copor do método define em quem herdar.

from pathlib import Path

# Pegando caminho absoluto: __file__ é o caminho do módulo
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no Log:', msg_formatada)
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    # l = Log() - assim não funciona. Precisa ter outra classe para herdar de Log.
    # l.log('Teste de log') não da mais para chamar pois está protegida _log()
    
    lp = LogPrintMixin()
    lp.log_error('Testando Log Error')
    lp.log_success('Testando Log Success')

    print(LOG_FILE) # c:\Python_intermediario\Seção_5_POO\aula5_Mixin\log.txt

    lf = LogFileMixin()
    lf.log_error('Testando Log Error')
    lf.log_success('Testando Log Success')
