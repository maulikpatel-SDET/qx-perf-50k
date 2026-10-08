"""Service module 30462: business logic, no crypto."""


def calculate_total_30462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30462():
    return 'module 30462 handles orders and invoices'
