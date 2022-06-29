from absl import flags
def pytest_configure(config):
  flags.FLAGS.mark_as_parsed()
