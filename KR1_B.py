def list_to_array(linked_list, head):
    ans = []
    val, next = head

    while True:
        ans.append(val)
        val, next = linked_list[next]
        if next == -1:
            ans.append(val)
            break

    return ans
######################################
