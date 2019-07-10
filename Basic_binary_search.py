def binary_search(sorted_list, target):#sorted_listがソートされたリスト、targetが探している要素
  
  if not sorted_list: # まず初めにリストに要素が存在するか確かめる。
    return 'value not found'
  
  mid_idx = len(sorted_list)//2 # 真ん中のインデックスを求める
  mid_val = sorted_list[mid_idx] # 先ほど変数にした真ん中のインデックスを使い真ん中の要素を求める。
  
  if mid_val == target: # もし真ん中の要素が探している要素であればその要素をリターン
    return mid_idx
  
  if mid_val > target: #探している要素が真ん中の要素より小さい場合
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)#見つかるまで自身の関数に入って計算し続ける
  
  if mid_val < target:#探している要素が真ん中の要素より大きい場合
    right_half = sorted_list[mid_idx+1:]
    result = binary_search(right_half, target)#見つかるまで自身の関数に入って計算し続ける
    
    if result == "value not found":#探している要素が見つからない場合
      return result
    else:
      return result + mid_idx + 1
    
# テスト:
sorted_values = [13, 14, 15, 16, 17,18,19,20,21]
print(binary_search(sorted_values, 21))
