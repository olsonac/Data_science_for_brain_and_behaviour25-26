test = {
  'name': 'Question easy_top_10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'easy_top_10'
          >>> assert 'easy_top_10' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'easy_top_10'
          >>> # from its initial state (of ...)
          >>> assert easy_top_10 is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # easy_top_10 should be a data frame
          >>> assert isinstance(easy_top_10, pd.DataFrame)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # easy_top_10 should have 10 rows.
          >>> assert len(easy_top_10) == 10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # easy_top_10 should be sorted, easiest first.
          >>> all_easy = np.sort(courses['Easiness'])[::-1]
          >>> assert np.all(easy_top_10['Easiness'] == all_easy[:10])
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
