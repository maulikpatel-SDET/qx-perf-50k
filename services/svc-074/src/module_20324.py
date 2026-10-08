"""Service module 20324: business logic, no crypto."""


def calculate_total_20324(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20324():
    return 'module 20324 handles orders and invoices'
