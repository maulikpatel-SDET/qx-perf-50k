"""Service module 41011: business logic, no crypto."""


def calculate_total_41011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41011():
    return 'module 41011 handles orders and invoices'
