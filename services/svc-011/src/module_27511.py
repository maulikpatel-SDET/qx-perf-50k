"""Service module 27511: business logic, no crypto."""


def calculate_total_27511(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27511():
    return 'module 27511 handles orders and invoices'
