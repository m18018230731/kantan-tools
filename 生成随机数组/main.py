import random

if __name__ == "__main__":
    try:
        start_num = int(input("Start number:"))
        need_num = int(input("How much u need:"))
        result_list = []
        for i in range(need_num):
            result_list.append(start_num)
            start_num = start_num + random.randint(-1000,1000)
            # result_list.append(str(start_num))
            # start_num = start_num + 1
        print(result_list)
    except Exception as e:
        print(e)