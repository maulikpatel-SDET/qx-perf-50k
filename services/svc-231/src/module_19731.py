"""Service module 19731: business logic, no crypto."""


def calculate_total_19731(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19731():
    return 'module 19731 handles orders and invoices'
