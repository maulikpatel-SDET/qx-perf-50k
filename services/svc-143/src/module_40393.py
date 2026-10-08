"""Service module 40393: business logic, no crypto."""


def calculate_total_40393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40393():
    return 'module 40393 handles orders and invoices'
