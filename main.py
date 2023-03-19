def parallel_processing(n, m, data):
    output = []
    nakamais = [0] * n  
    for darbs in range(m):
        thread = nakamais.index(min(nakamais))  
        darba_sakums = nakamais[thread]  
        output.append((thread, darba_sakums))  
        nakamais[thread] += data[darbs]  
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
