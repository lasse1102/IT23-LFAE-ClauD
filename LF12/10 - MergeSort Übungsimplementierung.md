
![[Pasted image 20240925105909.png]]


```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Mittenpunkt des Arrays finden
    mid = len(arr) // 2

    # Das Array in zwei Hälften teilen
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Rekursive Aufrufe, um beide Hälften zu sortieren
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Zusammenführen der sortierten Hälften
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    # Elemente von beiden Listen vergleichen und in sortierter Reihenfolge einfügen
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Restliche Elemente hinzufügen (falls vorhanden)
    if left_index < len(left):
        sorted_array.extend(left[left_index:])
        
    if right_index < len(right):
        sorted_array.extend(right[right_index:])

    return sorted_array

# Beispielaufruf:
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print("Sortierte Liste:", sorted_list)
```

