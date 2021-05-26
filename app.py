#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
# Copyright 2021 Atif Aziz
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

import simplejson
import pprint
import yaml
from django_jsonencoder import DjangoJSONEncoder

def get_output(y, type):
    objects = yaml.safe_load(y)
    if type == 'python':
        return pprint.pformat(objects)
    elif type in ['canonical_yaml', 'canonical-yaml']:
        return yaml.dump(objects, canonical=True)
    else: # type == 'json'
        return simplejson.dumps(objects, cls=DjangoJSONEncoder, indent=2)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if __name__ == '__main__':
    import sys
    args = sys.argv[1:] or ['json']
    try:
        print(get_output(sys.stdin.read(), args[0]))
    except Exception as why:
        eprint('ERROR:')
        eprint(why)
        sys.exit(1)
