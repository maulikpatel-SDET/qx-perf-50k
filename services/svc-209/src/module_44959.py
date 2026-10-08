"""Service module 44959: business logic, no crypto."""


def calculate_total_44959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44959():
    return 'module 44959 handles orders and invoices'
