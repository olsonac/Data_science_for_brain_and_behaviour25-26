
test = {
  'name': 'Question total1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You will need to define a "total1" variable.
          >>> assert 'total1' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Oops - did you accidentally include 13?
          >>> assert total1 != 91
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Not there yet...
          >>> assert total1 == 78
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
