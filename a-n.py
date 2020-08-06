# 「安直法」によるべき乗 (a^n) の計算アルゴリズム
function pow_simple(a, n):
  r = 1
  repeat `n` times:
    r *= a
  return r