import numpy as np

def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n // arrays[0].size
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out

def mlinspace(a,b,orders,out=None):

    import numpy

    sl = [numpy.linspace(a[i],b[i],orders[i]) for i in range(len(a))]

    if out is None:
        out = cartesian(sl)
    else:
        cartesian(sl, out)

    return out

def MyJacobian(fun, eps=1e-6):

    def rfun(x):
        n = len(x)
        x0 = x.copy()
        y0 = fun(x)
        D = np.zeros( (len(y0),len(x0)) )
        for i in range(n):
            delta = np.zeros(len(x))
            delta[i] = eps
            y1 = fun(x+delta)
            y2 = fun(x-delta)
            D[:,i] = (y1 - y2)/eps/2
        return D
    return rfun
