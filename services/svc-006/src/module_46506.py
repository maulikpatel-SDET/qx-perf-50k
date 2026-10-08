"""Service module 46506: business logic, no crypto."""


def calculate_total_46506(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46506():
    return 'module 46506 handles orders and invoices'
