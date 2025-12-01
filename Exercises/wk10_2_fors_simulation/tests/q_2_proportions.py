test = {
  'name': 'Question 2_proportions',
  'points': 1,
  'suites': [
    {
      # res = np.random.randint(0, 2, size=(10000000, 82))
      # means = res.mean(axis=1)
      # np.min(means), np.max(means)
      'cases': [
        {
          'code': r"""
          >>> # Proportions should be an array.
          >>> assert isinstance(proportions, np.ndarray)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'proportions'
          >>> # from its initial state (of an array of zeros).
          >>> assert np.any(proportions != 0)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # proportions should have 10000 values.
          >>> assert len(proportions) == 10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # All values in proportions should be in this range.
          >>> assert np.all(proportions > 0.219)
          >>> assert np.all(proportions < 0.781)
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
