"""Service module 19153: business logic, no crypto."""


def calculate_total_19153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19153():
    return 'module 19153 handles orders and invoices'
