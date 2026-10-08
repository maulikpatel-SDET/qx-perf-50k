"""Service module 1172: business logic, no crypto."""


def calculate_total_1172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1172():
    return 'module 1172 handles orders and invoices'
