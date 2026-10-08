"""Service module 44279: business logic, no crypto."""


def calculate_total_44279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44279():
    return 'module 44279 handles orders and invoices'
