"""Service module 16973: business logic, no crypto."""


def calculate_total_16973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16973():
    return 'module 16973 handles orders and invoices'
