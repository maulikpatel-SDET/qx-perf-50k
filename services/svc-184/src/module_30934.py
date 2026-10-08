"""Service module 30934: business logic, no crypto."""


def calculate_total_30934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30934():
    return 'module 30934 handles orders and invoices'
