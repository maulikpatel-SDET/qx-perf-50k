"""Service module 5580: business logic, no crypto."""


def calculate_total_5580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5580():
    return 'module 5580 handles orders and invoices'
