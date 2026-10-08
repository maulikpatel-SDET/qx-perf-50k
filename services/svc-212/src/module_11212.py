"""Service module 11212: business logic, no crypto."""


def calculate_total_11212(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11212():
    return 'module 11212 handles orders and invoices'
