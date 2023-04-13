from setuptools import setup,  find_namespace_packages
setup(
 name='clean_folder',
 version='1',
 description='',
 url='https://github.com/oduvaNN/Clean_folder',
 author='Kuznetsova Ilona',
 author_email='oduvan069@gmail.com',
 license='MIT',
 packages=find_namespace_packages(where='src'),
 package_dir={"": "src"},
 entry_points={'console_scripts': ['clean-folder = clean_folder:clean']},
 include_package_data=True
)
