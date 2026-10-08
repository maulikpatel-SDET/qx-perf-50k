"""Service module 20011: business logic, no crypto."""


def calculate_total_20011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20011():
    return 'module 20011 handles orders and invoices'
