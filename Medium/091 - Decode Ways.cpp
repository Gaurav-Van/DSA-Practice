class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        vector<int>dp(n+10);
        
        dp[0] = 1; /*a - to check for double digit*/
        dp[1] = ((s[0] - '0')==0) ? 0:1; /*b - to check for single digit*/
        
        /*These a and b will increment as we move on - thats why dp is used*/
        
        for(int i=2; i<=n; i++)
        {
            int singledigit = s[i-1] - '0';
            int doubledigit = 10*(s[i-2] - '0') + (s[i-1] - '0');
            
            if(singledigit >=1 && singledigit <=9) 
                dp[i]+= dp[i-1];
            if(doubledigit >=10 && doubledigit <=26) 
                dp[i]+= dp[i-2];
        }
        
        return dp[n];
    }
};
