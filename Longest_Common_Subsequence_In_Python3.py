def lcs(str1, str2):
      #calculate length of strings
      l1=len(str1)
      l2=len(str2)

      #initialise an array having l1+1 rows and l2+1 columns
      #all elements have value equal to 'None'
      arr=[[None for i in range(l2+1)] for j in range(l1+1)]

      #assigning 0 to each element in first row
      for i in range(l1+1):
            arr[i][0]=0

      #assigning 0 to each element in first column
      for j in range(l2+1):
            arr[0][j]=0

      for i in range(1, l1+1):
            for j in range(1, l2+1):
                  if str1[i-1]==str2[j-1]:
                        arr[i][j]=1+arr[i-1][j-1]

                  else:
                        if(arr[i-1][j]>arr[i][j-1]):
                              arr[i][j]=arr[i-1][j]
                        else:
                              arr[i][j]=arr[i][j-1]

      return arr[l1][l2]

if __name__=='__main__':
      str1=input("Enter string 1: ")
      str2=input("Enter string 2: ")

      #function to calculate the length of longest subsequence
      result=lcs(str1, str2)
      print("The length of the longest subsequence is: ", result)
                        
