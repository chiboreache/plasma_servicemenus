import argparse
import subprocess


p = argparse.ArgumentParser()
p.add_argument('path_list')
args = p.parse_args()


def log():
    from pathlib import Path
    tx = 'import_to_kdenlive_script__log.txt'
    with open(f"{Path.home()}/.local/share/kio/servicemenus/{tx}", 'w') as f:
        f.write(comma_list)


def parse_comma_list(path_list):
    rs = []
    ph = ""
    for tkn in path_list.split():
        if tkn.endswith('.mp4'):
            ph += ' ' + tkn
            rs.append(ph.strip())
            ph = ""
        else:
            ph += ' ' + tkn
    return ','.join(rs).replace(' ', r'\ ')


comma_list = parse_comma_list(args.path_list)

# log()

subprocess.run(['kdenlive', '-i', comma_list])
