class Solution {
    public int majorityElement(int[] nums) {
       int c=0;
       int e=0;
       for(int i=0;i<nums.length;i++){
            if(c==0){
                c=1;
                e=nums[i];
            }
            else if(nums[i]==e){
                c++;
            }
            else{
                c--;
            }
       }
       return e;
    }
}