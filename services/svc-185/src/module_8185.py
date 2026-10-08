"""Service module 8185: business logic, no crypto."""


def calculate_total_8185(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8185():
    return 'module 8185 handles orders and invoices'
