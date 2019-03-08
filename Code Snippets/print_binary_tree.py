def binaryPrint(cur, d):
    ret = ""
    if not cur:
        return

    if cur.right != None:
        ret += printPreorder(cur.right, d + 4)

    ret += "\n" + (" " * d) + str(cur.val)

    if cur.left != None:
        ret += printPreorder(cur.left, d + 4)

    return ret