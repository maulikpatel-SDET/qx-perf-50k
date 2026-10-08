"""Service module 13342: business logic, no crypto."""


def calculate_total_13342(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13342():
    return 'module 13342 handles orders and invoices'
