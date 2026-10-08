"""Service module 41172: business logic, no crypto."""


def calculate_total_41172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41172():
    return 'module 41172 handles orders and invoices'
