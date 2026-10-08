"""Service module 40223: business logic, no crypto."""


def calculate_total_40223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40223():
    return 'module 40223 handles orders and invoices'
