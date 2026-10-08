"""Service module 11172: business logic, no crypto."""


def calculate_total_11172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11172():
    return 'module 11172 handles orders and invoices'
