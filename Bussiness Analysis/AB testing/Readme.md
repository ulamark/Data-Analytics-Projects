# A / B Testing
## Fast Food Marketing Campaign

This project involves an A/B test analysis of a fast food marketing campaign. The goal is to evaluate A/B (or A/B/C) testing results and decide which marketing strategy out of 3 works the best.

**Description**

A fast-food chain plans to add a new item to its menu. They want to decide between three possible marketing campaigns for promoting the new product. In order to determine which promotion has the greatest effect on sales, the new item is introduced at locations in several randomly selected markets. A different promotion is used at each location, and the weekly sales of the new item are recorded for the first four weeks.

Full project description can be found in a [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1N7-fZcwemQvnYL3StWuqGSTo_k_VOUqYU-voXElibYE/edit?usp=sharing), which contains the SQL code, results, test description, analysis, and recommendations.

## Results & Conclusions

The main analysis question: which promotion out of 3 has the greatest effect on total sales?

H0: all promotion types are equal, there is no difference between them.
HA: all promotion types are NOT equal, there is a statistically significant difference between them.

**1 : 2 promotion**

![image](https://github.com/user-attachments/assets/f0ba832f-1e60-43b7-b4a8-7c9ff814a594)

The P-value is 0.00128, which is less than 0.01. Given that we are using a 99% confidence level, this P-value indicates that the observed difference in **sales between Promotion 1 and Promotion 2 is statistically significant**.
The estimated treatment effect is 43.07 (232.39-189.32), indicating that **Promotion 1 generates, on average, $43.07K more sales per store compared to Promotion 2**.
Since the confidence intervals do not overlap, this suggests there is a significant difference in sales between the two promotions.

**1 : 3 promotion**

![image](https://github.com/user-attachments/assets/80ca6629-46dd-4773-b9f2-5ae3220e4c1c)

The P-value is 0.43, which is much higher than the 0.01 threshold for a 99% confidence level. This means the observed difference in **sales between Promotion 1 and Promotion 3 is NOT statistically significant**.
The estimated treatment effect is 10.93, meaning **Promotion 1 generates an average of $10.93 thousand more sales per store than Promotion 3**.
Since the confidence intervals overlap, this suggests that the difference in sales between Promotion 1 and Promotion 3 is not statistically significant.

**2 : 3 promotion**

![image](https://github.com/user-attachments/assets/6a64b9bc-afd7-408d-af8c-7dce50c49ada)

The P-value is 0.0136, which is slightly above the 0.01 threshold for statistical significance at the 99% confidence level. This means the observed **difference between Promotion 2 and Promotion 3 is NOT statistically significant at the 99% level**.
On average, **Promotion 3 yields $32.14 thousand more in sales per store compared to Promotion 2**.
The slight overlap between the confidence intervals suggests that the difference in sales may not be reliably large enough to rule out the possibility of random variation.

**Recommendation**

To summarize, Promotion 1 outperforms Promotion 2 by a significant margin (statistically significant). Moreover, there is no strong evidence that Promotion 1 is better than Promotion 3. Comparing Promotion 2 vs. Promotion 3, there is no statistically significant difference at the 99% level, though Promotion 3 performs better (it comes close (P-value = 0.0136)).
**Decision:** Do not use Promotion 2, as it performed worse compared to the other promotions. If we need to decide now, use Promotion 1 out of three promotion types.
If company could use two promotion types, use both Promotion 1 and Promotion 3. If the company wants to use only one, it should consider other factors (e.g., cost, marketing reach) when deciding between these two promotions, since neither appears to have a clear advantage based solely on sales performance, or go with further analysis.


