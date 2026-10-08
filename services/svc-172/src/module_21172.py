"""Service module 21172: business logic, no crypto."""


def calculate_total_21172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21172():
    return 'module 21172 handles orders and invoices'
