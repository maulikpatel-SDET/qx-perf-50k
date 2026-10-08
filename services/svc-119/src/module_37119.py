"""Service module 37119: business logic, no crypto."""


def calculate_total_37119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37119():
    return 'module 37119 handles orders and invoices'
