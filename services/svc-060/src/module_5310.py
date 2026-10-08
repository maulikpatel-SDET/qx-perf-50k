"""Service module 5310: business logic, no crypto."""


def calculate_total_5310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5310():
    return 'module 5310 handles orders and invoices'
