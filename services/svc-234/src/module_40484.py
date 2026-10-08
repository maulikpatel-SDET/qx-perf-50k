"""Service module 40484: business logic, no crypto."""


def calculate_total_40484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40484():
    return 'module 40484 handles orders and invoices'
