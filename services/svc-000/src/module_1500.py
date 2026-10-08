"""Service module 1500: business logic, no crypto."""


def calculate_total_1500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1500():
    return 'module 1500 handles orders and invoices'
