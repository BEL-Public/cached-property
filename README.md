# Cached Property

This module adds a decorator `cached_property` and a function `drop_cache`.

## Example

```python
from cached_property import cached_property, drop_cache
import time

class Dummy:
    @cached_property
    def the_answer(self):
        time.sleep(0.5)
        return 42

dummy = Dummy()
t0 = time.time()
err = dummy.the_answer
dt = time.time()-t0
print(dt)
# dt -> ~0.5 seconds
t0 = time.time()
err = dummy.the_answer
dt = time.time()-t0
print(dt)
# dt -> ~1e-6 seconds
drop_cache(dummy, 'the_answer')
t0 = time.time()
err = dummy.the_answer
dt = time.time()-t0
print(dt)
# dt -> ~0.5 seconds
```

## License and Copyright
Copyright 2019 Brain Electrophysiology Laboratory Company LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this module or the code  within it except in
compliance with the License.

You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
