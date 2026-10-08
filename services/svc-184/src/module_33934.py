"""Service module 33934: business logic, no crypto."""


def calculate_total_33934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33934():
    return 'module 33934 handles orders and invoices'
