"""Service module 18213: business logic, no crypto."""


def calculate_total_18213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18213():
    return 'module 18213 handles orders and invoices'
