"""Service module 5119: business logic, no crypto."""


def calculate_total_5119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5119():
    return 'module 5119 handles orders and invoices'
