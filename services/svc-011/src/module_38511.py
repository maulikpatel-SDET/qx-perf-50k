"""Service module 38511: business logic, no crypto."""


def calculate_total_38511(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38511():
    return 'module 38511 handles orders and invoices'
