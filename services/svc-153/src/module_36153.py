"""Service module 36153: business logic, no crypto."""


def calculate_total_36153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36153():
    return 'module 36153 handles orders and invoices'
