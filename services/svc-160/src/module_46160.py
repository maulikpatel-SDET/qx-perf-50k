"""Service module 46160: business logic, no crypto."""


def calculate_total_46160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46160():
    return 'module 46160 handles orders and invoices'
