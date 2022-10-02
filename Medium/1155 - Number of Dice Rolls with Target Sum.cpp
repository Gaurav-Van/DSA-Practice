class Solution {
public:
    int rec_and_overlap(int dice, int faces, int target, vector<vector<int>>&dp)
    {
        if(dice==0 || target<=0)
            return (int)(dice==target);
            
        if(dp[dice][target] != -1)
            return dp[dice][target];
        
        int ans = 0;
        for(int i=1;i<=faces;i++)
        {
            ans = (ans + rec_and_overlap(dice-1, faces, target-i, dp))%1000000007;
        }
        
        return dp[dice][target] = ans;
    }
    
    int numRollsToTarget(int n, int k, int target) 
    {
        vector<vector<int>> dp(n+1, vector<int>(target+1, -1));
        return rec_and_overlap(n, k, target, dp);
    }
};
