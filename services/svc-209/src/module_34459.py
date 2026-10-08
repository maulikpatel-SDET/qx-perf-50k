"""Service module 34459: business logic, no crypto."""


def calculate_total_34459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34459():
    return 'module 34459 handles orders and invoices'
