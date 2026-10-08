"""Service module 23667: business logic, no crypto."""


def calculate_total_23667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23667():
    return 'module 23667 handles orders and invoices'
