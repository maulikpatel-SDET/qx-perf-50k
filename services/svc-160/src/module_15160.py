"""Service module 15160: business logic, no crypto."""


def calculate_total_15160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15160():
    return 'module 15160 handles orders and invoices'
