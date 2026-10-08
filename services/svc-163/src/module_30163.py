"""Service module 30163: business logic, no crypto."""


def calculate_total_30163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30163():
    return 'module 30163 handles orders and invoices'
