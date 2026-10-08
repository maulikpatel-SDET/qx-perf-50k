"""Service module 25340: business logic, no crypto."""


def calculate_total_25340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25340():
    return 'module 25340 handles orders and invoices'
