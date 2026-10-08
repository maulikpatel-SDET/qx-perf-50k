"""Service module 1933: business logic, no crypto."""


def calculate_total_1933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1933():
    return 'module 1933 handles orders and invoices'
