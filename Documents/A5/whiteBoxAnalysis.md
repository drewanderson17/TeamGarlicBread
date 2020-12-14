# Backend Unit test case using White Box testing

The chosen backend method for this implementation is the get_ticket_quantity method.

 ## partitioning
 To create a test case for get_ticket_quantity using basic block coverage, the test case will be partitioned into two tests. The first test will be to have the if statement return true and to test the contents of the if statement. The next test will be to have the if statement return false in order to test the else statement and its contents.

## Deciding code coverage method to use
to test get_ticket_quantity, the code coverage method that makes most sense to use is the basic block coverage method because the chosen backend method does not have any loops to consider, only if statements. That immidiatly makes statement coverage more appealing than decision coverage, and since the method does have an if statement, basic block coverage makes more sense than statement coversage.
 


| Block | X input | y input | test | x | y |
|-------|---------|---------|------|---|---|
| 1     | 0       | 0       | T1   | 0 | 0 |
| 2     | 0       | 0       |      |   |   |
| 3     | 0       | 1       | T2   | 0 | 1 |
| 4     | 0       | 1       |      |   |   |
