import ntpath, glob
import os
from util import os_check


def find_files_by_extension(dir_path, target_extension):
    found_paths = glob.glob(os.path.join(dir_path, '*.' + target_extension))
    return found_paths


def extract_filename(path):
    platform = os_check.get_platform()

    # linux, unix
    if platform == 'OSX':
        head, tail = os.path.split(path)
        return tail
    elif platform == 'Windows':
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
    else:
        raise RuntimeError("Not supported platform " + platform)


def change_extension(path, extension):
    # return Path(path).stem + "." + extension
    base = os.path.splitext(path)[0]
    os.rename(path, base + "." + extension)

