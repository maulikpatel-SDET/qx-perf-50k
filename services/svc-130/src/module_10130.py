"""Service module 10130: business logic, no crypto."""


def calculate_total_10130(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10130():
    return 'module 10130 handles orders and invoices'
