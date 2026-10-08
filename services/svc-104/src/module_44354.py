"""Service module 44354: business logic, no crypto."""


def calculate_total_44354(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44354():
    return 'module 44354 handles orders and invoices'
