"""Service module 39342: business logic, no crypto."""


def calculate_total_39342(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39342():
    return 'module 39342 handles orders and invoices'
