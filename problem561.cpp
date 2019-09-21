class Solution {
public:
    int vectorPairSum(vector<int>& nums) {
        
    }
    
    void swap(int* a, int* b)
    {
        int t = *a;
        *a = *b;
        *b = t;
    }

    int partition (int vector[], int l, int r) {
        int pivot = vector[r];
        int i = (l - 1);

        for (int j = l; j <= r - 1; j++) {
            if (vector[j] <= pivot) {
                i++;
                swap(&vector[i], &vector[j]);
            }
        }
        swap(&vector[i + 1], &vector[r]);
        return (i + 1);
    }

    void quickSort(int vector[], int l, int r) {
        if (l < r) {
            int pivot = partition(vector, l, r);
            quickSort(vector, l, pivot - 1);
            quickSort(vector, pivot + 1, r);
        }
    }
};