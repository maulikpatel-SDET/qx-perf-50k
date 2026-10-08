"""Service module 34914: business logic, no crypto."""


def calculate_total_34914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34914():
    return 'module 34914 handles orders and invoices'
