"""Service module 33332: business logic, no crypto."""


def calculate_total_33332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33332():
    return 'module 33332 handles orders and invoices'
