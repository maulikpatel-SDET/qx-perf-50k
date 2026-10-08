"""Service module 40105: business logic, no crypto."""


def calculate_total_40105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40105():
    return 'module 40105 handles orders and invoices'
