"""Service module 39105: business logic, no crypto."""


def calculate_total_39105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39105():
    return 'module 39105 handles orders and invoices'
