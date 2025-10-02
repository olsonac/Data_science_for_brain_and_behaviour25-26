test = {
  'name': 'Question correct_weekly_rate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'correct_weekly_rate'
          >>> 'correct_weekly_rate' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # This is a rate, not an increaser.  Remember, the rate
          >>> # is how much it grows each week, and should be a lot less
          >>> # than one.  It will be pretty close to the bank's estimate.
          >>> correct_weekly_rate < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You found that the bank's estimate gave you slightly more
          >>> # debt than the 0.1 yearly rate.  So your estimate for the
          >>> # correct weekly rate should be a tiny bit less than the bank's
          >>> # original estimate.
          >>> correct_weekly_rate < weekly_interest_rate
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Keep trying!  The value is very close to the bank's estimate.
          >>> round(correct_weekly_rate, 8) == 0.00183457
          True
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
