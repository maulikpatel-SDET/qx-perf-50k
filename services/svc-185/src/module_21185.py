"""Service module 21185: business logic, no crypto."""


def calculate_total_21185(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21185():
    return 'module 21185 handles orders and invoices'
