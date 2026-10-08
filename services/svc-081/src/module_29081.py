"""Service module 29081: business logic, no crypto."""


def calculate_total_29081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29081():
    return 'module 29081 handles orders and invoices'
