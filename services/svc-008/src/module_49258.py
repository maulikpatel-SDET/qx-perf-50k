"""Service module 49258: business logic, no crypto."""


def calculate_total_49258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49258():
    return 'module 49258 handles orders and invoices'
