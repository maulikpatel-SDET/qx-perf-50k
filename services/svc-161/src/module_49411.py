"""Service module 49411: business logic, no crypto."""


def calculate_total_49411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49411():
    return 'module 49411 handles orders and invoices'
