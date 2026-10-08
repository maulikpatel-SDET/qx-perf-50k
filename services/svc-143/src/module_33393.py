"""Service module 33393: business logic, no crypto."""


def calculate_total_33393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33393():
    return 'module 33393 handles orders and invoices'
