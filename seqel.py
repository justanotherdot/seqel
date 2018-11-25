import sys
import logging

# TODO just needs to be a constant.
# Python doesn't support CAFs.
# But _might_ inline funcs it knows to return as constants.
def usage():
    return """
seqel 0.0.1
Print numbers from integer sequences

USAGE:
    seqel [FLAGS] <SUBCOMMAND> NTH

FLAGS:
    -e, --entire     Print the entire sequence from initial values to the given NTH element
    --log-level=LVL  Run seqel with the given log level LVL. Defaults to `info'.

SUBCOMMANDS:
    padovan       P(n) = P(n-2)+P(n-3)
    fibonacci     F(n) = F(n-1)+F(n-2)
    catalan       C(n) = (2n)!/(n!(n+1)!)
""".strip()

# TODO untested
def factorial(n):
    assert(n > 0)
    k = n
    rv = 1
    while k != 1:
        rv *= k
        k -= 1
    return rv

def fibonacci(n):
    """
    Return the `n'th element of the fibonacci sequence.
    `n' must be an whole number.
    """
    logging.info('calculating fibonacci number for n = {}'.format(n))
    assert(type(0) == type(n))
    assert(n >= 0)
    rvs = [1, 1]
    if n >= 0 and n < 2:
        logging.debug('request for base case ({b} >= 0 and {b} < 2), returning {v}'.format(**{
            "b": n,
            "v": rvs[n],
        }))
        return rvs[n]
    k = n
    while k >= 2:
        logging.debug('top of loop')
        logging.debug('  k = {}'.format(k))
        logging.debug('  len(rvs) = {}'.format(len(rvs)))
        logging.debug('  rvs = {}'.format(rvs))
        rvs.append(rvs[len(rvs)-1] + rvs[len(rvs)-2])
        k -= 1
        logging.debug('bottom of loop')
        logging.debug('  k = {}'.format(k))
        logging.debug('  len(rvs) = {}'.format(len(rvs)))
        logging.debug('  rvs = {}'.format(rvs))
    return rvs[n]

# TODO untested
def padovan(n):
    """
    Return the `n'th element of the padovan sequence.
    `n' must be an whole number.
    """
    logging.info('calculating padovan number for n = {}'.format(n))
    assert(type(0) == type(n))
    assert(n >= 0)
    rvs = [1, 1, 1]
    if n >= 0 and n < 3:
        logging.debug('request for base case ({b} >= 0 and {b} < 3), returning {v}'.format(**{
            "b": n,
            "v": rvs[n],
        }))
        return rvs[n]
    k = n
    while k >= 3:
        logging.debug('top of loop')
        logging.debug('  k = {}'.format(k))
        logging.debug('  len(rvs) = {}'.format(len(rvs)))
        logging.debug('  rvs = {}'.format(rvs))
        rvs.append(rvs[len(rvs)-2] + rvs[len(rvs)-3])
        k -= 1
        logging.debug('bottom of loop')
        logging.debug('  k = {}'.format(k))
        logging.debug('  len(rvs) = {}'.format(len(rvs)))
        logging.debug('  rvs = {}'.format(rvs))
    return rvs[n]

# TODO untested
def validate_argv():
    """
    Validate sys.argv
    """
    numargs = len(sys.argv)-1
    ok = True
    reason = None
    if numargs != 2:
        if numargs == 0:
            reason = 'no subcommand provided'
        if numargs == 1:
            reason = 'no value given for indexing into sequence'
        if numargs > 2:
            reason = 'too many arguments provided'
        return (not ok, reason)
    else:
        scmd = sys.argv[1]
        acceptable_subcommands = [
            'padovan',
            'catalan',
            'fibonacci',
        ]
        if scmd.lower() not in acceptable_subcommands:
            reason = 'unrecognized subcommand'
            return (not ok, reason)
    return ok, reason

# TODO untested
def process_argv():
    """
    Parse argv into appropriate types
    """
    qty = sys.argv[2]
    try:
        qty = int(qty)
    except:
        logging.error('index value is not an integer')
        logging.error(usage())
        sys.exit(1)

    return sys.argv[1], qty

# TODO untested
def _unimplemented_func_err(_):
    logger.critical('the requested subcommand has not been implemented')
    sys.exit(2)

# TODO untested
def run_seqel():
    logger = logging.getLogger()
    logger.setLevel('NOTSET')
    if __name__ == "__main__":
        logging.debug("seqel 0.1.0; running in debug mode")
        for i, arg in enumerate(sys.argv):
            logging.debug("  arg in pos {}: {}".format(i, arg))

        ok, reason = validate_argv()
        if not ok:
            logging.error(reason)
            logging.error(usage())
            sys.exit(1)

        scmd, qty = process_argv()

        # Each command in the lookup table is unary.
        # Taking the number to index into the given sequence.
        scmd_vtable = {
            'padovan': padovan,
            'catalan': _unimplemented_func_err,
            'fibonacci': fibonacci,
        }

        scmd_func = scmd_vtable[scmd]
        assert(type(lambda x: x) == type(scmd_func))

        seq_el = scmd_func(qty)
        logging.info(seq_el)
    else:
        logging.error('this was imported as a library, which is unintended')
        logging.error('       please rerun this program directly')

run_seqel()
