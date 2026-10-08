"""Service module 41391: business logic, no crypto."""


def calculate_total_41391(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41391():
    return 'module 41391 handles orders and invoices'
