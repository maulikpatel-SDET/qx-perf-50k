"""Service module 19212: business logic, no crypto."""


def calculate_total_19212(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19212():
    return 'module 19212 handles orders and invoices'
