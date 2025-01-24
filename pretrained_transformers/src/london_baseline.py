# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

def run_london_check():
    prediction_lst = ["London" for _ in range(500)]
    total, correct = utils.evaluate_places(filepath=r"birth_dev.tsv", predicted_places=prediction_lst)
    percentage = correct / total
    print(f"The correct percentage is: {percentage}")

if __name__ == '__main__':
    run_london_check()