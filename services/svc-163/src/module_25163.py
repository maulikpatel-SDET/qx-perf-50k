"""Service module 25163: business logic, no crypto."""


def calculate_total_25163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25163():
    return 'module 25163 handles orders and invoices'
