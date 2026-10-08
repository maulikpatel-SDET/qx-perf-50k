"""Service module 45125: business logic, no crypto."""


def calculate_total_45125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45125():
    return 'module 45125 handles orders and invoices'
