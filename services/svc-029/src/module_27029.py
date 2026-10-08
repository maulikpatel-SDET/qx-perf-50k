"""Service module 27029: business logic, no crypto."""


def calculate_total_27029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27029():
    return 'module 27029 handles orders and invoices'
