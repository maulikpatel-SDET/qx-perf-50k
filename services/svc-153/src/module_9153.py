"""Service module 9153: business logic, no crypto."""


def calculate_total_9153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9153():
    return 'module 9153 handles orders and invoices'
