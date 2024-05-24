import inspect
import logging
import sys
from datetime import datetime


def set_debug():
    logging.getLogger().setLevel(logging.DEBUG)


def is_debug() -> bool:
    """
    此处是根据日志等级判断的debug，和服务器本身的状态不一定一致
    """
    return logging.getLogger().isEnabledFor(logging.DEBUG)


def _get_depth(kwargs) -> int:
    depth = 0
    if 'depth_' in kwargs:
        depth = kwargs['depth_']
        del kwargs['depth_']
    return depth


def _get_class_from_frame(fr):
    args, _, _, value_dict = inspect.getargvalues(fr)
    if len(args) and args[0] == 'self':
        instance = value_dict.get('self', None)
        if instance:
            return getattr(instance, '__class__', None)
    if len(args) and args[0] == 'cls':
        instance = value_dict.get('cls', None)
        if instance:
            return instance
    return None


get_frame = getattr(sys, "_getframe")


def _get_prefix(depth: int = 1):
    f = getattr(sys, '_getframe')(depth + 1)
    func_name = f.f_code.co_name
    lineno = f.f_lineno
    file_name = ''
    class_name = ''
    # if is_debug():
    length = 5 if is_debug() else 2
    file_name = f.f_code.co_filename
    file_name = file_name.split('src')[-1]
    file_name = '/'.join(file_name.split('/')[-length:])
    clazz = _get_class_from_frame(f)
    class_name = '' if not clazz else clazz.__name__

    prefix = '[{time}]-[{file_name}][{lineno}]-[{class_name}.{func_name}]==>:'.format(
        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
        file_name=file_name, lineno=lineno,
        class_name=class_name, func_name=func_name)

    return prefix


def _pack_args(*args, **kwargs) -> str:
    delimiter = kwargs.get('delimiter', ' ')
    assert isinstance(delimiter, str)
    return delimiter.join([str(arg) for arg in args])


def _pack_msg(*args, **kwargs) -> str:
    depth = _get_depth(kwargs)
    prefix = _get_prefix(depth + 1 + 1)
    msg = prefix + _pack_args(*args, **kwargs)

    return msg


def info(*args, **kwargs):
    if logging.getLogger().isEnabledFor(logging.INFO):
        logging.info(_pack_msg(*args, **kwargs))


def error(*args, **kwargs):
    if logging.getLogger().isEnabledFor(logging.ERROR):
        logging.error(_pack_msg(*args, **kwargs))


exception = error


def warning(*args, **kwargs):
    if logging.getLogger().isEnabledFor(logging.WARNING):
        logging.warning(_pack_msg(*args, **kwargs))


def debug(*args, **kwargs):
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        logging.debug(_pack_msg(*args, **kwargs))


def critical(*args, **kwargs):
    if logging.getLogger().isEnabledFor(logging.CRITICAL):
        logging.critical(_pack_msg(*args, **kwargs))
