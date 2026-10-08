"""Service module 12949: business logic, no crypto."""


def calculate_total_12949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12949():
    return 'module 12949 handles orders and invoices'
