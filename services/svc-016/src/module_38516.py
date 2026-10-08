"""Service module 38516: business logic, no crypto."""


def calculate_total_38516(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38516():
    return 'module 38516 handles orders and invoices'
