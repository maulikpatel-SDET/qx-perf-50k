"""Service module 9379: business logic, no crypto."""


def calculate_total_9379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9379():
    return 'module 9379 handles orders and invoices'
