import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def mirrormirror(x, y):
    # returns a list with results of 
    # 1. simple equality check
    # 2. identity check
    # 3. type equality check
    # 4. type identity check
    ret = []
    logging.debug(f'#######comparing {x} and {y}#######')
    logging.debug(f'simple equality check {x == y}')
    ret.append(x == y)
    logging.debug(f'identity check {x is y}')
    assert (x is y) == (id(x) == id(y)), "Identity check failed"
    ret.append(x is y)
    logging.debug(f'type check {type(x) == type(y)}')
    ret.append(type(x) == type(y))
    logging.debug(f'type identity check {type(x) is type(y)}')
    ret.append(type(x) is type(y))
    return ret
