"""Service module 49933: business logic, no crypto."""


def calculate_total_49933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49933():
    return 'module 49933 handles orders and invoices'
