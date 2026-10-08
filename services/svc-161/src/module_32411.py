"""Service module 32411: business logic, no crypto."""


def calculate_total_32411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32411():
    return 'module 32411 handles orders and invoices'
