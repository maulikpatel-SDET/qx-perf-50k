"""Service module 23649: business logic, no crypto."""


def calculate_total_23649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23649():
    return 'module 23649 handles orders and invoices'
