"""Service module 27917: business logic, no crypto."""


def calculate_total_27917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27917():
    return 'module 27917 handles orders and invoices'
