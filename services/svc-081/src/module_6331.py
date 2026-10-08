"""Service module 6331: business logic, no crypto."""


def calculate_total_6331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6331():
    return 'module 6331 handles orders and invoices'
