"""Service module 6580: business logic, no crypto."""


def calculate_total_6580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6580():
    return 'module 6580 handles orders and invoices'
