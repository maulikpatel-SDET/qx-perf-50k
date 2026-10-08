"""Service module 34878: business logic, no crypto."""


def calculate_total_34878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34878():
    return 'module 34878 handles orders and invoices'
