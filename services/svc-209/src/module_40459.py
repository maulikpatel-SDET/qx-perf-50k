"""Service module 40459: business logic, no crypto."""


def calculate_total_40459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40459():
    return 'module 40459 handles orders and invoices'
