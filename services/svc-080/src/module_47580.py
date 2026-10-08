"""Service module 47580: business logic, no crypto."""


def calculate_total_47580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47580():
    return 'module 47580 handles orders and invoices'
