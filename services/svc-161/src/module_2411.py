"""Service module 2411: business logic, no crypto."""


def calculate_total_2411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2411():
    return 'module 2411 handles orders and invoices'
