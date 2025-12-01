
test = {
  'name': 'Question m_to_all_ratio',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'm_to_all_ratio'
          >>> assert 'm_to_all_ratio' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'm_to_all_ratio'
          >>> # from its initial state (of ...)
          >>> assert m_to_all_ratio is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There were more boys born than girls.
          >>> assert m_to_all_ratio > 0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert 0.5161 < m_to_all_ratio < 0.51615
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
