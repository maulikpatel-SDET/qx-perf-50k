"""Service module 17016: business logic, no crypto."""


def calculate_total_17016(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17016():
    return 'module 17016 handles orders and invoices'
