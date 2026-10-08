"""Service module 14463: business logic, no crypto."""


def calculate_total_14463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14463():
    return 'module 14463 handles orders and invoices'
