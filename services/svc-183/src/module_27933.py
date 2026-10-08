"""Service module 27933: business logic, no crypto."""


def calculate_total_27933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27933():
    return 'module 27933 handles orders and invoices'
