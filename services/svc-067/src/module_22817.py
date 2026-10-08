"""Service module 22817: business logic, no crypto."""


def calculate_total_22817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22817():
    return 'module 22817 handles orders and invoices'
