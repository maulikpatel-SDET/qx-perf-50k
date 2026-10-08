"""Service module 32212: business logic, no crypto."""


def calculate_total_32212(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32212():
    return 'module 32212 handles orders and invoices'
