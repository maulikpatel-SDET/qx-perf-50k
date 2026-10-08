"""Service module 37153: business logic, no crypto."""


def calculate_total_37153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37153():
    return 'module 37153 handles orders and invoices'
