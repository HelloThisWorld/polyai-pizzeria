import sys

from service.param_service import ParamService


def _handle_arg():
    is_calculated = 'New'
    params = list()
    args = sys.argv[1:]
    if not args:
        for line in sys.stdin:
            _handle_line(line=line, is_calculated=is_calculated, params=params)
    else:
        file = args[0]
        fh = open(file, 'r')
        for line in fh:
            params.append(line.strip())

        ParamService.resolve_params(params)


def _handle_line(line, is_calculated, params):
    if line is not '\n' and is_calculated is 'New':
        params.append(line.strip())

    if line is '\n':
        ParamService.resolve_params(params)
        is_calculated = 'Done'

    if is_calculated is 'Done':
        quit()


if __name__ == '__main__':
    _handle_arg()
