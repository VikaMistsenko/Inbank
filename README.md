Main function is make_decision(). I retrieve data from a simple form (index.html) that asks the user for personal code, 
loan amount, and loan period. Then I call the function calculate_credit_score(), which returns a credit score for 
certain personal codes, as mentioned in the task. If the credit score is greater than or equal to 1, the algorithm tries
to find a higher loan amount. If the credit score is less than 1, then it tries to find a suitable loan period until it 
reaches 2000. After all these actions, if the credit score is less than 1, the decision is negative and, in this case, 
it renders negativeDecision.html. In other case, the decision is positive and it renders another HTML page.

I have been focused on the algorithm, so the frontend is very simple. I have a lot of ideas on how to improve it, but 
for now, it works and provides an opportunity to test the algorithm.