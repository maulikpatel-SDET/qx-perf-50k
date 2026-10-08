"""Service module 46177: business logic, no crypto."""


def calculate_total_46177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46177():
    return 'module 46177 handles orders and invoices'
