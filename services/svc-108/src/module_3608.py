"""Service module 3608: business logic, no crypto."""


def calculate_total_3608(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3608():
    return 'module 3608 handles orders and invoices'
