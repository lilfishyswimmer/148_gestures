from setuptools import setup

package_name = '148_gestures'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='root',
    author_email='hdemendoza@ucsd.edu',
    maintainer='root',
    maintainer_email='hdemendoza@ucsd.edu',
    description='Gesture recognition using DepthAI hand tracking with ROS2 for RC car control',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gesture_tracker = 148_gestures.gesture_tracker:main',
            'gesture_controller = 148_gestures.gesture_controller:main',
        ],
    },
)

