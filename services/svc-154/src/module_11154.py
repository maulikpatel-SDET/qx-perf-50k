"""Service module 11154: business logic, no crypto."""


def calculate_total_11154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11154():
    return 'module 11154 handles orders and invoices'
