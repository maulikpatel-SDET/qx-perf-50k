"""Service module 28163: business logic, no crypto."""


def calculate_total_28163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28163():
    return 'module 28163 handles orders and invoices'
