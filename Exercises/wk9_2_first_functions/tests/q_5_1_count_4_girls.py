test = {
  'name': 'Question 5_1_count_4_girls',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You haven't defined a count_4_girls function yet
          >>> assert 'count_4_girls' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # count_4_girls is not a function
          >>> import types
          >>> assert type(count_4_girls) is types.FunctionType
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert 0 <= count_4_girls() <= 4
          """,
          'hidden': False,
          'locked': False
        },
        {
          # counts = np.random.binomial(4, 0.487, (10000, 1000))
          # means = np.mean(counts, axis=0)
          # np.min(means), np.max(means)
          'code': r"""
          >>> counts = np.zeros(10000)
          >>> for i in range(10000):
          ...     counts[i] = count_4_girls()
          >>> assert np.all(counts >= 0)
          >>> assert np.all(counts <= 4)
          >>> assert 1.9 <= np.mean(counts) <= 1.99
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
