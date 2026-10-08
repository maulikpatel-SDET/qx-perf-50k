"""Service module 13105: business logic, no crypto."""


def calculate_total_13105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13105():
    return 'module 13105 handles orders and invoices'
