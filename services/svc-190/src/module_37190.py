"""Service module 37190: business logic, no crypto."""


def calculate_total_37190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37190():
    return 'module 37190 handles orders and invoices'
