"""Service module 8516: business logic, no crypto."""


def calculate_total_8516(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8516():
    return 'module 8516 handles orders and invoices'
