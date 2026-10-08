"""Service module 4081: business logic, no crypto."""


def calculate_total_4081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4081():
    return 'module 4081 handles orders and invoices'
