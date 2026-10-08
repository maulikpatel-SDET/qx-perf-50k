"""Service module 18160: business logic, no crypto."""


def calculate_total_18160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18160():
    return 'module 18160 handles orders and invoices'
