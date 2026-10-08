"""Service module 36933: business logic, no crypto."""


def calculate_total_36933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36933():
    return 'module 36933 handles orders and invoices'
