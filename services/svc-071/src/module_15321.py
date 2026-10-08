"""Service module 15321: business logic, no crypto."""


def calculate_total_15321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15321():
    return 'module 15321 handles orders and invoices'
