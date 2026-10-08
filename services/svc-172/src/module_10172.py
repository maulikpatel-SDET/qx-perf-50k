"""Service module 10172: business logic, no crypto."""


def calculate_total_10172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10172():
    return 'module 10172 handles orders and invoices'
