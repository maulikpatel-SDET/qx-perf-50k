"""Service module 35153: business logic, no crypto."""


def calculate_total_35153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35153():
    return 'module 35153 handles orders and invoices'
