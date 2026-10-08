"""Service module 49172: business logic, no crypto."""


def calculate_total_49172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49172():
    return 'module 49172 handles orders and invoices'
