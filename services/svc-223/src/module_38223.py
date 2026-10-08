"""Service module 38223: business logic, no crypto."""


def calculate_total_38223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38223():
    return 'module 38223 handles orders and invoices'
