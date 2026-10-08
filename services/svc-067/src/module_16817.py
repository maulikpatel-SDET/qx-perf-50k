"""Service module 16817: business logic, no crypto."""


def calculate_total_16817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16817():
    return 'module 16817 handles orders and invoices'
