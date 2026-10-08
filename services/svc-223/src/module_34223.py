"""Service module 34223: business logic, no crypto."""


def calculate_total_34223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34223():
    return 'module 34223 handles orders and invoices'
