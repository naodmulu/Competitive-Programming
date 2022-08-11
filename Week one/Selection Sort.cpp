int select(int arr[], int i, int n)
    {
        // code here such that selectionSort() sorts arr[]
        for (int j = i + 1; j < n; j++) {
              if ( arr[i] > arr[j]) {
                  swap(arr[i],arr[j]);
              }
        }
        return 0;
    }

    void selectionSort(int arr[], int n)
    {
       //code here
      int change;
      for(int i = 0; i < n - 1; i++) {
          select(arr,i,n);
      }
    }