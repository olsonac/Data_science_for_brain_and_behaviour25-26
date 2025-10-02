test = {
  'name': 'Question defining_a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'a'
          >>> # Have you run the cell defining 'a' yet?
          >>> 'a' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'a'
          >>> # from its initial state (of 0)
          >>> a != 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Change the value of 'a' to 3.
          >>> a == 3
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
