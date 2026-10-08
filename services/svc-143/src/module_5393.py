"""Service module 5393: business logic, no crypto."""


def calculate_total_5393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5393():
    return 'module 5393 handles orders and invoices'
