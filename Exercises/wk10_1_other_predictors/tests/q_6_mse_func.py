test = {
  'name': 'Question q_6_mse_func',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Did you remember to return a value from your function?
          >>> assert mean_sq_err(np.array([3, 5]), 5) is not None
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert mean_sq_err(np.array([3, 4]), 5) == 2.5
          >>> assert mean_sq_err(np.array([3, 5]), 4) == 1
          >>> assert mean_sq_err(np.array([2, 3, 5]), 4) == 2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_wbc = ckd['White Blood Cell Count']
          >>> assert np.isclose(mean_sq_err(my_wbc, 10000),
          ...                        ((my_wbc - 10000) ** 2).mean())
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
