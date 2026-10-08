"""Service module 41710: business logic, no crypto."""


def calculate_total_41710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41710():
    return 'module 41710 handles orders and invoices'
