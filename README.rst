Code and documentation for big data intro course at UW, summer 2018

To build docs for web:

1. make html
2. cd ../../big_data_course_build/html
3. git commit -am "<message for new docs>" 
4. git push

If you do:
make clean
You will have to recreate the build docs:

1. cd ../../big_data_course_build/
2. rm -Rf html
3. git clone git@github.com:paulhtremblay/big_data_course.git html
4. cd  html
5. git checkout gh-pages

tar --exclude=python_code/temp_data  -cvzf  python_code.tar.gz python_code/
