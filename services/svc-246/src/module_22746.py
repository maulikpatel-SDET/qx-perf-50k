"""Service module 22746: business logic, no crypto."""


def calculate_total_22746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22746():
    return 'module 22746 handles orders and invoices'
