test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          # trials = np.random.randint(1, 11, size=(10000, 1000))
          # scores = np.sum(trials, axis=1)
          # np.min(scores), np.max(scores)
          'code': r"""
          >>> assert 5090 <= total_score <= 5900
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
