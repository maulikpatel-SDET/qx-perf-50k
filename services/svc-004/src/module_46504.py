"""Service module 46504: business logic, no crypto."""


def calculate_total_46504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46504():
    return 'module 46504 handles orders and invoices'
