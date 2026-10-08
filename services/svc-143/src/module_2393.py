"""Service module 2393: business logic, no crypto."""


def calculate_total_2393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2393():
    return 'module 2393 handles orders and invoices'
