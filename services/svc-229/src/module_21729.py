"""Service module 21729: business logic, no crypto."""


def calculate_total_21729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21729():
    return 'module 21729 handles orders and invoices'
