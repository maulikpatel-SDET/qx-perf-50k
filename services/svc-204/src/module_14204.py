"""Service module 14204: business logic, no crypto."""


def calculate_total_14204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14204():
    return 'module 14204 handles orders and invoices'
