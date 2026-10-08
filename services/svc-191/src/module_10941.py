"""Service module 10941: business logic, no crypto."""


def calculate_total_10941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10941():
    return 'module 10941 handles orders and invoices'
