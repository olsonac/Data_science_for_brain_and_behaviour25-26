test = {
  'name': 'Question hamlet_improved',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'hamlet_improved'
          >>> 'hamlet_improved' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'hamlet_improved'
          >>> # from its initial state (of ...)
          >>> hamlet_improved is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> we_want = np.array(['to', 'be', 'or', 'not', 'to', 'be',
          ...             'that', 'be', 'the', 'question',
          ...             'whether', 'be', 'nobler', 'in', 'the', 'mind',
          ...             'to', 'suffer', 'the', 'slings', 'and', 'arrows',
          ...             'of', 'outrageous', 'fortune'])
          >>> assert np.all(we_want == hamlet_improved)
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
