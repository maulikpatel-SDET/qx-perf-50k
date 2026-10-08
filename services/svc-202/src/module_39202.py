"""Service module 39202: business logic, no crypto."""


def calculate_total_39202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39202():
    return 'module 39202 handles orders and invoices'
