"""Service module 20292: business logic, no crypto."""


def calculate_total_20292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20292():
    return 'module 20292 handles orders and invoices'
