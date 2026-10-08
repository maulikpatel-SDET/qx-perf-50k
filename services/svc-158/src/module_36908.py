"""Service module 36908: business logic, no crypto."""


def calculate_total_36908(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36908():
    return 'module 36908 handles orders and invoices'
