"""Service module 4340: business logic, no crypto."""


def calculate_total_4340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4340():
    return 'module 4340 handles orders and invoices'
