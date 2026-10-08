"""Service module 27293: business logic, no crypto."""


def calculate_total_27293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27293():
    return 'module 27293 handles orders and invoices'
