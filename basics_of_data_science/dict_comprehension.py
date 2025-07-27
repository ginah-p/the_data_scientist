def num_classifier(numbers: list) -> None:

    average = sum(numbers) / len(numbers)
    print(f"Average : {average}")

    classification = {}

    # Square each even number
    squared = [x**2 for x in numbers if x % 2 == 0]
    print(f"Squared : {squared}")

    # Classify based on average
    for num in numbers:
        if num < average:
            classification[num] = "Low"
        if num == average:
            classification[num] = "Average"
        else:
            classification[num] = "High"

    even_count = list(classification.values()).count("Even")
    odd_count = list(classification.values()).count("Odd")

    print(classification)
    print(f"Average : ", average)
    print(f"Even : ", even_count)
    print(f"Odd : ", odd_count)
print(num_classifier([2,5,7,10]))


