"""Service module 42863: business logic, no crypto."""


def calculate_total_42863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42863():
    return 'module 42863 handles orders and invoices'
