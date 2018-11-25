import sys

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

# TODO untested
def padovan(n):
    print('calculating padovan number for n = {}'.format(n))
    assert(type(0) == type(n))
    assert(n >= 0)
    rvs = [1, 1, 1]
    if n >= 0 and n < 3:
        print('request for base case ({b} >= 0 and {b} < 3), returning {v}'.format(**{
            "b": n,
            "v": rvs[n],
        }))
        return rvs[n]
    k = n
    while k >= 3:
        print('top of loop')
        print('  k = {}'.format(k))
        print('  len(rvs) = {}'.format(len(rvs)))
        print('  rvs = {}'.format(rvs))
        rvs.append(rvs[len(rvs)-2] + rvs[len(rvs)-3])
        k -= 1
        print('bottom of loop')
        print('  k = {}'.format(k))
        print('  len(rvs) = {}'.format(len(rvs)))
        print('  rvs = {}'.format(rvs))
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
            reason = 'error: no subcommand provided'
        if numargs == 1:
            reason = 'error: no value given for indexing into sequence'
        if numargs > 2:
            reason = 'error: too many arguments provided'
        return (not ok, reason)
    else:
        scmd = sys.argv[1]
        acceptable_subcommands = [
            'padovan',
            'catalan',
            'fibonacci',
        ]
        if scmd.lower() not in acceptable_subcommands:
            reason = 'error: unrecognized subcommand'
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
        print('error: index value is not an integer')
        print usage()
        sys.exit(1)

    return sys.argv[1], qty

# TODO untested
def _unimplemented_func_err(_):
    print('fatal: the requested subcommand has not been implemented')
    sys.exit(2)

# TODO untested
def run_seqel():
    if __name__ == "__main__":
        print("seqel 0.1.0; running in debug mode")
        for i, arg in enumerate(sys.argv):
            print("  arg in pos {}: {}".format(i, arg))

        ok, reason = validate_argv()
        if not ok:
            print reason
            print usage()
            sys.exit(1)

        scmd, qty = process_argv()

        # Each command in the lookup table is unary.
        # Taking the number to index into the given sequence.
        scmd_vtable = {
            'padovan': padovan,
            'catalan': _unimplemented_func_err,
            'fibonacci': _unimplemented_func_err,
        }

        scmd_func = scmd_vtable[scmd]
        assert(type(lambda x: x) == type(scmd_func))

        seq_el = scmd_func(qty)
        print(seq_el)
    else:
        print('error: this was imported as a library, which is unintended')
        print('       please rerun this program directly')

run_seqel()
