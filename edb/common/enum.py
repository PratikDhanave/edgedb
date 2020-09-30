#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2008-present MagicStack Inc. and the EdgeDB authors.
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
#


from __future__ import annotations

import enum


class StrEnum(str, enum.Enum):
    """A version of string enum with reasonable __str__."""

    def __str__(self):
        return self._value_


class StrCaseInsensitiveEnum(StrEnum):
    """A case insensitive version of StrEnum."""

    @classmethod
    def _missing_(cls, name):
        return cls(name.upper())
