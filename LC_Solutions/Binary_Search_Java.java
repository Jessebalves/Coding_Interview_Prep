package pack1;

public class Randissimo {
	public static void main(String[] args) {
		int[] arr = {1,2,3};
		int target = 4;
		int indexo = BinarySearch(arr,target);
		System.out.println(indexo);
	}
	
	static int BinarySearch(int[] arr, int target) {
		int left = 0;
		int right = arr.length - 1;
		
		while(left<=right) {
			int middle = (left+right) / 2;
			if(target == arr[middle]) {
				return middle;
			} else if(target < arr[middle]){
				right = middle -1;
			} else {
				left = middle + 1;
			}
			
		}
		return -1;
	}
}
