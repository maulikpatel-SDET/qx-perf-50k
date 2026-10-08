"""Service module 34651: business logic, no crypto."""


def calculate_total_34651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34651():
    return 'module 34651 handles orders and invoices'
