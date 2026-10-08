"""Service module 33287: business logic, no crypto."""


def calculate_total_33287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33287():
    return 'module 33287 handles orders and invoices'
