"""Service module 47820: business logic, no crypto."""


def calculate_total_47820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47820():
    return 'module 47820 handles orders and invoices'
