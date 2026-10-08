"""Service module 38917: business logic, no crypto."""


def calculate_total_38917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38917():
    return 'module 38917 handles orders and invoices'
