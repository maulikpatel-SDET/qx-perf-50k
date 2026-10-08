"""Service module 12615: business logic, no crypto."""


def calculate_total_12615(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12615():
    return 'module 12615 handles orders and invoices'
