"""Service module 3324: business logic, no crypto."""


def calculate_total_3324(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3324():
    return 'module 3324 handles orders and invoices'
