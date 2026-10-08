"""Service module 14342: business logic, no crypto."""


def calculate_total_14342(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14342():
    return 'module 14342 handles orders and invoices'
