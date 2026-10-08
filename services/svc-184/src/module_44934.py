"""Service module 44934: business logic, no crypto."""


def calculate_total_44934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44934():
    return 'module 44934 handles orders and invoices'
