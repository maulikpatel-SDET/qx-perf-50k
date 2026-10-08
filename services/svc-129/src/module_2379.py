"""Service module 2379: business logic, no crypto."""


def calculate_total_2379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2379():
    return 'module 2379 handles orders and invoices'
