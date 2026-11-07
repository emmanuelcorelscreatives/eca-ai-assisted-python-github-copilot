# Expense tracker acceptance examples

These are proposed behaviors to check before implementation. Each scenario starts from its own stated saved records.

## Example starting set

- Lunch — 12.50 — Food
- Bus — 3.00 — Travel
- Tea — 2.25 — Food

## Add

As someone tracking spending, I want to add an expense so that it is available in my records.

- Success: Given no saved expenses, when I add Lunch for 12.50 in Food, then the tracker reports success and a later list contains that one expense.
- Invalid request: Given no saved expenses, when I try to add an expense without an amount, then the tracker explains that the request is invalid, does not claim success, and still has no saved expenses.

## List

As someone tracking spending, I want to see my expenses so that I can review what I’ve recorded.

- Success: Given the example starting set, when I list expenses, then Lunch, Bus, and Tea each appear once with enough information to distinguish them.
- Empty result: Given no saved expenses, when I list expenses, then the tracker clearly reports an empty list, not an error.
- Read failure: Given that saved expenses cannot be read, when I list expenses, then the tracker reports the problem rather than claiming there are no expenses.

## Filter

As someone tracking spending, I want to see expenses in a chosen category so that I can focus on that spending.

- Success: Given the example starting set, when I filter for Food, then Lunch and Tea appear and Bus does not.
- Empty result: Given the example starting set, when I filter using a supported category with no matches, then the result is clearly empty.
- Invalid request: Given the example starting set, when I submit an unsupported filter request, then the tracker explains that the request is invalid rather than returning all three expenses as though no filter was requested.

## Summarize

As someone tracking spending, I want totals so that I can see how much I spent overall and by category.

- Success: Given the example starting set, when I request a summary, then Food is 14.75, Travel is 3.00, and the overall total is 17.75.
- Empty result: Given no saved expenses, when I request a summary, then the overall total is zero and no spending is attributed to a category.
- Read failure: Given that saved expenses cannot be read, when I request a summary, then the tracker reports that it could not produce the summary rather than presenting zero as a measured total.

## Delete

As someone tracking spending, I want to delete a chosen expense so that an unwanted record no longer appears.

- Success: Given the example starting set, when I delete using the existing identifier for Bus, then a later list contains Lunch and Tea but not Bus.
- Missing record: Given the example starting set, when I delete using an identifier matching no saved expense, then the tracker says no matching expense was deleted and Lunch, Bus, and Tea all remain.

## Review each example

- Does Given establish the starting records without relying on another scenario?
- Does When identify one user action?
- Does Then describe something observable, including what must remain absent or unchanged?
- Are empty results distinguished from invalid requests and failures?
- Are expected totals calculated from the example records rather than copied from an implementation?