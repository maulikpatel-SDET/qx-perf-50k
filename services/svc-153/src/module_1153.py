"""Service module 1153: business logic, no crypto."""


def calculate_total_1153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1153():
    return 'module 1153 handles orders and invoices'
