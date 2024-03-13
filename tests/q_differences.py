
test = {
  'name': 'Question differences',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to make an array called "differences"
          >>> 'differences' in vars()
          True
          >>> isinstance(differences, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The first two values should be 532 and 401
          >>> differences[0] == 535
          True
          >>> differences[1] == 401
          True
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
