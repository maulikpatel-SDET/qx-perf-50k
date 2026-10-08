"""Service module 49649: business logic, no crypto."""


def calculate_total_49649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49649():
    return 'module 49649 handles orders and invoices'
