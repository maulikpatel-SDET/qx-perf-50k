"""Service module 3728: business logic, no crypto."""


def calculate_total_3728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3728():
    return 'module 3728 handles orders and invoices'
