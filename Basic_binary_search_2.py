def binary_search(sorted_list, left_pointer, right_pointer, target):
#sorted_listとtargetにリストと探したい数値を入れます。ここまでは前回のテストと同じ。left_pointerとright_pointerを最初と最後のインデックスから始め探している数値が見つかるまでこの数値を動かしていきます。

  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"
	
  # We calculate the middle index from the pointers now
  mid_idx = (left_pointer + right_pointer) // 2 #真ん中のインデックス
  mid_val = sorted_list[mid_idx] #真ん中の数値

  if mid_val == target: #もし真ん中の数値が探している数値と同じだった場合
    return mid_idx
    
  if mid_val > target: #探している数値が真ん中より小さい場合
    # 真ん中から右側にはないことがわかったので、right_pointerをmid_idxに持ってくる。
    return binary_search(sorted_list, left_pointer, mid_idx, target)
    
  if mid_val < target: #探している数値が真ん中より小さい場合
    # 真ん中から左側にはないことがわかったので、left_pointerをmid_idxに持ってくる。
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
#以下がテスト値
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("探している要素 {0} は インデックスの {1}　にあります。".format(288, result))
