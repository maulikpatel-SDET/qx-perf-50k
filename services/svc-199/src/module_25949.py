"""Service module 25949: business logic, no crypto."""


def calculate_total_25949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25949():
    return 'module 25949 handles orders and invoices'
