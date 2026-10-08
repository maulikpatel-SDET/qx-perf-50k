"""Service module 6587: business logic, no crypto."""


def calculate_total_6587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6587():
    return 'module 6587 handles orders and invoices'
