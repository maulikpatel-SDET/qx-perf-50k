"""Service module 48897: business logic, no crypto."""


def calculate_total_48897(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48897():
    return 'module 48897 handles orders and invoices'
