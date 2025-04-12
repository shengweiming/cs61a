def pair(s):
    '''Returns TRUE if for each element x in S there is some other element y in S such that x==y. Assume S is non-empty.
    >>> pair([1,2,3,3,2,1])
    True

    >>> pair([1,2,3,4,4,3,2])
    False

    >>> pair([1,2,3,-1,-1,2,3,1])
    True

    >>> pair([0])
    False
    '''
    t = [sum([1 for x in s if s[i]==x])-1 for i in range(len(s))]

    return all(t)


def ordered(s, key=lambda x: x):
    if s.rest == Link.empty:
        return True
    else:
        return all( [key(s.first) <= key(s.rest.first), ordered(s.rest)] )


def new_sorted(s,t):
    if s == Link.empty and t == Link.empty:
        return Link.empty
    elif s == Link.empty and t != Link.empty:
        return Link(t.first, t.rest)
    elif s != Link.empty and t == Link.empty:
        return Link(s.first, s.rest)
    else:
        if s.first < t.first:
            return Link(s.first, new_sorted(s.rest, t))
        elif s.first > t.first:
            return Link(t.first, new_sorted(s, t.rest))
        else:
            return Link(s.first, Link(t.first, new_sorted(s.rest, t.rest)))

def combine(s,t):
    while s != Link.empty and t != Link.empty:
        if s.first <= t.first:
            s.rest = t
        else:
            t.rest = s
        s, t = s.rest, t.rest



    if s != Link.empty and t != Link.empty:
        a , b = s.first, t.first
        while 
        if a <= b:



class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

if __name__ == "__main__":
    import doctest
    doctest.testmod()