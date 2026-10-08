"""Service module 4917: business logic, no crypto."""


def calculate_total_4917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4917():
    return 'module 4917 handles orders and invoices'
