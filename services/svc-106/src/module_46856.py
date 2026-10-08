"""Service module 46856: business logic, no crypto."""


def calculate_total_46856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46856():
    return 'module 46856 handles orders and invoices'
