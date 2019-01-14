
import pytest
from .cached_property import cached_property, drop_cache
import time

sleep_time = 0.3

@pytest.fixture
def dummy():
    class Dummy:
        @cached_property
        def takes_some_time(self):
            """some documentation code"""
            time.sleep(sleep_time)
            return 'unexpected time span'
    return Dummy()

def test_cached_property(dummy):
    """Test that property is cached"""
    # Test that doc string is transfered by decorator
    assert type(dummy).takes_some_time.__doc__ == """some documentation code"""
    # first time takes 1 second
    t0 = time.time()
    err = dummy.takes_some_time
    dt = time.time()-t0
    assert dt == pytest.approx(sleep_time, 1e-2), err
    # second time takes zero second, because result is cached
    # here we also test that the output didn't change.
    t0 = time.time()
    assert err == dummy.takes_some_time, "Cache has wrong value"
    dt = time.time()-t0
    assert dt == pytest.approx(0.0, abs=1e-2), err

def test_drop_cache(dummy):
    """test that cache is removed"""
    # test that `drop_cache` can fail if no cache exists
    drop_cache(dummy, 'takes_some_time', permissive=True)
    with pytest.raises(ValueError):
        drop_cache(dummy, 'takes_some_time')
    t0 = time.time()
    err = dummy.takes_some_time
    dt = time.time()-t0
    assert dt == pytest.approx(sleep_time, 1e-2), err
    drop_cache(dummy, 'takes_some_time')
    t0 = time.time()
    assert err == dummy.takes_some_time, "Function output changed"
    dt = time.time()-t0
    assert dt == pytest.approx(sleep_time, abs=1e-2), err
