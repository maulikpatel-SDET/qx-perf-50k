"""Service module 46934: business logic, no crypto."""


def calculate_total_46934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46934():
    return 'module 46934 handles orders and invoices'
