"""Service module 37710: business logic, no crypto."""


def calculate_total_37710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37710():
    return 'module 37710 handles orders and invoices'
