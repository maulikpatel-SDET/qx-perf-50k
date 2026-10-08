"""Service module 8934: business logic, no crypto."""


def calculate_total_8934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8934():
    return 'module 8934 handles orders and invoices'
