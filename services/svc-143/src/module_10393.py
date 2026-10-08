"""Service module 10393: business logic, no crypto."""


def calculate_total_10393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10393():
    return 'module 10393 handles orders and invoices'
