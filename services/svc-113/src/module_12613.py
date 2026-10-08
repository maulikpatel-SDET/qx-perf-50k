"""Service module 12613: business logic, no crypto."""


def calculate_total_12613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12613():
    return 'module 12613 handles orders and invoices'
