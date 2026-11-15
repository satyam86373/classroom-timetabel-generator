DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MAX_PERIODS_PER_SUBJECT_PER_DAY = 2


def generate_timetable(number_of_days, periods_per_day, subjects):
    """
    Generate a timetable using a greedy scheduling approach.

    subjects is a dictionary whose insertion order determines tie priority.
    Returns a list of days; each day is a list of subject names.
    Raises ValueError if the input constraints cannot be satisfied.
    """

    # Validate day and period limits.
    if not isinstance(number_of_days, int) or not 1 <= number_of_days <= 7:
        raise ValueError("Days must be a whole number from 1 to 7.")

    if not isinstance(periods_per_day, int) or periods_per_day <= 0:
        raise ValueError("Periods per day must be a positive whole number.")

    if not isinstance(subjects, dict) or not subjects:
        raise ValueError("Enter at least one subject.")

    # Keep the original entry order for resolving ties.
    subject_names = list(subjects.keys())    
    remaining = {}

    for name in subject_names:
        count = subjects[name]

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Subject names cannot be empty.")

        if not isinstance(count, int) or count <= 0:
            raise ValueError(
                f"Weekly periods for {name} must be a positive whole number."
            )

        if count > number_of_days * MAX_PERIODS_PER_SUBJECT_PER_DAY:
            raise ValueError(
                f"{name} needs {count} periods, but the limit is "
                f"{MAX_PERIODS_PER_SUBJECT_PER_DAY} per day for "
                f"{number_of_days} day(s)."
            )

        remaining[name] = count

    total_required = sum(remaining.values())
    total_available = number_of_days * periods_per_day

    if total_required != total_available:
        raise ValueError(
            f"Total weekly periods ({total_required}) must equal "
            f"available slots ({total_available})."
        )

    timetable = []

    # Generate one day at a time.
    for day_index in range(number_of_days):
        daily_schedule = []
        daily_count = {name: 0 for name in subject_names}

        for _ in range(periods_per_day):
            # Select the subject with the most periods remaining.
            # In a tie, the earlier entered subject wins.
            eligible_subjects = [
                name for name in subject_names
                if remaining[name] > 0
                and daily_count[name] < MAX_PERIODS_PER_SUBJECT_PER_DAY
            ]

            if not eligible_subjects:
                raise ValueError(
                    "A valid timetable could not be generated "
                    "with the given constraints."
                )

            selected_subject = max(
                eligible_subjects,
                key=lambda name: remaining[name]
            )

            daily_schedule.append(selected_subject)
            remaining[selected_subject] -= 1
            daily_count[selected_subject] += 1

        timetable.append(daily_schedule)

    if any(count != 0 for count in remaining.values()):
        raise ValueError("Some subject periods could not be scheduled.")

    return timetable


def display_timetable(timetable):
    """Print the generated timetable in a readable format."""
    print("\n" + "=" * 42)
    print("             WEEKLY TIMETABLE")
    print("=" * 42)

    for index, schedule in enumerate(timetable):
        print(f"{DAYS[index]}: {', '.join(schedule)}")

    print("=" * 42)


def get_positive_integer(prompt, minimum=1, maximum=None):
    """Read and validate a positive whole number from the console."""
    while True:
        try:
            value = int(input(prompt))

            if value < minimum or (maximum is not None and value > maximum):
                if maximum is not None:
                    print(f"Please enter a number from {minimum} to {maximum}.")
                else:
                    print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("\nCLASSROOM TIMETABLE GENERATOR")
    print("-" * 32)

    try:
        days = get_positive_integer("Enter number of days (1-7): ", 1, 7)
        periods = get_positive_integer("Enter periods per day: ")

        number_of_subjects = get_positive_integer("Enter number of subjects: ")

        subjects = {}

        for index in range(number_of_subjects):
            while True:
                name = input(f"Enter name of subject {index + 1}: ").strip()

                if not name:
                    print("Subject name cannot be empty.")
                elif name in subjects:
                    print("Subject already entered. Enter a different name.")
                else:
                    break

            count = get_positive_integer(
                f"Enter weekly periods for {name}: "
            )
            subjects[name] = count

        timetable = generate_timetable(days, periods, subjects)
        display_timetable(timetable)

    except ValueError as error:
        print("\nERROR:", error)


if __name__ == "__main__":
    main()