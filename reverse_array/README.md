# Reverse Array Example

This repository contains a simple Python script to reverse a list of items and display the results before and after the reversal.

## Description

The script receives a predefined list of items, displays the original list, and then reverses the order of the elements. After a brief delay, the script shows the reversed list.

## Code Structure

- **main()**: Main function that initializes the array, displays the original list, and calls the reversal function.
- **reverse_array(array)**: Function that reverses the given list using an element-swapping approach.
- **print_array(description, array)**: Helper function to display the list with a formatted description.

## Expected Output

When executing the script, the output will be similar to the following example:

```bash
Original Items:  => | item1 | item2 | item3 | item4 | itemN |
--------------------------------------------
Reversed Items:  => | itemN | item4 | item3 | item2 | item1 |
--------------------------------------------
```

## How to Run

1. Ensure you have [Python](https://www.python.org/downloads/) installed.
2. Clone this repository:
   ```bash
   git clone <REPOSITORY-URL>
   cd <FOLDER-NAME>
   ```
3. Execute the script:
   ```bash
   python3 reverse_array.py
   ```

## Logic Explanation

The list reversal is performed using a loop that iterates up to half of the list. For each iteration, a swap of elements between the extremes occurs.

## Possible Improvements

- Add handling for empty lists.
- Include automated tests.
- Allow dynamic list input from the user.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with suggestions for improvements.

