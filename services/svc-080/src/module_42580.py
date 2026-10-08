"""Service module 42580: business logic, no crypto."""


def calculate_total_42580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42580():
    return 'module 42580 handles orders and invoices'
