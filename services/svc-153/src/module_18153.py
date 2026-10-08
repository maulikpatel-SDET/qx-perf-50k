"""Service module 18153: business logic, no crypto."""


def calculate_total_18153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18153():
    return 'module 18153 handles orders and invoices'
