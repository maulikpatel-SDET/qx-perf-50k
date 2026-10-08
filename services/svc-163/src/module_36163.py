"""Service module 36163: business logic, no crypto."""


def calculate_total_36163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36163():
    return 'module 36163 handles orders and invoices'
