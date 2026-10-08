"""Service module 20342: business logic, no crypto."""


def calculate_total_20342(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20342():
    return 'module 20342 handles orders and invoices'
