"""Service module 8153: business logic, no crypto."""


def calculate_total_8153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8153():
    return 'module 8153 handles orders and invoices'
