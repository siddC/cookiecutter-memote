# -*- coding: utf-8 -*-

# Copyright 2017 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

from os.path import isabs, exists, isfile

MODEL_PATH = "{{ cookiecutter.model }}"


if MODEL_PATH != "default":
    if not (isabs(MODEL_PATH) and exists(MODEL_PATH) and isfile(MODEL_PATH)):
        raise ValueError(
            "'model' value must be an absolute path to an existing file;"
            " got '{}' instead.".format(MODEL_PATH))
