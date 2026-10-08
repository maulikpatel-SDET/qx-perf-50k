"""Service module 5615: business logic, no crypto."""


def calculate_total_5615(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5615():
    return 'module 5615 handles orders and invoices'
