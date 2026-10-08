"""Service module 18314: business logic, no crypto."""


def calculate_total_18314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18314():
    return 'module 18314 handles orders and invoices'
