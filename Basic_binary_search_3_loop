#今回はループを使ってバイナリーサーチをしていきます。

#まず初めに関数を作りその中の一番上にリストの最初と最後を決めるleft_pointerとright_pointerを作ります。
def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # ここからWhileを使って探している値が見つかるまでループさせていきます。
  while left_pointer < right_pointer:
  
    mid_idx = (left_pointer + right_pointer) // 2 ＃真ん中の値インデックスを出す
    mid_val = sorted_list[mid_idx] ＃真ん中の値を出す
    
    if mid_val == target: ＃探している値と真ん中の値が同じ場合
      return mid_idx
      
    if target < mid_val: #検索値が中心値より小さいので右のポイントを中心に持ってくる
      right_pointer = mid_idx
      
    if target > mid_val:#検索値が中心値より大きいので左のポイントを中心に持ってくる
      left_pointer = mid_idx + 1
  
  return "Value not in list" #何も見つからない場合これが出力

# テストしてみよう。
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))
