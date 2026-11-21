from pathlib import Path

ENTRY = ('The night ferry runs late. '
    'You sit on the deck with your coat folded behind you, '
    'and the engine knocks softly under the floor. '
    'Somewhere ahead is a harbour you have never seen. '
    'You finish your coffee. The lights come closer.')

def write_entry():
    out = Path('/output')
    out.mkdir(parents=True, exist_ok=True)
    (out / 'entry.txt').write_text(ENTRY, encoding='utf-8')
    print(ENTRY)

if __name__ == '__main__':
    write_entry()
