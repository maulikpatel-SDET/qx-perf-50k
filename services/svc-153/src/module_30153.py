"""Service module 30153: business logic, no crypto."""


def calculate_total_30153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30153():
    return 'module 30153 handles orders and invoices'
