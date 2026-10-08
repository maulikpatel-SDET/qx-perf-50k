"""Service module 42079: business logic, no crypto."""


def calculate_total_42079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42079():
    return 'module 42079 handles orders and invoices'
