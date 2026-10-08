"""Service module 34500: business logic, no crypto."""


def calculate_total_34500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34500():
    return 'module 34500 handles orders and invoices'
