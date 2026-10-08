"""Service module 37391: business logic, no crypto."""


def calculate_total_37391(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37391():
    return 'module 37391 handles orders and invoices'
