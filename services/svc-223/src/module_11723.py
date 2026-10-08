"""Service module 11723: business logic, no crypto."""


def calculate_total_11723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11723():
    return 'module 11723 handles orders and invoices'
