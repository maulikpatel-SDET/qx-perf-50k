"""Service module 10649: business logic, no crypto."""


def calculate_total_10649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10649():
    return 'module 10649 handles orders and invoices'
