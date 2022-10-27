# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(name='python-card-framework',
                 version='0.5.0',
                 description='API for rendering Chat App Card json.',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://github.com/google/python-card-framework',
                 author='David Harcombe',
                 author_email='davidharcombe@google.com',
                 license='Apache 2.0',
                 zip_safe=False,
                 include_package_data=True,
                 packages=setuptools.find_packages(),
                 classifiers=[
                     'Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'Topic :: Software Development',
                     'License :: OSI Approved :: Apache Software License',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.9',
                 ],
                 python_requires=">=3.10",
                 install_requires=[
                     'dataclasses-json>=0.5.2',
                     'stringcase>=1.2.0'
                 ],
                 )
