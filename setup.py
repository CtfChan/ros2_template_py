from setuptools import setup

package_name = 'ros2_template_py'

setup(
    name=package_name,
    version='0.6.1',
    packages=[],
    py_modules=[
        'demo'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='yourname',
    author_email='email@XXX',
    maintainer='yourname',
    maintainer_email='email@XXX',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal publishers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo = demo:main',
        ],
    },
)
