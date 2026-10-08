"""Service module 33500: business logic, no crypto."""


def calculate_total_33500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33500():
    return 'module 33500 handles orders and invoices'
