"""Service module 25066: business logic, no crypto."""


def calculate_total_25066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25066():
    return 'module 25066 handles orders and invoices'
