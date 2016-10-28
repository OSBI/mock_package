import os
import sys

if __name__ == "__main__":
  if len(sys.argv) != 2:
    sys.stderr.write('Wrong number of arguments\n')
    sys.stderr.write('Correct usage: python doit.py <package>\n')
    sys.exit(1)

  package = sys.argv[1]
  package_path = 'src/main/java/' + package.replace('.', '/')
  file_name = package_path + '/MockClass.java'

  os.makedirs(package_path)
  f = open(file_name, 'w+')

  f.write('package ' + package + '; public class MockClass {}\n')
  f.close()

  print ('Done, file ' + file_name + ' created successfully')