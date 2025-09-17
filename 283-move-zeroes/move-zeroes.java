class Solution {
    public void moveZeroes(int[] nums) {
        int j=-1;
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(nums[i]==0){
                j=i;
                break;
            }
        }
        if(j==-1) return;

        for(int k=j+1;k<n;k++){
            if(nums[k]!=0){
                int t=nums[k];
                nums[k]=nums[j];
                nums[j]=t;
                j++;
            }
        }
    }
}