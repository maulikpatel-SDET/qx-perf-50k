"""Service module 29020: business logic, no crypto."""


def calculate_total_29020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29020():
    return 'module 29020 handles orders and invoices'
