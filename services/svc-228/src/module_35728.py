"""Service module 35728: business logic, no crypto."""


def calculate_total_35728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35728():
    return 'module 35728 handles orders and invoices'
