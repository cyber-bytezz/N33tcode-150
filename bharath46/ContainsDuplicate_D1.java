class Solution1   //runtime 11ms (more efficient (O(n) time complexity))
{
	public boolean containsDuplicate(int[] nums) 
	{
		HashSet<Integer> elements = new HashSet<>();
		
		for(int i= 0; i<nums.length; i++)
		{
			if(elements.contains(nums[i]))
				return true;
				elements.add(nums[i]);
		}
		
		return false;
	}
	
}


class Solution2    // runtime 18ms (less efficient (O(n log n) time complexity) )
{
	public boolean containsDuplicate(int[] nums) 
	{
		Arrays.sort(nums);
		
		for(int i= 0; i<nums.length-1; i++)
		{
			if(nums[i] == nums[i+1] return true;
			
		}
		
		return false;
	}
	
}


