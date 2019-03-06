def swap(a, b):  # 将a,b交换
    temp = a
    a = b
    b = temp
    return a,b

def sift_down(array, start, end):
    """
    调整成大顶堆，初始堆时，从下往上；交换堆顶与堆尾后，从上往下调整
    :param array: 列表的引用
    :param start: 父结点
    :param end: 结束的下标
    :return: 无
    """
    while True:

        # 当列表第一个是以下标0开始，结点下标为i,左孩子则为2*i+1,右孩子下标则为2*i+2;
        # 若下标以1开始，左孩子则为2*i,右孩子则为2*i+１
        left_child = 2*start + 1  # 左孩子的结点下标
        # 当结点的右孩子存在，且大于结点的左孩子时
        if left_child > end:
            break

        if left_child+1 <= end and array[left_child+1] > array[left_child]:
            left_child += 1
        if array[left_child] > array[start]:  # 当左右孩子的最大值大于父结点时，则交换
            array[left_child], array[start] = swap(array[left_child], array[start])

            start = left_child  # 交换之后以交换子结点为根的堆可能不是大顶堆，需重新调整
        else:  # 若父结点大于左右孩子，则退出循环
            break

        print(">>", array)


def heap_sort(array):  # 堆排序
    # 先初始化大顶堆
    first = len(array)//2 -1  # 最后一个有孩子的节点(//表示取整的意思)
    # 第一个结点的下标为０，很多博客&课本教材是从下标1开始，无所谓吧，你随意
    for i in range(first, -1, -1):  # 从最后一个有孩子的节点开始往上调整
        print(array[i])
        sift_down(array, i, len(array)-1)  # 初始化大顶堆

    print("初始化大顶堆结果:", array)
    # 交换堆顶与堆尾
    for head_end in range(len(array)-1, 0, -1):  # start stop step
        array[head_end], array[0] = swap(array[head_end], array[0]) # 交换堆顶与堆尾
        sift_down(array, 0, head_end-1)  # 堆长度减一(head_end-1)，再从上往下调整成大顶堆
        print ("第几个大的数:",len(array)-head_end,array[head_end])



if __name__ == "__main__":
    array = [-1,2,0]
    print(array)
    heap_sort(array)
    print("堆排序最终结果:", array)


