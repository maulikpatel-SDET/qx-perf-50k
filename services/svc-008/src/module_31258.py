"""Service module 31258: business logic, no crypto."""


def calculate_total_31258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31258():
    return 'module 31258 handles orders and invoices'
