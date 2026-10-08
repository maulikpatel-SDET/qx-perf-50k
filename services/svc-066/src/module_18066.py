"""Service module 18066: business logic, no crypto."""


def calculate_total_18066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18066():
    return 'module 18066 handles orders and invoices'
