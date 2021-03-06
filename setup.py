from setuptools import setup, find_packages

setup(name='qcpy',
      version='0.2.2',
      description='Tools for automating running quantum chemistry jobs',
      url='http://github.com/peterspackman/qcauto',
      author='Peter Spackman',
      author_email = 'peterspackman@fastmail.com',
      keywords = ['quantum chemistry', 'qc', 'job'],
      classifiers = [
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Chemistry',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
      license='GPLv3',
      packages=find_packages(),
      package_data={
         'qcpy.templates': ['*.template']  # include all templates
      },
      entry_points={
          'console_scripts': [
              'chembench-init = qcpy.cli:generate_inputs',
              'chembench-process = qcpy.cli:process_outputs_main',
              'chembench-process-batch = qcpy.cli:process_outputs_batch'
          ]
      },
      install_requires=['numpy', 'jinja2', 'tqdm'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
)
