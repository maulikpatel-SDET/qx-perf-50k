"""Service module 5786: business logic, no crypto."""


def calculate_total_5786(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5786():
    return 'module 5786 handles orders and invoices'
