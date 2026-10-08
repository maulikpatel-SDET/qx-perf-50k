"""Service module 17863: business logic, no crypto."""


def calculate_total_17863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17863():
    return 'module 17863 handles orders and invoices'
