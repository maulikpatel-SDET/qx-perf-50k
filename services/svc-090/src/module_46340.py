"""Service module 46340: business logic, no crypto."""


def calculate_total_46340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46340():
    return 'module 46340 handles orders and invoices'
