"""Service module 23746: business logic, no crypto."""


def calculate_total_23746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23746():
    return 'module 23746 handles orders and invoices'
