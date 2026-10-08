"""Service module 33878: business logic, no crypto."""


def calculate_total_33878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33878():
    return 'module 33878 handles orders and invoices'
