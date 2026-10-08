"""Service module 40153: business logic, no crypto."""


def calculate_total_40153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40153():
    return 'module 40153 handles orders and invoices'
