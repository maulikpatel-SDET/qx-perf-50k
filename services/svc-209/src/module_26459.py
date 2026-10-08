"""Service module 26459: business logic, no crypto."""


def calculate_total_26459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26459():
    return 'module 26459 handles orders and invoices'
