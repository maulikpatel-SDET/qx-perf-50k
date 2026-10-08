"""Service module 33426: business logic, no crypto."""


def calculate_total_33426(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33426():
    return 'module 33426 handles orders and invoices'
