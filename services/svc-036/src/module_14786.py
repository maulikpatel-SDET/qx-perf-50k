"""Service module 14786: business logic, no crypto."""


def calculate_total_14786(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14786():
    return 'module 14786 handles orders and invoices'
