"""Service module 39163: business logic, no crypto."""


def calculate_total_39163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39163():
    return 'module 39163 handles orders and invoices'
