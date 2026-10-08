"""Service module 31852: business logic, no crypto."""


def calculate_total_31852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31852():
    return 'module 31852 handles orders and invoices'
