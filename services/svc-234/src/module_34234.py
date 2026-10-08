"""Service module 34234: business logic, no crypto."""


def calculate_total_34234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34234():
    return 'module 34234 handles orders and invoices'
