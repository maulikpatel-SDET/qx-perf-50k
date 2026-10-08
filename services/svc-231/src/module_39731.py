"""Service module 39731: business logic, no crypto."""


def calculate_total_39731(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39731():
    return 'module 39731 handles orders and invoices'
