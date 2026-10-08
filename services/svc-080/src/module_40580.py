"""Service module 40580: business logic, no crypto."""


def calculate_total_40580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40580():
    return 'module 40580 handles orders and invoices'
