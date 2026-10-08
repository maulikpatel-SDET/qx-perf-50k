"""Service module 37170: business logic, no crypto."""


def calculate_total_37170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37170():
    return 'module 37170 handles orders and invoices'
