"""Service module 19515: business logic, no crypto."""


def calculate_total_19515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19515():
    return 'module 19515 handles orders and invoices'
