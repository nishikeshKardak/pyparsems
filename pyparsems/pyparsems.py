import math
from sys import argv

class parseMilliSecs:
  @staticmethod
  def parse_millisecs(ms):
    try:
      val = int(ms)
    except TypeError:
      print("Expected the input as number.")
    ms = int(ms)

    round_ms = lambda t: math.floor(t) if t > 0 else math.ceil(t)

    return dict(
      days=round_ms(ms / 86400000),
      hours=round_ms(ms / 3600000) % 24,
      minutes=round_ms(ms / 60000) % 60,
      seconds=round_ms(ms / 1000) % 60,
      milliseconds=round_ms(ms) % 1000,
      microseconds=round_ms(ms * 1000) % 1000,
      nanoseconds=round_ms(ms * 1e6) % 1000
    )

if __name__ == "__main__":
    val = argv[1]
    print(parseMilliSecs.parse_millisecs(val))
