"""Service module 38143: business logic, no crypto."""


def calculate_total_38143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38143():
    return 'module 38143 handles orders and invoices'
