"""Service module 14115: business logic, no crypto."""


def calculate_total_14115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14115():
    return 'module 14115 handles orders and invoices'
