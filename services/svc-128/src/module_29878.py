"""Service module 29878: business logic, no crypto."""


def calculate_total_29878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29878():
    return 'module 29878 handles orders and invoices'
