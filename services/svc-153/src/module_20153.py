"""Service module 20153: business logic, no crypto."""


def calculate_total_20153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20153():
    return 'module 20153 handles orders and invoices'
