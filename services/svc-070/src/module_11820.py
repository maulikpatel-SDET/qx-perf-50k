"""Service module 11820: business logic, no crypto."""


def calculate_total_11820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11820():
    return 'module 11820 handles orders and invoices'
