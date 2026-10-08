"""Service module 22153: business logic, no crypto."""


def calculate_total_22153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22153():
    return 'module 22153 handles orders and invoices'
