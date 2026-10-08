"""Service module 24649: business logic, no crypto."""


def calculate_total_24649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24649():
    return 'module 24649 handles orders and invoices'
