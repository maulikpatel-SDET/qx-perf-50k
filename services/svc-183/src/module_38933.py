"""Service module 38933: business logic, no crypto."""


def calculate_total_38933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38933():
    return 'module 38933 handles orders and invoices'
