test = {
  'name': 'Question q_11_mae_predictors',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'predictors'
          >>> assert 'predictors' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'predictors'
          >>> # from its initial state (of ...)
          >>> assert predictors is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.allclose((predictors - 7000) * 2, np.arange(6000))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You need to set the value for 'mae_for_predictors'
          >>> assert 'mae_for_predictors' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'mae_for_predictors'
          >>> # from its initial state (of ...)
          >>> assert mae_for_predictors is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert len(mae_for_predictors) == len(predictors)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # This is a fancy "vectorized" method to do the calcuations,
          >>> # but you probably used a "for" loop.
          >>> my_wbc = np.array(ckd['White Blood Cell Count'])
          >>> ps = np.arange(6000) / 2 + 7000  # Slightly obfuscated.
          >>> m_abs_deviations = np.mean(np.abs(my_wbc[:, None] - ps), axis=0)
          >>> assert np.allclose(mae_for_predictors, m_abs_deviations)
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
