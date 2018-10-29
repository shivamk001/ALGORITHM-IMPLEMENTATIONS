def max_heapify(arr, i):
      l=2*i+1
      r=2*i+2
      print("i: ", i, "l: ", l, "r: ", r)
      if(l<len(arr) and arr[l]>arr[i]):
            largest=l
      else:
            largest=i

      if(r<len(arr) and arr[r]>arr[l]):
            largest=r

      if(largest != i):
            t=arr[i]
            arr[i]=arr[largest]
            arr[largest]=t
            print(arr)
            max_heapify(arr, largest)

def build_max_heap(arr):
      heap_size=len(arr)

      for i in range(int(len(arr)/2)-1, -1, -1):
            max_heapify(arr, i)

if __name__=='__main__':
      arr=[1,2,3,4,5,6,7]
      print("Before heapify:", arr)
      build_max_heap(arr)
      print("After heapify:", arr)
      
