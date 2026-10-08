"""Service module 8356: business logic, no crypto."""


def calculate_total_8356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8356():
    return 'module 8356 handles orders and invoices'
