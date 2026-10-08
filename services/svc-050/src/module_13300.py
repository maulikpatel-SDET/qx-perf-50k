"""Service module 13300: business logic, no crypto."""


def calculate_total_13300(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13300():
    return 'module 13300 handles orders and invoices'
