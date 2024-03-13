test = {
  'name': 'Question 2_male_counts',
  'points': 1,
  'suites': [
    {
      # rng = np.random.default_rng()
      # res = rng.choice([0, 1], size=(100000, 9901))
      # sums = res.sum(axis=1)
      # np.min(sums), np.max(sums) # minus / plus a bit.
      'cases': [
        {
          'code': r"""
          >>> # male_counts should be an array.
          >>> isinstance(male_counts, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # male_counts should have 10000 values.
          >>> len(male_counts) == 10000
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
