"""Service module 15066: business logic, no crypto."""


def calculate_total_15066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15066():
    return 'module 15066 handles orders and invoices'
