"""Service module 35066: business logic, no crypto."""


def calculate_total_35066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35066():
    return 'module 35066 handles orders and invoices'
