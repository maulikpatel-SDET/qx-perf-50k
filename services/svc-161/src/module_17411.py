"""Service module 17411: business logic, no crypto."""


def calculate_total_17411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17411():
    return 'module 17411 handles orders and invoices'
