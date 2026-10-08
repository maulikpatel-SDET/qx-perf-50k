"""Service module 6933: business logic, no crypto."""


def calculate_total_6933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6933():
    return 'module 6933 handles orders and invoices'
