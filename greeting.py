import random as r


def random_greeting():
  arr = ('こんにちは', 'お疲れ様です', 'ごきげんよう')
  return r.choice(arr)


print(f'greeting.py の __name__ => {__name__}')  # 注目

# random_greeting の動作チェック
if __name__ == '__main__':
  assert type(random_greeting()) == str
  for i in range(5):
    print(f'{i}. {random_greeting()}')
