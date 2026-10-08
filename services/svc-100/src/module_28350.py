"""Service module 28350: business logic, no crypto."""


def calculate_total_28350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28350():
    return 'module 28350 handles orders and invoices'
