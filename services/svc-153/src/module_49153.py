"""Service module 49153: business logic, no crypto."""


def calculate_total_49153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49153():
    return 'module 49153 handles orders and invoices'
