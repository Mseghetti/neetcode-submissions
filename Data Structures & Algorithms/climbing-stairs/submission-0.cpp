class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int back1 = 2;
        int back2 = 1;
        int current = 0;

        for(int i = 3; i <= n; ++i){
            current = back1 + back2;
            back2 = back1;
            back1 = current;
        }

        return current; 
        
    }
};