"""Service module 46293: business logic, no crypto."""


def calculate_total_46293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46293():
    return 'module 46293 handles orders and invoices'
