import os
import shutil
import subprocess
import glob
import subprocess
from shutil import copyfile

BUILD_DIR='build_pdf'
STORE_DIR=os.path.join('/home/paul/Downloads/', 'course_pdfs')

def make_dir():
    if os.path.isdir(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.mkdir(BUILD_DIR)

def make_store_dir():
    if not os.path.isdir(STORE_DIR):
        os.mkdir(STORE_DIR)

def copy_files(index):
    shutil.copytree('img', os.path.join(BUILD_DIR, 'img'))
    if index == 0:
        files = ['introduction.rst', 'super_hero.rst', 'lesson1_2.rst']
    else:
        files = glob.glob('lesson{i}*'.format(i  = index))
    files.append('Makefile')
    files.append('conf.py')
    list(map(lambda x: copyfile(x, '{build_dir}/{f}'.format(build_dir = BUILD_DIR, f = x)), files))

def make_pdf():
    subprocess.call('cd {b};  make latexpdf'.format(b = BUILD_DIR), shell= True)
    #subprocess.call('cd ../../big_data_course_build_pdf/ && make'.format(b = BUILD_DIR), shell= True)


def rename_pdf(index):
    new_pdf = 'lesson_{index}.pdf'.format(index = index)
    if index == 0:
        new_pdf = 'introduction.pdf'
    d = os.path.dirname(os.path.abspath(__file__))
    shutil.move('/home/paul/Documents/projects/big_data_course_build/latex/BigDataUWSummer2018.pdf',
            os.path.join(STORE_DIR, new_pdf))

def write_index(i):
    with open('index.rst', 'r') as read_obj:
        line = 'init'
        with open(os.path.join(BUILD_DIR, 'index.rst'), 'w') as write_obj:
            while line:
                line = read_obj.readline()
                if i != 0 and line.strip() in ['introduction', 'super_hero']:
                    continue
                if line.strip()[0:6] == 'lesson' and line.strip()[6:7] != str(i):
                    continue
                write_obj.write(line)

def main():
    make_store_dir
    for i in range(9):
        if i == 1:
            continue
        make_dir()
        copy_files(i)
        write_index(i)
        make_pdf()
        rename_pdf(i)

if __name__ == '__main__':
    main()
