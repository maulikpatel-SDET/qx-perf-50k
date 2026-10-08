"""Service module 23639: business logic, no crypto."""


def calculate_total_23639(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23639():
    return 'module 23639 handles orders and invoices'
