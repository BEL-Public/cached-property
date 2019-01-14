
import types

def get_cached_property_name(obj):
    if isinstance(obj, types.FunctionType):
        name = obj.__name__
    elif isinstance(obj, str):
        name = obj
    else:
        raise ValueError("Invalid argument '%s'"%obj)
    return '_cached_'+name

def cached_property(fn):
    cached_name = get_cached_property_name(fn)

    @property
    def _cached_property(self):
        try:
            return getattr(self, cached_name)
        except AttributeError:
            ans = fn(self)
            setattr(self, cached_name, ans)
            return ans
    _cached_property.__doc__ = fn.__doc__
    return _cached_property

def drop_cache(obj, prop_name, permissive=False):
    cached_name = get_cached_property_name(prop_name)
    if hasattr(obj, cached_name):
        delattr(obj, cached_name)
    else:
        if not permissive:
            raise ValueError("Property '%s' not cached in object '%s'"%(prop_name, obj))
