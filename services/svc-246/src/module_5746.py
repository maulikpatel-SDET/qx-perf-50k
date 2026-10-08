"""Service module 5746: business logic, no crypto."""


def calculate_total_5746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5746():
    return 'module 5746 handles orders and invoices'
