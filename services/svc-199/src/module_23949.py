"""Service module 23949: business logic, no crypto."""


def calculate_total_23949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23949():
    return 'module 23949 handles orders and invoices'
