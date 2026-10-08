"""Service module 35516: business logic, no crypto."""


def calculate_total_35516(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35516():
    return 'module 35516 handles orders and invoices'
