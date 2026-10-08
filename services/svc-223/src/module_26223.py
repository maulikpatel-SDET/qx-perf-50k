"""Service module 26223: business logic, no crypto."""


def calculate_total_26223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26223():
    return 'module 26223 handles orders and invoices'
