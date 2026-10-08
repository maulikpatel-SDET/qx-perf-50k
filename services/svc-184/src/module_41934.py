"""Service module 41934: business logic, no crypto."""


def calculate_total_41934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41934():
    return 'module 41934 handles orders and invoices'
