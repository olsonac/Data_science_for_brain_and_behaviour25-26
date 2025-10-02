test = {
  'name': 'Question hamlet_joined',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'hamlet_joined'
          >>> 'hamlet_joined' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'hamlet_joined'
          >>> # from its initial state (of ...)
          >>> hamlet_joined is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you remember the apostrophe in 'tis ?
          >>> "'" in hamlet_joined
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you remember get 'tis in there?
          >>> "'tis" in hamlet_joined
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you join the string with " "?
          >>> " " in hamlet_joined
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hamlet_joined == ("to be or not to be that is the question "
          ...                   "whether 'tis nobler in the mind to suffer "
          ...                   "the slings and arrows of outrageous fortune")
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
