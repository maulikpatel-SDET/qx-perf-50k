"""Service module 823: business logic, no crypto."""


def calculate_total_823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_823():
    return 'module 823 handles orders and invoices'
