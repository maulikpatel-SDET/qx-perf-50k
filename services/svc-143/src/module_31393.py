"""Service module 31393: business logic, no crypto."""


def calculate_total_31393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31393():
    return 'module 31393 handles orders and invoices'
