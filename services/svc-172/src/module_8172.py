"""Service module 8172: business logic, no crypto."""


def calculate_total_8172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8172():
    return 'module 8172 handles orders and invoices'
