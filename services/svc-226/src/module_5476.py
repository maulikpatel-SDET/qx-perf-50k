"""Service module 5476: business logic, no crypto."""


def calculate_total_5476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5476():
    return 'module 5476 handles orders and invoices'
