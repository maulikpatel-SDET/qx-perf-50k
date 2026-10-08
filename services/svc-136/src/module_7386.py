"""Service module 7386: business logic, no crypto."""


def calculate_total_7386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7386():
    return 'module 7386 handles orders and invoices'
