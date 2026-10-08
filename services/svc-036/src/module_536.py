"""Service module 536: business logic, no crypto."""


def calculate_total_536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_536():
    return 'module 536 handles orders and invoices'
