"""Service module 19964: business logic, no crypto."""


def calculate_total_19964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19964():
    return 'module 19964 handles orders and invoices'
