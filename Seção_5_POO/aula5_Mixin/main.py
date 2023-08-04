""" 
As classes de Log não precisa está aqui. Vai colocar Log no Smartphone
from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('Testando Log Error')
lp.log_success('Testando Log Success')

lf = LogFileMixin()
lf.log_error('Testando Log Error')
lf.log_success('Testando Log Success')
"""

from eletronico import Smartphone

samsung_s22 = Smartphone('Samsung S22')
iphone14 = Smartphone('Iphone 14')

samsung_s22.ligar()
iphone14.desligar()
iphone14.ligar()
iphone14.desligar()
