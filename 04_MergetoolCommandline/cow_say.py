import cmd
import shlex
import readline
from cowsay import list_cows, THOUGHT_OPTIONS, Bubble, cowsay, cowthink, make_bubble

class CowShell(cmd.Cmd):
    intro = 'This is cowsay shell. Program works the same way as the original cowsay program \
            \nType help or ? to list commands.\n'
    prompt = '(cowsay) '

    @staticmethod
    def __parse_arg(arg):
        params = {
            'message': None,
            'cow': 'default',
            'eyes': 'oo',
            'tongue': '  '
        }

        args = shlex.split(arg)
        for key, arg in zip(params, args):
            params[key] = arg

        return params

    @staticmethod
    def __complete_arg(text, line, begin_idx, end_idx):
        defaults = {
            'cow': list_cows(),
            'eyes_list': ['==', 'XX', '$$', '@@', '**', '--', 'OO', '..'],
            'toungue_list': [';', '0', 'l', '|']
        }

        args = shlex.split(line)
        if len(args) <= 2 and begin_idx != end_idx:
            return None
        else:
            idx = len(args) - 3
            if begin_idx == end_idx:
                idx += 1

            key = ['cow', 'eyes', 'tongue'][idx]
            options = defaults[key]
            return [opt for opt in options if opt.startswith(text)]


    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def do_bye(self, arg):
        """Exit the program)"""
        return True

    def do_listcows(self, arg):
        """List all cows"""
        print(list_cows())

    def do_cowsay(self, arg):
        """Make cow say the message given as argument"""
        print(cowsay(**self.__parse_arg(arg)))

    def do_cowthink(self, arg):
        """Make cow think the message given as argument"""
        print(cowthink(**self.__parse_arg(arg)))

    def complete_cowsay(self, text, line, begin_idx, end_idx):
        return self.__complete_arg(text, line, begin_idx, end_idx)

    def complete_cowthink(self, text, line, begin_idx, end_idx):
        return self.__complete_arg(text, line, begin_idx, end_idx)

    def do_make_bubble(self, arg):
        """Generate bubble"""
        params = {
            'text': None,
            'wrap': True,
            'width': 40
        }

        args = shlex.split(arg)
        for key, arg, func in zip(params, args, [lambda x: x, eval, int]):
            params[key] = func(arg)

        params.update({
            'brackets': THOUGHT_OPTIONS['cowsay']
        })

        print(make_bubble(**params))

    def complete_make_bubble(self, text, line, begin_idx, end_idx):
        args = shlex.split(line)
        if len(args) <= 2 and begin_idx != end_idx:
            return None
        else :
            idx = len(args) - 2
            if begin_idx == end_idx:
                idx += 1
            if idx == 1:
                return [opt for opt in ['True', 'False'] if opt.startswith(text)]


if __name__ == '__main__':
    CowShell().cmdloop()
    