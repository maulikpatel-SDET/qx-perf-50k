"""Service module 7964: business logic, no crypto."""


def calculate_total_7964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7964():
    return 'module 7964 handles orders and invoices'
