"""Service module 30247: business logic, no crypto."""


def calculate_total_30247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30247():
    return 'module 30247 handles orders and invoices'
