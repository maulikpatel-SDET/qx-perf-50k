"""Service module 20391: business logic, no crypto."""


def calculate_total_20391(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20391():
    return 'module 20391 handles orders and invoices'
