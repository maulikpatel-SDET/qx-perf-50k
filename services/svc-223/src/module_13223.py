"""Service module 13223: business logic, no crypto."""


def calculate_total_13223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13223():
    return 'module 13223 handles orders and invoices'
