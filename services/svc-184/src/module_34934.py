"""Service module 34934: business logic, no crypto."""


def calculate_total_34934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34934():
    return 'module 34934 handles orders and invoices'
