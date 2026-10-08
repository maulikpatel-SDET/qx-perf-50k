"""Service module 46437: business logic, no crypto."""


def calculate_total_46437(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46437():
    return 'module 46437 handles orders and invoices'
