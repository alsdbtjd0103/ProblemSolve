def rotation_90(arr,q):    # 시계 방향으로 90도 회전하는 함수
    temp=[[0]*q for i in range(q)]
    for i in range(q):
        for j in range(q):
            temp[j][q-1-i]=arr[i][j]
    return temp