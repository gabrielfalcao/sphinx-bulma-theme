# -*- coding: utf-8 -*-


def make_user(email, password, admin=False, **kwargs):
    """creates structured user data for storage

    :param email: string
    :param password: in plain-text
    :param admin: bool - indicates user has all priviledges
    :param kwargs: extra data

    :returns: a :py:class:`dict` with user data
    """
    data = locals()
    data.update(data.pop('kwargs'))
    return data
