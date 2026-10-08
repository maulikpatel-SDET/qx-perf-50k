"""Service module 31153: business logic, no crypto."""


def calculate_total_31153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31153():
    return 'module 31153 handles orders and invoices'
