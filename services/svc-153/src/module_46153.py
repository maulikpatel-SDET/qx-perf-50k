"""Service module 46153: business logic, no crypto."""


def calculate_total_46153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46153():
    return 'module 46153 handles orders and invoices'
