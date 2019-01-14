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
