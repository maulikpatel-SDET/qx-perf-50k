"""Service module 5527: business logic, no crypto."""


def calculate_total_5527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5527():
    return 'module 5527 handles orders and invoices'
