
test = {
  'name': 'Question courses',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'courses'
          >>> assert 'courses' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'courses'
          >>> # from its initial state (of ...)
          >>> assert courses is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Courses should be a data frame
          >>> assert isinstance(courses, pd.DataFrame)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Courses should have 75 rows.
          >>> assert len(courses) == 75
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
