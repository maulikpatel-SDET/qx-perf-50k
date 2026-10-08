"""Service module 49715: business logic, no crypto."""


def calculate_total_49715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49715():
    return 'module 49715 handles orders and invoices'
