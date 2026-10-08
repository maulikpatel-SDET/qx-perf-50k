"""Service module 28511: business logic, no crypto."""


def calculate_total_28511(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28511():
    return 'module 28511 handles orders and invoices'
