from .base import *

if (MODE == 'dev'):
    print('Running with `development` settings.')
    from .dev import *
elif (MODE == 'stage'):
    print('Running with `staging` settings.')
    from .stage import *
else:
    print('Running with `production` settings.')
    from .prod import *
