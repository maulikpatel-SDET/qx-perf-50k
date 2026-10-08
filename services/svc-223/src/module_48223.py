"""Service module 48223: business logic, no crypto."""


def calculate_total_48223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48223():
    return 'module 48223 handles orders and invoices'
