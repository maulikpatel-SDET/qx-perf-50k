"""Service module 32615: business logic, no crypto."""


def calculate_total_32615(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32615():
    return 'module 32615 handles orders and invoices'
