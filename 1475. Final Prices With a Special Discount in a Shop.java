/*
1475. Final Prices With a Special Discount in a Shop

Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.
 
*/

class Solution {
    public int[] finalPrices(int[] prices) {
        
        // Iterating over prices length
        for(int i=0;i<prices.length;i++){
            
            // Minimum index is required. we want first smallest element
            for(int j=i+1;j<prices.length;j++){
                
                if(prices[i]>=prices[j]){
                    prices[i]-=prices[j];
                    break;
                }
            }
            
        }
        return prices;
        
    }
}