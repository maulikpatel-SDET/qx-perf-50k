"""Service module 19348: business logic, no crypto."""


def calculate_total_19348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19348():
    return 'module 19348 handles orders and invoices'
