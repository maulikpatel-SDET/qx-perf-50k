"""Service module 30511: business logic, no crypto."""


def calculate_total_30511(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30511():
    return 'module 30511 handles orders and invoices'
