"""Service module 13649: business logic, no crypto."""


def calculate_total_13649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13649():
    return 'module 13649 handles orders and invoices'
