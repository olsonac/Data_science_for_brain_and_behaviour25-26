test = {
  'name': 'Question 2_male_counts',
  'points': 1,
  'suites': [
    {
      # res = np.random.randint(0, 2, size=(100000, 9901))
      # sums = res.sum(axis=1)
      # np.min(sums), np.max(sums) # minus / plus a bit.
      'cases': [
        {
          'code': r"""
          >>> # male_counts should be an array.
          >>> assert isinstance(male_counts, np.ndarray)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # male_counts should have 10000 values.
          >>> assert len(male_counts) == 10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # All values in male_counts should be in this range.
          >>> assert np.all((male_counts > 4730) & (male_counts < 5190))
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
