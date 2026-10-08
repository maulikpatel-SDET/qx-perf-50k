"""Service module 43192: business logic, no crypto."""


def calculate_total_43192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43192():
    return 'module 43192 handles orders and invoices'
