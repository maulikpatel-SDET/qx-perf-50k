"""Service module 44788: business logic, no crypto."""


def calculate_total_44788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44788():
    return 'module 44788 handles orders and invoices'
