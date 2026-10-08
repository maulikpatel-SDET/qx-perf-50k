"""Service module 40445: business logic, no crypto."""


def calculate_total_40445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40445():
    return 'module 40445 handles orders and invoices'
