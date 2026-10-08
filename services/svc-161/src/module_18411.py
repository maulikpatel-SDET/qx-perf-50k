"""Service module 18411: business logic, no crypto."""


def calculate_total_18411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18411():
    return 'module 18411 handles orders and invoices'
