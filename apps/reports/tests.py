from django.test import TestCase

# Create your tests here.
from datetime import datetime
if __name__ == '__main__':
    # print(datetime.now())
    rs=datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    print(rs)