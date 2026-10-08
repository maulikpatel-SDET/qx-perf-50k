"""Service module 19007: business logic, no crypto."""


def calculate_total_19007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19007():
    return 'module 19007 handles orders and invoices'
