"""Service module 2204: business logic, no crypto."""


def calculate_total_2204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2204():
    return 'module 2204 handles orders and invoices'
