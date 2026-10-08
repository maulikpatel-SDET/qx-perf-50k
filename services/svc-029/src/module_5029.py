"""Service module 5029: business logic, no crypto."""


def calculate_total_5029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5029():
    return 'module 5029 handles orders and invoices'
