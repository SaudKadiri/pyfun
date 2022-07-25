# Encapsulation for Python methods; implemented using decorators.
# Author: Saud Kadiri 
"""
C++
+---------------------------------------------------+
| Modifier     | Same Class | Derived Class |  Main |
|--------------+------------+---------------+-------|
|  public      |     ✅     |       ✅      |  ✅  |    
+--------------+------------+---------------+-------|
|  protected   |     ✅     |       ✅      |  ❌  |
+--------------+------------+---------------+-------|
|  private     |     ✅     |       ❌      |  ❌  |
+--------------+------------+---------------+-------+
"""

class DecoratedFunctionException(Exception):
    pass

class MagicMethodException(Exception):
    pass

class RestictedAccessException(Exception):
    pass

import types, functools, inspect

def public(meth):
    @functools.wraps(meth)
    def wrapper(*args, **kwargs):
        frame = inspect.stack()[1].frame
        meth_class = frame.f_globals.get(meth.__qualname__.split('.')[0], None)
        if 'local' in meth.__qualname__ or isinstance(meth_class, types.FunctionType):
            raise DecoratedFunctionException(f"`{meth.__qualname__}` is a function. @public decorator is only for methods.")
        return meth(*args, **kwargs)
    return wrapper

def protected(meth):
    @functools.wraps(meth)
    def wrapper(*args, **kwargs):
        meth_name = meth.__name__
        frame = inspect.stack()[1].frame
        meth_class = frame.f_globals.get(meth.__qualname__.split('.')[0], None)
        caller_class = frame.f_locals.get('self', None).__class__

        if meth_name.startswith('__') and meth_name.endswith('__'):
            raise MagicMethodException("Magic methods are to have public access.")

        if 'local' in meth.__qualname__ or isinstance(meth_class, types.FunctionType):
            raise DecoratedFunctionException(f"`{meth_name}()` is a function. @protected decorator is only for methods.")

        if meth_class != caller_class and not issubclass(caller_class, meth_class):
            raise RestictedAccessException(f'Cannot access <{meth.__qualname__}> from {caller_class}')

        return meth(*args, **kwargs)
    return wrapper

def private(meth):
    @functools.wraps(meth)
    def wrapper(*args, **kwargs):
        meth_name = meth.__name__
        frame = inspect.stack()[1].frame
        meth_class = frame.f_globals.get(meth.__qualname__.split('.')[0], None)
        caller_class = frame.f_locals.get('self', None).__class__

        if meth_name.startswith('__') and meth_name.endswith('__'):
            raise MagicMethodException("Magic methods are to have public access.")
        
        if 'local' in meth.__qualname__ or isinstance(meth_class, types.FunctionType):
            raise DecoratedFunctionException(f"`{meth_name}()` is a function. @private decorator is only for methods.")

        if meth_class != caller_class:
            raise RestictedAccessException(f'Cannot access <{meth.__qualname__}> from {caller_class}')
    
        return meth(*args, **kwargs)
    return wrapper
