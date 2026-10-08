"""Service module 39721: business logic, no crypto."""


def calculate_total_39721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39721():
    return 'module 39721 handles orders and invoices'
