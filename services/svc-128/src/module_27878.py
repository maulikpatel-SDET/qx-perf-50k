"""Service module 27878: business logic, no crypto."""


def calculate_total_27878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27878():
    return 'module 27878 handles orders and invoices'
