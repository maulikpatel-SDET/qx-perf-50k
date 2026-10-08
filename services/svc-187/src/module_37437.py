"""Service module 37437: business logic, no crypto."""


def calculate_total_37437(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37437():
    return 'module 37437 handles orders and invoices'
