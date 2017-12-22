import datetime
import string
import random
from datetime import datetime
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def create_session(event, context):
    report_date = datetime.today()
    retvalue=report_date.strftime('%Y%m%d%H%M%S')
    retobj={}
    retobj['session']=retvalue + '.' + id_generator(12, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return retobj


if __name__ == '__main__':
    print(create_session('',''))


