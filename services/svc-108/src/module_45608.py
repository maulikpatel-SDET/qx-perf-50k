"""Service module 45608: business logic, no crypto."""


def calculate_total_45608(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45608():
    return 'module 45608 handles orders and invoices'
