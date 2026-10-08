"""Service module 40213: business logic, no crypto."""


def calculate_total_40213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40213():
    return 'module 40213 handles orders and invoices'
